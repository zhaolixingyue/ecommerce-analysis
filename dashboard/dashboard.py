import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

data = pd.read_csv("../data/clean_data.csv")
print("数据已读取")

# KPI指标
total_sales = data["消费金额"].sum()
total_orders = len(data)
total_users = data["用户ID"].nunique()

# 平台销售额
platform_sales = data.groupby("平台")["消费金额"].sum().reset_index()
fig_platform = px.bar(platform_sales, x="平台", y="消费金额", title="平台销售额")

# 商品类别
category_sales = data.groupby("商品类别")["购买数量"].sum().reset_index()
fig_category = px.pie(category_sales, names="商品类别", values="购买数量")

# 城市消费
city_sales = data.groupby("用户城市")["消费金额"].sum().reset_index()
city_sales = city_sales.sort_values("消费金额", ascending=False).head(10)
fig_city = px.bar(city_sales, x="用户城市", y="消费金额")

# 时间分析
hour_sales = data.groupby("小时")["购买数量"].sum().reset_index()
fig_hour = px.line(hour_sales, x="小时", y="购买数量")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("电商用户行为数据分析大屏",
            style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.H3("总销售额"),
            html.H2(f"{total_sales}")
        ], className="card"),

        html.Div([
            html.H3("订单数量"),
            html.H2(f"{total_orders}")
        ], className="card"),

        html.Div([
            html.H3("用户数量"),
            html.H2(f"{total_users}")
        ], className="card"),
    ], style={"display": "flex",
              "justifyContent": "space-around"}),

    html.Div([
        dcc.Graph(figure=fig_platform),
        dcc.Graph(figure=fig_category)
    ], style={"display": "flex"}),

    html.Div([
        dcc.Graph(figure=fig_city),
        dcc.Graph(figure=fig_hour)
    ], style={"display": "flex"}),

])


if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=8050)




