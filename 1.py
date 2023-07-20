from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 2023.07-20 课后作业1
bar = (
    # 使用了InitOpts来初始化图的主题
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT,))
    .set_global_opts(
        legend_opts=opts.LegendOpts(pos_right='10%'),
        xaxis_opts=opts.AxisOpts(
            splitline_opts= opts.AxisLineOpts(is_show=False)
    #         axisline_opts=opts.AxisLineOpts(is_show=False),
    #         axistick_opts=opts.AxisTickOpts(is_show=False),
    #         axislabel_opts=opts.LabelOpts(is_show=False)
        ),
        yaxis_opts=opts.AxisOpts(
            axisline_opts=opts.AxisLineOpts(is_show=True),
            splitline_opts=opts.AxisLineOpts(is_show=False),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            # axislabel_opts=opts.LabelOpts(is_show=False)
        ),

    )

    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [10, 21, 30, 15, 80, 92])
    # 使用TitleOpts来初始化了标题和子标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Pyecharts练习",subtitle="柱状图"))
)
bar.render()
