import torch
import torchvision as tv
import torchvision.transforms as transforms
import torch.nn as nn
import torch.optim as optim
import argparse
import os
selfpath=os.path.split(os.path.realpath(__file__))[0].replace("\\","/")#末尾不含斜杠/
cachepath=selfpath+"/cache"
logpath=selfpath+"/LeNet_CPU.log"
from myDataset import mnist
import time
import re
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def checkRunning():
    return os.path.exists(os.path.join(cachepath,"LeNet_CPU.running"))

def checkAndRemove(filename):#一次性标记文档检查
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except:
            pass
        return True
    return False

def checkStop():
    filename=os.path.join(cachepath,"LeNet_CPU.stopnow")
    if os.path.exists(filename):
        try:
            os.remove(filename)
            os.remove(os.path.join(cachepath,"LeNet_CPU.running"))
        except:
            pass
        return True
    return False

def checkSave():#一次性标记文档检查: save
    return checkAndRemove(os.path.join(cachepath,"LeNet_CPU.save"))

def checkLoad():#一次性标记文档检查: load
    return checkAndRemove(os.path.join(cachepath,"LeNet_CPU.load"))

def checkLaunchTraining():#一次性标记文档检查: launch_training
    return checkAndRemove(os.path.join(cachepath,"LeNet_CPU.launch_training"))

def checkLaunchRecog():#一次性标记文件：launch_recog
    return checkAndRemove(os.path.join(cachepath,"LeNet_CPU.launch_recog"))

# 检查是否有其他同类运行程序的标注文件存在，以确保同一时间只有一个LeNetCPU进程。（CPU进程可以和GPU进程共存）
if checkRunning():
    exit()
open(os.path.join(cachepath,"LeNet_CPU.running"),"w").close()#创建“正在运行”的标记文件
logfile=open(logpath,"w",encoding="utf-8")

def log(content):
    global logfile
    logfile.write(time.strftime("[%Y-%m-%d %H:%M:%S] ",time.localtime())+content+"\n")
    logfile.close()
    logfile=open(logpath,"a",encoding="utf-8")

def cleanAndExit():
    checkStop()
    logfile.close()
    exit()

def saveImg(arr,name):
    plt.imshow(arr)
    plt.axis('off')
    plt.savefig(name,bbox_inches="tight")



# 定义是否使用GPU
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")




def show_img(img):
    plt.imshow(img)
    plt.axis('off')
    plt.show()

# 定义网络结构
class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.conv1 = nn.Sequential(     #input_size=(1*28*28)
            nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=2), #padding=2保证输入输出尺寸相同
            nn.ReLU(),      #input_size=(6*28*28)
            nn.MaxPool2d(kernel_size=2, stride=2),#output_size=(6*14*14)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5),
            nn.ReLU(),      #input_size=(16*10*10)
            nn.MaxPool2d(2, 2)  #output_size=(16*5*5)
        )
        self.fc1 = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Linear(120, 84),
            nn.ReLU()
        )
        self.fc3 = nn.Linear(84, 10)

    # 定义前向传播过程，输入为x
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        # nn.Linear()的输入输出都是维度为一的值，所以要把多维度的tensor展平成一维
        x = x.view(x.size()[0], -1)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x

# 超参数设置
# EPOCH = 8   #遍历数据集次数
EPOCH = 1
BATCH_SIZE = 64      #批处理尺寸(batch_size)
LR = 0.001        #学习率

trainset,trainloader,testset,testloader = mnist(selfpath,BATCH_SIZE)

# 定义损失函数loss function 和优化方式（采用SGD）
net = LeNet().to(device)
criterion = nn.CrossEntropyLoss()  # 交叉熵损失函数，通常用于多分类问题上
optimizer = optim.SGD(net.parameters(), lr=LR, momentum=0.9)

