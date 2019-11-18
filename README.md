# Image Classification - CIFAR10 - Pytorch

### Tricks 
+ Linear scaling learning rate (LSLR)
+ Learning rate warmup
+ Zero r
+ No bias decay
+ Cosine Learning Rate Decay
+ Label Smoothing (LS)
+ Mixup Training


### AlexNet
> n_epochs=200, batch_size=128 <br>
> SGD(lr=0.01, momentum=0.9, weight_decay=1e-4, nesterov=True) <br>
> MultiStepLR(milestones=[80, 120, 160], gamma=0.1)

| Tricks | #Param | Accuracy |
| ----  | ----   | -------  |
| Alex  | 23.27M  | 84.35% |
|Alex + LSLR * 2 | 23.27M | 84.81% |
|Alex + LSLR * 4 | 23.27M | 84.30% |
|Alex + Warmup   | 23.27M | 84.62% |
|Alex + Cosine | 23.27M | 84.82% |
|Alex + No bias decay| 23.27M | 85.12% |
|Alex + LS | 23.27M | 85.33% |
|Alex + Mixup | 23.27M | 86.18% |
|Alex + Warmup + Cosine| 23.27M | 85.28% |
|Alex + Warmup + Cosine + LS | 23.27M | 85.18% |
|Alex + Warmup + Cosine + Mixup | 23.27M | 86.87% |
|Alex + Warmup + Cosine + LS + Mixup | 23.27M | 86.78%
|Alex + Warmup + Cosein + Mixup + LSLR * 2 | 23.27M | **86.94%** |
|Alex + Warmup + Cosine + Mixup + No bias decay + LSLR * 2 | 23.27M | 86.72% |
|Alex + Warmup + Cosin + Mixup + LS + No bias decay + LSLR * 2| 23.27M | 86.39%|

### VGG
> n_epochs=200, batch_size=128 <br>
> SGD(lr=0.01, momentum=0.9, weight_decay=1e-4, nesterov=True) <br>
> MultiStepLR(milestones=[80, 120, 160], gamma=0.1)

| Tricks | #Param | Accuracy |
| ----  | ----   | -------  |
| VGG11  | 9.75M  | 89.08% |
| VGG11_BN | 9.76M | 90.27%|
| VGG13  | 9.94M | 90.50%|
|VGG13_BN | 9.94M  |91.79%|
|VGG16    |15.25M  |90.33%|
|VGG16_BN |15.25M  |**91.88%**|
|VGG19    |20.55M  |90.48%|
|VGG19_BN  |20.57M |91.69%|

> SGD(lr=0.1, momentum=0.9, weight_decay=1e-4, nesterov=True) <br>

| Tricks | #Param | Accuracy |
| ----  | ----   | -------  |
|VGG16_BN                       |15.25M|         92.95%|
|VGG16_BN + LSLR * 2            |15.25M |        92.92%|
|VGG16_BN + Warmup              |15.25M  |       93.29%|
|VGG16_BN + Warmup + Cosin      |15.25M   |      93.50%|
|VGG16_BN + Warmup + Cosin  + No bias Decay    |15.25M    |     92.99%|
|VGG16_BN + Warmup + Cosin  + LS    |15.25M   |      93.39%|
|VGG16_BN + Warmup + Cosin   + Mixup    |15.25M    |     **94.13%**|
        

### DenseNet
| Model | Layers | #Param | Accuracy |
|  ----  | ----  | ---- | ---- |
|Bottleneck | 100 x 12  | 0.76M| 95.02% |
|Basic      | 100 x 12  | 4.07M| 95.96% |
|Basic      | 100 x 24  | 16M  | 95.16% |

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
