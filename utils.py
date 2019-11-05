import sys
import time
import torch
import datetime
import numpy as np
from visdom import Visdom


class AverageMeter(object):
    """ Computes and stores the average and current value """
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


class Logger(object):
    def __init__(self, n_epochs, monitor, model):
        self.n_epochs = n_epochs
        self.monitor = monitor
        self.model = model
        
        self.epoch = 1
        self.period = 0
        self.best_value = 0
        self.prev_time = time.time()

        self.viz = Visdom()
        self.windows = {}


    def log(self, **kwargs):
        self.period = time.time() - self.prev_time
        self.prev_time = time.time()

        sys.stdout.write('\rEpoch %03d/%03d  ' % (self.epoch, self.n_epochs))
        seconds = int((self.n_epochs - self.epoch) * self.period)
        sys.stdout.write('ETA: %s -- ' % (datetime.timedelta(hours=seconds//3600, minutes=(seconds//60)%60, seconds=seconds%60)))

        for name, dicts in kwargs.items():
            self.add_line(name, dicts)

            for key, val in dicts.items():
                sys.stdout.write('%s: %.4f  ' % (key, val))

                if self.monitor == key and self.best_value < val:
                    self.best_value = val
                    sys.stdout.write(' save')
                    torch.save(self.model.state_dict(), 'best_model.pth')

        sys.stdout.write('\n')
        self.epoch += 1

    def add_line(self, name, dicts):
        for key, val in dicts.items():
            if name not in self.windows:
                self.windows[name] = self.viz.line(X=np.array([self.epoch]), Y=np.array([val]), 
                                                   opts={'xlabel': 'epochs', 'ylabel': name}, name=key)
            else:
                self.viz.line(X=np.array([self.epoch]), Y=np.array([val]), win=self.windows[name], update='append', name=key)