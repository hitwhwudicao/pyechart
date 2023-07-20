from pyecharts.charts import Bar,Page
from pyecharts.globals import ThemeType
from pyecharts.faker import Faker
from  pyecharts import options  as opts
import  random
page = Page()
theme_list = ['essos',
              'infographic',
              'light',
              'macarons',
              'roma',
              'romantic',
              'shine',
              'vintage',
              'walden',
              'westeros',
              'white',       # white是默认主题
              'wonderland']  # 所有内置主题
x_data = Faker.choose()
y_data = Faker.values()
y_data2 = Faker.values()
# 1. 拿数据
for theme in theme_list:
    bar = Bar(
        init_opts=opts.InitOpts(theme=random.choice(theme_list))
    ).add_xaxis(x_data).add_yaxis('name1',y_data).add_yaxis('name2',y_data2)
    page.add(bar)

page.render('page.html')
