import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

data = pd.read_csv("../data/clean_data.csv")

#商品类别销量分析
print("===商品类别销量分析===")
category_sales = data.groupby("商品类别")["购买数量"].sum()
print(category_sales)
#画图
plt.figure()
category_sales.plot(kind="bar")
plt.title("商品类别销量")
plt.xlabel("商品类别")
plt.ylabel("销量")
plt.savefig("../output/商品类别销量.png")
plt.close()
print("商品类别销量对比柱形图已保存")
print()


print("===畅销商品TOP 10分析===")
#商品销量
top_products = data.groupby("商品名称")["购买数量"].sum()
print(top_products.head(10))
#排序
top_products = top_products.sort_values(ascending= False)
print(top_products.head(10))
#画图
plt.figure(figsize=(10,6))
top_products.head(10).plot(kind = "bar")
plt.title("畅销商品 TOP10")
plt.xlabel("商品")
plt.ylabel("销量")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../output/畅销商品.png")
plt.close()
print("畅销商品对比图已保存")
print()


print("===商品关联分析===")
# 构建用户-商品矩阵
basket = pd.crosstab(data["用户ID"],data["商品名称"])
print(basket.head())
print(data.groupby("用户ID")["商品名称"].nunique().describe())
multi_buy = data.groupby("用户ID")["商品名称"].nunique()
print(multi_buy[multi_buy > 1].count())
# 转换为0/1
basket = basket.applymap(lambda x:1 if x>0 else 0)
# 频繁项集
frequent_itemsets = apriori(basket,min_support=0.001,use_colnames=True)
# 关联规则
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.05)
print(rules.head())
#过滤有价值的规则
rules = rules[["antecedents","consequents","support","confidence","lift"]]
rules = rules.sort_values("lift",ascending=False)
print(rules.head(10))
#将结果打印成可读形式
for i, row in rules.head(10).iterrows():
    A = ",".join(list(row["antecedents"]))
    B = ",".join(list(row["consequents"]))
    print(f"{A} → {B}")
    print(f"支持度:{row['support']:.3f}")
    print(f"置信度:{row['confidence']:.2f}")
    print(f"提升度:{row['lift']:.2f}")
    print("------")
print()





