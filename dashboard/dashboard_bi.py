import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv("../data/clean_data.csv")
app = dash.Dash(__name__)

# =====================
# KPI
# =====================
total_sales = data["消费金额"].sum()
total_orders = len(data)
total_users = data["用户ID"].nunique()

# =====================
# 布局
# =====================

app.layout = html.Div(
style={"backgroundColor":"#0d1b2a","color":"white","padding":"20px"},
children=[html.H1("电商用户行为分析 BI 系统",style={"textAlign":"center"}),
# KPI
html.Div([
html.Div([html.H3("总销售额"),html.H2(f"{total_sales}")],
         style={"width":"30%","background":"#1b263b","padding":"20px"}),

html.Div([html.H3("订单数"),html.H2(f"{total_orders}")],
         style={"width":"30%","background":"#1b263b","padding":"20px"}),

html.Div([html.H3("用户数"),html.H2(f"{total_users}")],
         style={"width":"30%","background":"#1b263b","padding":"20px"}),],
         style={"display":"flex","justifyContent":"space-between"}),
# 图表
html.Div([dcc.Graph(id="platform_chart"),dcc.Graph(id="category_chart")],style={"display":"flex"})])

#筛选组件
dcc.Dropdown(id="city_filter",
      options=[{"label":i,"value":i} for i in data["用户城市"].unique()],
      multi=True,
      placeholder="选择城市"
)

#自动刷新
dcc.Interval(id="interval_component",interval=5000,n_intervals=0)

#回调函数
@app.callback(

Output("platform_chart","figure"),
Input("interval_component","n_intervals")

)

def update_chart(n):

    df = pd.read_csv("../data/clean_data.csv")

    platform_sales = df.groupby("平台")["消费金额"].sum().reset_index()

    fig = px.bar(
        platform_sales,
        x="平台",
        y="消费金额",
        template="plotly_dark"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=8050)