state="idle"
log("idle")
while True:
    if state == "idle":
        time.sleep(1)
        if checkStop():
            logfile.close()
            cleanAndExit()
        if checkLoad():
            loadpath=selfpath+'/LeNet.pth'
            try:
                net.load_state_dict(torch.load(loadpath))
                log("load successfully.")
            except:
                log("load failed, file does not exist or unreadable.")
            log("idle")
            continue
        if checkSave():
            savepath=selfpath+'/LeNet_CPU.pth'
            try:
                torch.save(net.state_dict(), savepath)
                log("save successfully.")
            except:
                log("ERROR, cannot save file.")
            log("idle")
            continue
        if checkLaunchTraining():
            state="training"
        if checkLaunchRecog():
            log("recognizing...")
            imgpath=os.path.join(cachepath,"LeNet_CPU_recog.png")
            img = Image.open(imgpath)
            img = img.resize((28,28))
            arr = np.array(img)
            # log("debug0")
            arr[:,:,0]=arr[:,:,0]*0.3
            arr[:,:,1]=arr[:,:,1]*0.59
            arr[:,:,2]=arr[:,:,2]*0.11
            arr=np.sum(arr,axis=2)
            arr=arr.astype(np.float32)
            # log("debug1")
            arr-=np.min(arr)
            arr/=np.max(arr)
            if np.mean(arr)>0.5:#当背景为白色时转换为黑色背景。否则识别常失效，显示为8
                arr=1-arr
            # log("debug2")
            saveImg(arr,os.path.join(cachepath,"LeNet_CPU_recog_.png"))
            # log("debug3")
            images=torch.from_numpy(arr)
            labels=torch.from_numpy(np.array([0]))
            images=torch.reshape(images,[1,1,28,28])
            start_time=time.time()
            with torch.no_grad():
                images, labels = images.to(device), labels.to(device)
                outputs = net(images)
                    # 取得分最高的那个类
                _, predicted = torch.max(outputs.data, 1)
            log("recog result : "+str(predicted.item()))
            end_time=time.time()
            log("time usage : %.3f ms"%(1000*(end_time-start_time)))
            continue
        #checkTraining start?
        #checkRecognition
        continue
    elif state == "recognizing":
        state="idle"
        continue
    elif state == "training":
        open(os.path.join(cachepath,"LeNet_CPU.training"),"w").close()
        for epoch in range(EPOCH):
            sum_loss = 0.0
            # 数据读取
            for i, data in enumerate(trainloader):
                inputs, labels = data
                inputs, labels = inputs.to(device), labels.to(device)

                # 梯度清零
                optimizer.zero_grad()

                # forward + backward
                outputs = net(inputs)
                loss = criterion(outputs, labels)
                loss.backward()
                optimizer.step()

                # 每训练100个batch打印一次平均loss
                sum_loss += loss.item()
                if i % 100 == 99:
                    log('[%d, %d] loss: %.03f'
                        % (epoch + 1, i + 1, sum_loss / 100))
                    sum_loss = 0.0
                    images_in_cpu=torch.Tensor.cpu(inputs)
                    saveImg(images_in_cpu.numpy()[0][0],os.path.join(cachepath,"CPU_training.jpg"))
            # 每跑完一次epoch测试一下准确率
            with torch.no_grad():
                log('testing')
                correct = 0
                total = 0
                flag=True
                for data in testloader:
                    images, labels = data
                    images, labels = images.to(device), labels.to(device)
                    outputs = net(images)
                    # 取得分最高的那个类
                    _, predicted = torch.max(outputs.data, 1)
                    total += labels.size(0)
                    correct += (predicted == labels).sum()
                    if flag:
                        images_in_cpu=torch.Tensor.cpu(images)
                        labels_in_cpu=torch.Tensor.cpu(labels)
                        predicted_in_cpu=torch.Tensor.cpu(predicted)
                        flag=False
                log('第%d个epoch的识别准确率为：%.2f%%' % (epoch + 1, (100 * correct / total)))
        checkAndRemove(os.path.join(cachepath,"LeNet_CPU.training"))
        checkLaunchTraining()#查询，但不开始训练，防止因刷新不同步造成的用户连续触发训练的问题。此点可写在论文中。
        state="idle"
        log("idle")
