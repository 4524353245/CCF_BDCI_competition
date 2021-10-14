import numpy as np
import random
import pandas as pd

train_label = np.load('data/data104925/train_label.npy',encoding = "latin1") 
train_data = np.load('data/data104925/train_data.npy',encoding = "latin1") 

data_label=pd.DataFrame(train_label)

# 少样本的标签
few_label = [21,16,19,7,10,28,15,6,17,24,29,25,14,12,3]
few_label = sorted(few_label) # 有小到大排序
few_label_copy = few_label

idx = {}
label = []
flag = False
train_label_list = train_label.tolist()
# idx 为少样本在训练集中的位置
for i in range(train_label.size):
    for j in range(len(few_label)):
        if train_label_list[i] == few_label[j]:
            idx[i] = few_label[j]
            if train_label_list[i] not in label:
                label.append(few_label[j])

# 根据缺失值 将所有的索引以二级数组的形式存储
add_idx = []
single_idx = []

for i in few_label:
    for j in idx.keys():
        if i == idx[j]:
            single_idx.append(j)
    add_idx.append(single_idx)
    single_idx = []


# lack 为少样本缺少的数值 是按照标签的从小到大来的
count = data_label.value_counts()
lack_value = []
for i in range(count.size):
    if count[i].values != 140:
        lack_value.append(140-int(count[i].values))


# add_label
add_label = []
for i in range(len(few_label)):
    for j in range(lack_value[i]):
        add_label.append(few_label[i])
    # print(add_label.count(few_label[i])) # 计算列表中某个值出现的次数


## 添加label标签
final_label = np.concatenate((train_label, add_label), axis=0)
# print(final_label.shape)

# 添加train_data
add_data = []
for i in range(len(few_label)):
    for j in range(lack_value[i]):
        add_data.append(train_data[random.choice(add_idx[i]),:,:,:,:])
add_data = np.array(add_data)
final_data = np.concatenate((train_data, add_data), axis=0)


