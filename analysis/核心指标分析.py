import pandas as pd
import matplotlib.pyplot as plt

# 读取清洗后的数据
data = pd.read_csv("../data/clean_data.csv")
print(data.head())
#1 总销售额(所有订单金额加起来)
total_sales = data["消费金额"].sum()
#2 订单数量(数据总行数,一行一订单)
order_count = data.shape[0]
#3 用户数量(去重后的用户数量)
user_total = data["用户ID"].nunique()
#4 平均客单价
avg_value = total_sales / order_count

print("===== 电商核心指标 =====")
print("总销售额：", total_sales)
print("订单数量：", order_count)
print("用户数量：", user_total)
print("平均客单价：", avg_value)
print()

#Matplotlib默认字体不支持中文显示,需重新设置
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

#平台销售额分析
print("按平台统计销售额:")
platform_sales = data.groupby("平台")["消费金额"].sum()
print(platform_sales)
#画图
plt.figure()
platform_sales.plot(kind = "bar") #柱状图
plt.title("平台销售额对比")
plt.xlabel("平台")
plt.ylabel("销售额")
plt.savefig("../output/平台销售额对比.png",dpi=300,bbox_inches="tight")
plt.close()
print("平台销售额对比柱形图已保存")
print()





