import torch

from metrics import accuracy
from utils import AverageMeter


def train(train_loader, model, criterion, optimizer):
    losses = AverageMeter()
    top1 = AverageMeter()

    model.train()
    for input, target in train_loader:
        if torch.cuda.is_available():
            input, target = input.cuda(), target.cuda()

        output = model(input)
        loss = criterion(output, target)
        prec = accuracy(output, target)[0]

        losses.update(loss.item(), input.size(0))
        top1.update(prec.item(), input.size(0))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    return top1.avg, losses.avg


def validate(val_loader, model, criterion):
    losses = AverageMeter()
    top1 = AverageMeter()

    model.eval()
    with torch.no_grad():
        for input, target in val_loader:
            if torch.cuda.is_available():
                input, target = input.cuda(), target.cuda()

            output = model(input)
            loss = criterion(output, target)
            prec = accuracy(output, target)[0]

            losses.update(loss.item(), input.size(0))
            top1.update(prec.item(), input.size(0))

    return top1.avg, losses.avg
    