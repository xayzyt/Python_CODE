# json格式数据可以作为桥梁，让不同编程语言相通
# json可以是字典格式也可以是列表
import json
# 列表变字符串（json）
data = [{"name":"张云腾","age": 21},{"name":"张腾","age": 22},{"name":"张云","age": 23}]
json_str = json.dumps(data,ensure_ascii=False)
print(json_str)
print(type(json_str))
# 字典变字符串
d = {"name":"张云腾","age": 21}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str)
print(type(json_str))
# 将json转变python列表
s = '[{"name": "张云腾", "age": 21}, {"name": "张腾", "age": 22}, {"name": "张云", "age": 23}]'
l = json.loads(s)
print(l)
print(type(l))

# pyecharts
# 基础折线图
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
from pyecharts.charts import Line
line = Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,20,10])

# set_global_opts 全局配置
line.set_global_opts(
    title_opts=TitleOpts(title = "GDP展示",pos_left="center",pos_bottom="20px",pos_top="20px"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()# 生成图像

