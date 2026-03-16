import pandas as pd

data = pd.read_csv("../data/clean_data.csv")

total_sales = data["消费金额"].sum()
orders = len(data)
users = data["用户ID"].nunique()

top_city = data.groupby("用户城市")["消费金额"].sum().idxmax()

report = f"""
电商用户行为分析报告

1. 总销售额：{total_sales}
2. 订单数量：{orders}
3. 用户数量：{users}
4. 消费最高城市：{top_city}

分析结论：用户消费集中在核心城市，建议加强高消费城市营销投放。
"""

with open("../output/analysis_report.txt","w",encoding="utf-8") as f:
    f.write(report)

print("报告生成成功")