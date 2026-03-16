import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 读取数据
data = pd.read_csv("../data/clean_data.csv")
print("===销量预测模型===")

# 按日期统计销量
daily_sales = data.groupby("日期")["购买数量"].sum().reset_index()
X = daily_sales[["日期"]]
y = daily_sales["购买数量"]

# 训练模型
model = LinearRegression()
model.fit(X, y)

# 预测
pred = model.predict(X)
print(pred)

# 画图
plt.figure(figsize=(8,5))
plt.scatter(X, y, label="真实销量")
plt.plot(X, pred, color="red", label="预测趋势")
plt.title("销量预测趋势")
plt.xlabel("日期")
plt.ylabel("销量")
plt.legend()
plt.savefig("../output/销量预测模型")
plt.close()
print("销售预测模型图已保存")

print()
print("===用户流失预测模型===")
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
# 用户消费统计
user_data = data.groupby("用户ID").agg({
    "消费金额":"sum",
    "购买数量":"sum",
    "商品ID":"count"
}).reset_index()

# 模拟流失标签
user_data["流失"] = user_data["商品ID"].apply(lambda x: 1 if x < 2 else 0)

# 特征
X = user_data[["消费金额","购买数量"]]
y = user_data["流失"]

# 划分数据
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)
# 模型
model = RandomForestClassifier()
model.fit(X_train,y_train)
pred = model.predict(X_test)
print(classification_report(y_test,pred))





