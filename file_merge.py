import pandas as pd
import os
import numpy as np
import time 

# 时间戳
now_time = time.strftime(r'%Y-%m-%d_%H:%M:%S', time.localtime())

# 存放文件的文件夹
input_dir = r"C:\Users\surface\Desktop\submission"

# 创建空的DataFrame
df_empty = pd.DataFrame(columns=['sample_index',])


# os库的walk功能遍历文件夹里的所有文件，并读取文件名字
for parents, dirnames, filenames in os.walk(input_dir):
    # print(parents,dirnames,filenames)  # 主文件夹 次级文件夹 文件名
    for filename in filenames:
        df = pd.read_csv(os.path.join(parents,filename))
        df_empty['sample_index'] = df['sample_index']
        df_empty = pd.concat([df_empty,df['predict_category']],axis=1)   # append 是增加原表格的长度 concat是增加宽度
 

#分别求行最大值及最大值所在索引
# df_empty['max_value']=df_empty.max(axis=1)
# df_empty['max_index']=np.argmax(df_empty,axis=1)


# 获取每行出现次数最多的值，并计算出现的次数
value = df_empty.apply(lambda x: x.value_counts().index[0], axis=1)
count = df_empty.apply(lambda x: x.value_counts().iloc[0], axis=1)

df_count = pd.concat([value, count], axis=1).reset_index()
df_count.columns = ['row_num', 'val', 'appearing']

# 原始df加入新的计数列
df_empty = pd.concat([df_empty,df_count['val'],df_count['appearing']],axis=1) 

# 将结果写入CSV表格
df_upload = pd.DataFrame()
df_upload = pd.concat([df_upload,df_empty['sample_index'],df_empty['val']],axis=1)
df_upload.columns = ['sample_index', 'predict_category']
save_file = str(now_time[5:13]) + ".csv"
df_upload.to_csv(save_file,index=None)

print(save_file)
print(df_upload.head())