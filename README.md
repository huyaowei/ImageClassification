# Image Classification - CIFAR10

Tricks 
+ Linear scaling learning rate
+ Learning rate warmup
+ Zero \gamma
+ No bias decay
+ Cosine Learning Rate Decay
+ Label Smoothing
+ Mixup Training


### AlexNet
n_epochs=200, batch_size=128
SGD(lr=0.01, momentum=0.9, weight_decay=1e-4, nesterov=True)
MultiStepLR(milestones=[80, 120, 160], gamma=0.1)


| Tricks | #Param | Accuracy |
| ----  | ----   | -------  |
| Alex  | 23.27M  | 84.35% |
|Alex + LSLR * 2 | 23.27M | 84.81% |
|Alex + LSLR * 4 | 23.27M | 84.30% |
|Alex + Warmup   | 23.27M | 84.62% |
|Alex + Cosine Decay | 23.27M | 84.82% |
|Alex + No bias decay| 23.27M | 85.12% |
|Alex + Label Smoothing | 23.27M | 85.33% |
|Alex + Mixup Training | 23.27M | 86.18% |
|Alex + Warmup + Cosine Decay | 23.27M | 85.28% |
|Alex + Warmup + Cosine Decay + Label Smoothing | 23.27M | 85.18% |
|Alex + Warmup + Cosine Decay + Mixup Training | 23.27M | 86.87% |
|Alex + Warmup + Cosine Decay + Label Smoothing + Mixup Training | 23.27M | 86.78%
|Alex + Warmup + Cosein Decay + Mixup Training + LSLR * 2 | 23.27| 86.94% |
|Alex + Warmup + Cosine Decay + Mixup Training + No bias decay + LSLR * 2 | 23.27M | 86.72% |
|Alex + Warmup + Cosin Decay + Mixup Training + Label Smoothing + No bias decay + LSLR * 2| 23.27M | 86.39%|

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
