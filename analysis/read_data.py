import pandas as pd
#分别读取数据
pdd=pd.read_csv("../data/拼多多.csv")
tb=pd.read_csv("../data/淘宝.csv")

#添加 平台 字段
pdd["平台"] = "拼多多"
tb["平台"] = "淘宝"

#查看前5行数据
print("拼多多数据：")
print(pdd.head())
print("淘宝数据：")
print(tb.head())

#查看数据结构
print("拼多多数据结构：")
print(pdd.info())
print("淘宝数据结构：")
print(tb.info())

#合并数据
data = pd.concat([pdd,tb],ignore_index=True)
print("合并后的数据：")
print(data.head())

#查看数据量
print("总数据量：",data.shape)
print("拼多多数据量：",pdd.shape)
print("淘宝数据量：",tb.shape)

#保存合并后的数据
data.to_csv("../data/电商用户数据.csv",index=False)#index=False 只保存数据列不保存行索引
print("合并数据保存成功")

