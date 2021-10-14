import os  
import sys  
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib as mpl
import math  
import re  
import pylab  
from pylab import figure, show, legend  
from mpl_toolkits.axes_grid1 import host_subplot  
 
fp = open(r'C:/Users/Surface/Desktop/out.txt', 'r')
  
train_epochs = []  
learningrate = [] 
train_loss = []  
test_epochs = []  
#test_accuracy = []  
i=0 
for ln in fp:  
  # get train_iterations and train_loss  
  if 'END' in ln and 'epoch' in ln: 
    arr = re.findall(r'loss: (.*?)lr:',ln)  
    train_epochs.append(int(i))
    #print(re.findall(r'top1: (.*?) top5',ln))
    train_loss.append(float(re.findall(r' top1_avg: (.*?) top5',ln)[0]))#top1数值在字符  top1_avg: 和 top5之间
    i=i+1 
fp.close()  
# plot curves  
plt.plot(train_epochs, train_loss, label="dilated+delete pooling",color='#542788')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.yticks(fontsize= 10.5)
plt.xticks(fontsize= 10.5)
plt.xlim([-10,200])  
plt.ylim([0., 1]) 
plt.legend(loc="upper right",fontsize=10.5)  
# plt.savefig('d:/Users/Administrator/Desktop/loss曲线.jpg',dpi=100)
plt.show()