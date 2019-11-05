import argparse
from sklearn.model_selection import StratifiedShuffleSplit

import torch.nn as nn
import torch.optim as optim
import torch.backends.cudnn as cudnn
from torch.optim.lr_scheduler import MultiStepLR
from torch.utils.data import DataLoader, Subset

from torchvision import models
from torchvision import transforms
from torchvision.datasets import CIFAR10

from training import *
from utils import *
from models.wide_resnet import *


parser = argparse.ArgumentParser()
parser.add_argument('--valid_radio', type=int, default=0.1)

parser.add_argument('--n_epochs', type=int, default=200)
parser.add_argument('--batch_size', type=int, default=128)

parser.add_argument('--lr', type=float, default=0.1)
parser.add_argument('--momentum', type=float, default=0.9)
parser.add_argument('--weight_decay', type=float, default=5e-4)

opt = parser.parse_args()

####################### data ############################
train_transforms = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.491, 0.482, 0.447), (0.247, 0.243, 0.262))
])
test_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.491, 0.482, 0.447), (0.247, 0.243, 0.262))
])

train_dataset = CIFAR10(root='../data', train=True, transform=train_transforms)
valid_dataset = CIFAR10(root='../data', train=True, transform=test_transforms)
test_dataset = CIFAR10(root='../data', train=False, transform=test_transforms)

################# train and valid split ####################

labels = [train_dataset[i][1] for i in range(len(train_dataset))]
ss = StratifiedShuffleSplit(n_splits=1, test_size=0.1)
train_indices, valid_indices = list(ss.split(np.array(labels)[:, np.newaxis], labels))[0]
train_dataset = Subset(train_dataset, train_indices)
valid_dataset = Subset(valid_dataset, valid_indices)

train_loader = DataLoader(train_dataset, batch_size=opt.batch_size, shuffle=True, num_workers=4)
valid_loader = DataLoader(valid_dataset, batch_size=100, num_workers=4)
test_loader = DataLoader(test_dataset, batch_size=100, num_workers=4)

###################### Model ############################
model = wide_resnet(20, 10)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=opt.lr, momentum=opt.momentum, weight_decay=opt.weight_decay)
scheduler = MultiStepLR(optimizer, [60, 120, 160], gamma=0.2)

if torch.cuda.is_available():
    model = nn.DataParallel(model).cuda()
    model = model.cuda()
    criterion = criterion.cuda()
    cudnn.benchmark = True

###################### Training #########################
logger = Logger(opt.n_epochs, 'valid_acc', model)
for epoch in range(1, opt.n_epochs + 1):
   
   tr_acc, tr_loss = train(train_loader, model, criterion, optimizer)
   va_acc, va_loss = validate(valid_loader, model, criterion)
   scheduler.step()
   
   logger.log(loss={'train_loss': tr_loss, 'valid_loss': va_loss},
              acc={'train_acc': tr_acc, 'valid_acc': va_acc})

##################### Test #############################
model.load_state_dict(torch.load('best_model.pth'))
model = model.module
test_acc, test_loss = validate(test_loader, model)
print("Test Acc:{:.4f} Test Loss{:.4f}".format(test_acc, test_loss))
