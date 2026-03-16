import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = pd.read_csv("../data/clean_data.csv")
print("===商品推荐系统===")
# 用户商品矩阵
user_product = pd.crosstab(data["用户ID"],data["商品名称"])

# 相似度
similarity = cosine_similarity(user_product)
similarity_df = pd.DataFrame(
    similarity,
    index=user_product.index,
    columns=user_product.index
)

# 推荐函数
def recommend(user_id):
    """
    基于协同过滤的商品推荐函数
    参数:
    user_id: 要推荐商品的用户ID
    返回:
    推荐的前5个商品
    """
    # 如果传入的是数字，转换为U开头的字符串
    if isinstance(user_id, int):
        user_id = f"U{user_id}"
    # 确保user_id是字符串
    user_id = str(user_id)
    # 检查用户是否存在
    if user_id not in similarity_df.columns:
        available = list(similarity_df.columns[:5])
        return f"用户 {user_id} 不存在。可用的用户ID示例：{available}"
    sim_users = similarity_df[user_id].sort_values(
        ascending=False
    ).index[1:6]
    products = data[data["用户ID"].isin(sim_users)]["商品名称"]
    return products.value_counts().head(5)

print("可用的用户ID：", list(user_product.index[:10]))  # 显示前10个用户
# 用户可以选择输入格式
user_input = input("请输入用户ID（如U1003或1003）: ")
try:
    user_id = int(user_input) # 尝试转换为整数，如果是数字输入
except ValueError:
    user_id = user_input # 如果不是数字，保持原样

print(f"为用户 {user_id} 推荐的商品：")
print(recommend(user_id))