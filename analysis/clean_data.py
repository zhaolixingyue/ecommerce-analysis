import pandas as pd
data = pd.read_csv("../data/电商用户数据.csv")
print("数据量：",data.shape)
print(data.head())
print("数据结构：")
print(data.info())

#查看是否存在空值
print("各列空值数量：")
print(data.isnull().sum())
#data = data.dropna()  删除空值

#处理时间字段
data["购买时间"] = pd.to_datetime(data["购买时间"])
#提取时间信息
data["年份"] = data["购买时间"].dt.year
data["月份"] = data["购买时间"].dt.month
data["日期"] = data["购买时间"].dt.day
data["小时"] = data["购买时间"].dt.hour
print("数据结构：")
print(data.info())

print(data.head())

# 保存清洗后的数据
data.to_csv("../data/clean_data.csv", index=False)

print("\n数据清洗完成，已保存")