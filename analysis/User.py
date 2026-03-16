import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

data = pd.read_csv("../data/clean_data.csv")

print("===用户年龄分布分析===")
# 年龄分布
plt.figure()
plt.hist(data["用户年龄"], bins=10)#直方图
plt.title("用户年龄分布")
plt.xlabel("年龄")
plt.ylabel("人数")
plt .savefig("../output/用户年龄分布.png")
plt.close()
print("用户年龄分布直方图已保存")
print()

#城市消费排名
print("===用户城市消费排名分析===")
city_sales = data.groupby("用户城市")["消费金额"].sum()
print(city_sales.head())
print()
#排序
city_sales = city_sales.sort_values(ascending=False)
print("城市消费金额前十名：")
print(city_sales.head(10))
#画图
plt.figure()
city_sales.head(10).plot(kind = "bar")
plt.title("城市消费TOP10")
plt.xlabel("城市")
plt.ylabel("消费金额")
plt.savefig("../output/城市消费Top10.png")
plt.close()
print("用户城市消费排名前十对比图已保存")
print()


print("===用户消费能力分层===")
#每个用户的消费总额
user_spending = data.groupby("用户ID")["消费金额"].sum()
print(user_spending.head())
#用户等级划分
labels  = ["低消费","中消费","高消费"]#定义三个等级的名称
user_level = pd.qcut(user_spending,3,labels = labels)#pd.qcut() 是pandas的分位数切分函数,user_spending 是要切分的数据,3 表示要分成3个等级,labels=labels 给这三个等级命名
#统计每个等级有多少个用户
level_count = user_level.value_counts()
print(level_count)

#绘制饼图
plt.figure(figsize=(6,6))
colors = ["#66c2a5","#fc8d62","#8da0cb"]

level_count.plot(kind = "pie",
                 autopct = "%1.1f%%",#绘制饼图,在饼图上显示百分比（保留1位小数）
                 colors=colors,

                 startangle=90,#从90度开始画
                 counterclock=False)#顺时针

plt.title("用户消费能力分布",fontsize = 14)
plt.ylabel("")#去掉y轴
plt.axis("equal")#保证是圆形
plt.savefig ("../output/用户消费能力等级")
plt.close()
print("用户消费能力等级图已保存")

print()
print("===用户活跃时间分析===")
#小时购买量
hour_sales = data.groupby("小时")["购买数量"].sum()
print(hour_sales.head())
#绘制折线图
plt.figure(figsize=(10,6))
hour_sales.plot(kind="line", marker="o")
plt.title("用户购买时间分布")
plt.xlabel("小时")
plt.ylabel("购买量")
plt.grid()
plt.savefig("../output/用户购买时间分布")
plt.close()
print("用户购买时间分布图已保存")

print()
print("===用户复购率分析===")
#统计每个用户订单数量
user_orders = data.groupby("用户ID").size()
print(user_orders.head())
#复购用户
repeat_users = user_orders[user_orders >1]
print(repeat_users.head())
#复购率
repeat_rate = len(repeat_users)/len(user_orders)
print("用户总数：", len(user_orders))
print("复购用户：", len(repeat_users))
print("复购率：", repeat_rate)
#绘制饼图
labels = ["复购用户","单次购买用户"]
repeat_count = int(len(repeat_users))
single_count = int(len(user_orders)-len(repeat_users))
values = [repeat_count,single_count]
plt.figure()
plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.title("用户复购率")
plt.savefig("../output/用户复购率")
plt.close()
print("用户复购率图已保存")

print()
print("===用户消费漏斗分析===")
import plotly.graph_objects as go
import os
#漏斗
stages = ["浏览商品","加入购物车","下单","支付"]
values = [10000, 6000, 3500, 2800]
#计算转化率
view = values[0]
cart = values[1]
order = values[2]
pay = values[3]
cart_rate = cart / view
order_rate = order / cart
pay_rate = pay / order
#计算流失率
cart_loss = 1 - cart_rate
order_loss = 1 - order_rate
pay_loss = 1 - pay_rate
#输出
print("\n===转化率===")
print(f"浏览 → 加购 转化率: {cart_rate:.2%}")
print(f"加购 → 下单 转化率: {order_rate:.2%}")
print(f"下单 → 支付 转化率: {pay_rate:.2%}")
print("\n===流失率===")
print(f"浏览 → 加购 流失率: {cart_loss:.2%}")
print(f"加购 → 下单 流失率: {order_loss:.2%}")
print(f"下单 → 支付 流失率: {pay_loss:.2%}")
print("\n===分析结论===")
if cart_loss > 0.4:
    print("浏览到加购阶段流失较高，可能商品吸引力不足或价格偏高")
if order_loss > 0.4:
    print("加购到下单阶段流失较高，建议优化结算流程")
if pay_loss > 0.3:
    print("下单到支付阶段流失较高，可能支付体验存在问题")
print()
#绘制漏斗图
fig = go.Figure(go.Funnel(y = stages,x = values,textinfo="value+percent initial"))
fig.update_layout(title = "用户消费漏斗分析")
fig.show()
#保存
os.makedirs("output",exist_ok=True)
fig.write_html("../output/用户消费漏斗图")
print("用户消费漏斗图已保存")