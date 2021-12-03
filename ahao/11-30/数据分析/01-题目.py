import json

import pandas as pd
import matplotlib.pyplot as plt
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
import random
# from pyecharts.charts import Geo
# from pyecharts.faker import Faker
# from pyecharts.globals import ChartType
import os

plt.rcParams['font.family'] = 'SimHei'

# 第一题
"""
1 - 加载数据
读取当前目录下
东京奥运会奖牌数据.csv -> df1
东京奥运会奖牌分日数据.csv -> df2
"""
df1 = pd.read_csv('东京奥运会奖牌数据.csv', encoding='utf-8')
df2 = pd.read_csv('东京奥运会奖牌分日数据.csv', encoding='utf-8')
# print(df1.head())
# print(df2.head())

# 第二题
"""
2- 修改列名
将原 df1 列名 Unnamed: 2、Unnamed: 3、Unnamed: 4 修改为 金牌数、银牌数、铜牌数
"""
df1.rename(columns={'Unnamed: 2': '金牌数', 'Unnamed: 3': '银牌数', 'Unnamed: 4': '铜牌数'}, inplace=True)
# print(df1.head())

# 第三题
"""
3 - 数据类型查看
查看 df2 的数据类型
"""
# print(df1.dtypes)

# 第四题
"""
4 - 类型修改
将 df2 的获奖时间修改为 时间格式
"""
df2['获奖时间'] = pd.to_datetime(df2['获奖时间'], format='%Y%m%d %H:%M')
# print(df2['获奖时间'].dtype)
# print(df2.head())

# 第五题
"""
5 - 数据排序
将 df2 按照获奖时间升序排列
"""
df2.sort_values(by=['获奖时间'], ascending=True, inplace=True)
# print(df2)

# 第六题
"""
6 - 匹配修改
给 df2 新增一列国家, 总奖牌数，值根据 国家id 与 df1 匹配
注意：原始数据可能有一点问题，射击队杨倩应该是东京首金
"""
df3 = df1[['国家id', '国家奥委会', '总分']]
df2 = pd.merge(df2, df3, how='outer', on='国家id')
df2.rename(columns={'总分': '总奖牌数', '国家奥委会': '国家'}, inplace=True)
# print(df2.head())

# 第七题
"""
7 - 分组统计
通过对 df2 的国家进行分组统计，计算每个国家的奖牌总数（也就是出现次数）
并查看奖牌数前5名，结果可以用 df1 进行验证
"""
# print(df2['国家'].value_counts(ascending=False).head())


# 第八题
"""
通过 df2 计算获得奖牌最多的运动员
注意：仅统计单人项目
"""
df3 = df2.loc[(~df2['运动员'].str.contains('队')) & (~df2['运动员'].str.contains('/'))]
# print(df3['运动员'].value_counts(ascending=False))
# 或
# df3 = df2.loc[(df2['运动员'].str.contains('队')==False) & (df2['运动员'].str.contains('/')==False)]
# print(df3['运动员'].value_counts(ascending=False).head())

# 第九题
"""
9 - 数据查
查看乒乓球项目的全部信息
"""
# print(df2.loc[df2['运动类别'] == '乒乓球'])

# 第十题
"""
10 - 数据透视
查看各国在不同项目上的获奖牌情况
"""
df3 = df2.groupby(['国家', '运动类别'])['总奖牌数'].count().to_frame()
# print(df3)


# 第十一题
"""
11 - 数据查询
在上一题的基础上，查询中国队的获奖牌详情
"""
# print(df3.loc['中国', :])

# 第十二题
"""
12 - 个性化查看
在数据框中根据奖牌数量进行可视化
"""

# 第十三题
"""
13 - 数据格式化
将 df2 的获奖时间格式化为 x月x日
"""
df2['获奖时间'] = df2['获奖时间'].dt.strftime('%#m月%#d日')

# 第十四题
"""
14 - 分组统计
查看每天产生奖牌的数量
"""
# print(df2['获奖时间'].value_counts())
# 或
# print(df2.groupby('获奖时间').count()['奖牌类型'])

# 第十五题
"""
15 - 数据透视
查看不同项目在不同国家的分布情况
"""
# print(df2.groupby(['运动类别', '国家']).count()['总奖牌数'])

# 第十六题
"""
16 - 数据计算
计算中国每日总奖牌数量
"""
df3 = df2.loc[df2['国家'] == '中国']
w = df3.groupby('获奖时间').count()['总奖牌数'].to_frame()
s = df3.groupby('获奖时间').count()['总奖牌数'].values
all = 0
new = []
for i in range(len(s)):
    all = all + s[i]
    new.append(all)
w['总奖牌数'] = new
# print(w)


