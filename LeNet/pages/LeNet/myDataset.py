import torch
import torchvision as tv
import torchvision.transforms as transforms


def mnist(path,BATCH_SIZE):
    # 定义数据预处理方式
    transform = transforms.ToTensor()

    # 定义训练数据集
    trainset = tv.datasets.MNIST(
        root=path,
        train=True,
        download=False,
        transform=transform)

    # 定义训练批处理数据
    trainloader = torch.utils.data.DataLoader(
        trainset,
        batch_size=BATCH_SIZE,
        shuffle=True,
        )

    # 定义测试数据集
    testset = tv.datasets.MNIST(
        root=path,
        train=False,
        download=False,
        transform=transform)

    # 定义测试批处理数据
    testloader = torch.utils.data.DataLoader(
        testset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        )

    return (trainset,trainloader,testset,testloader)