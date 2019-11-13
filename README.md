# Image Classification - CIFAR10

### Resnet
| Model | Layers | #Param | Accuracy |
|  ----  | ----  | ---- | ---- |
|Bottelneck | 100 x 12  | 0.76M|  |

### Resnet
| Model | Layers | Accuracy | Model | Layers | Accuracy |
|  ----  | ----  | ---- | ---- | ----| ---|
|           |20   | 91.59% |           |    20 |91.61%|
|BasicBlock |56   | 92.83% | Bottleneck|    56 |92.55%|
|           |110  | 93.05% |           |    110|93.28%|

### Tricks-Resnet20-BasicBlock
| Trick | Parameter | Accuracy|
|----   |----     |----|
|Baseline         | batch_size=128, lr=0.1  |91.59%|
|+warmup          | batch_size=128, lr=0.1  |91.31%|
|+warmup + cosin  | batch_size=128, lr=0.1  |91.27%|
|+linear Scale * 2| batch_size=256, lr=0.2  |91.67%|
|+linear Scale * 2 + zero $/gamma$|batch_size=256, lr=0.2|91.57%|
|+linear Scale * 2 + Weight Decay| batch_size=256, lr=0.2  |91.49%|
|+linear Scale * 2 + Xavier| batch_size=256, lr=0.2 | 91.28%|
|+linear Scale * 2 + warmup + cosin| batch_size=256, lr=0.2|91.64%|
|+linear Scale * 4| batch_size=512, lr=0.4  |90.71%|
|+linear Scale * 8| batch_size=1024, lr=0.8 |89.45%|


### Tricks-Resnet20-Bottleneck
| Trick | Parameter | Accuracy|
|----   |----     |----|
|Baseline         | batch_size=128, lr=0.1  |91.61%|
|+linear Scale * 2| batch_size=256, lr=0.2  |90.37%|
|+linear Scale * 2 + Model D| batch_size=256, lr=0.2 |91.01%|