# 第十七题
"""
计算前十名各国每日奖牌数量合计
注意：对于第一天没有数据的国家用0填充，其余时间的缺失值用上一日数据填充
"""
df1.sort_values(by=['按总数排名'], ascending=True, inplace=True)
states = df1['国家奥委会'].head(10).values
time = df2['获奖时间'].value_counts().sort_index().index.values
data = {}
for state in states:
    df3 = df2.loc[df2['国家'] == state]
    s = df3.groupby('获奖时间').count()['总奖牌数']
    s = s.reindex(time, fill_value=0).sort_index()
    all = 0
    new = []
    for i in range(len(s)):
        all = all + s[i]
        new.append(all)
    data.update({state: new})
df4 = pd.DataFrame(data, index=time, columns=states)
# print(df4)


# 第十八题
"""
18 - 条形图
对金牌数量排行前10的国家制作条形图
"""
# df1.sort_values(by=['金牌数', '总分'], ascending=False, inplace=True)
# x = df1['国家奥委会'].head(10).values
# y = df1['金牌数'].head(10).values
# plt.bar(x=range(len(x)), height=y, width=0.4)
# plt.xticks(range(len(x)), x)
# plt.title('东京奥运会金牌数前十的国家')
# plt.xlabel('国家奥委会')
# plt.ylabel('金牌数')
# plt.show()

# 第十九题
"""
19 - 堆叠图
将排行榜前十名的奖牌绘制堆叠图
"""
# 方法一
# df1.sort_values(by=['总分', '金牌数'], ascending=False, inplace=True)
# x = df1['国家奥委会'].head(10).values
# y1 = df1['金牌数'].head(10).values
# y2 = df1['银牌数'].head(10).values
# y3 = df1['铜牌数'].head(10).values
# data = {'金牌': y1, '银牌': y2, '铜牌': y3}
# df = pd.DataFrame(data, index=x)
# print(df)
# df.plot(kind='bar', stacked=True)
# plt.show()

# 方法二
# df1.sort_values(by=['总分', '金牌数'], ascending=False, inplace=True)
# x = df1['国家奥委会'].head(10).values
# y1 = df1['金牌数'].head(10).values
# y2 = df1['银牌数'].head(10).values
# y3 = df1['铜牌数'].head(10).values
# d = []
# for i in range(len(y1)):
#     d.append(y1[i] + y2[i])
# plt.bar(x, y1, width=0.4, color='Gold', label="金牌")
# plt.bar(x, y2, width=0.4, bottom=y1, color='Silver', label="银牌")
# plt.bar(x, y3, width=0.4, bottom=d, color='#B87333', label="铜牌")
# plt.legend(loc='best')
# plt.show()

# 第二十题
"""
20 - 饼图
绘制中国队的奖牌分布饼图
"""
# df = df2.loc[df2['国家'] == '中国']
# s = df['运动类别'].value_counts()
# sizes = list(s.values)
# labels = s.index.values
# print(sizes)
# print(labels)
# plt.pie(sizes, labels=labels)
# plt.show()

# 第二十一题
"""
21 - 地图
绘制各国奖牌分布热力地图
"""
# df2.sort_values(by=['总奖牌数'], ascending=False, inplace=True)
# df = df2.drop_duplicates(subset=['国家'])
# states = list(df['国家'].values)
# numbers = df['总奖牌数'].values.tolist()
# print(type(numbers[0]))
# with open('name_map.json', 'r', encoding='utf-8') as f:
#     name = json.loads(f.read())
# c = (
#     Map()
#     .add("", [list(z) for z in zip(states, numbers)], "world", is_map_symbol_show=False, name_map=name)
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="东京奥运会各国奖牌数"),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#
#     )
#     .render(path="东京奥运会奖牌热力图.html")
# )


# 第二十二题
"""
22 - 动态图
将排行榜前十名的奖牌变化动态展示
"""


# print(df4)
states = df4.columns.values.tolist()
dates = df4.index.values.tolist()

t1 = Timeline()  # 创建 Timeline对象
for i in dates:
    bar = (
        Bar()
            .add_xaxis(random.sample(states, len(states)))
            .add_yaxis('奖牌书', list(df4.loc[i, :]), label_opts=opts.LabelOpts(position='right'),
                       )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='right'))
            .reversal_axis()
            .set_global_opts(title_opts=opts.TitleOpts("{}".format(i),
                                                       pos_left='50%',
                                                       ),
                             legend_opts=opts.LegendOpts(pos_right='10%'))
    )
    t1.add(bar, '{}'.format(i))
    t1.add_schema(
        symbol='arrow',  # 设置标记时间；
        orient='horizontal',
        symbol_size=2,  # 标记大小;
        play_interval=900,  # 播放时间间隔；
        control_position='right',  # 控制位置;
        linestyle_opts=opts.LineStyleOpts(width=5,
                                          type_='dashed',
                                          color='rgb(255,0,0,0.5)'),
        label_opts=opts.LabelOpts(color='rgb(0,0,255,0.5)',
                                  font_size=15,
                                  font_style='italic',
                                  font_weight='bold',
                                  font_family='Time New Roman',
                                  position='left',
                                  interval=20,
                                  )
    )
    t1.render("动态图.html")
