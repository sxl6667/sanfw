import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as plot
import numpy as np

# 设置所有列可见
pd.set_option('display.max_columns', None)
# 设置可视化字体 不设置将显示不出字体
plot.rc('font', family='Microsoft YaHei')


# 第一题
"""
1 - 加载数据
读取当前目录下
东京奥运会奖牌数据.csv -> df1
东京奥运会奖牌分日数据.csv -> df2
"""
df1 = pd.read_csv('./东京奥运会奖牌数据.csv', encoding='utf-8')
df2 = pd.read_csv('./东京奥运会奖牌分日数据.csv', encoding='utf-8')
# print(df1)
# print(df2)


# 第二题
"""
2- 修改列名
将原 df1 列名 Unnamed: 2、Unnamed: 3、Unnamed: 4 修改为 金牌数、银牌数、铜牌数
"""
df1 = df1.rename(columns={'Unnamed: 2': '金牌数', 'Unnamed: 3': '银牌数', 'Unnamed: 4': '铜牌数'})
# print(df1.dtypes)


# 第三题
"""
3 - 数据类型查看
查看 df2 的数据类型
"""
# print(df2.dtypes)


# 第四题
"""
4 - 类型修改
将 df2 的获奖时间修改为 时间格式
"""
df2['获奖时间'] = pd.to_datetime(df2['获奖时间'])
# print(df2.dtypes)


# 第五题
"""
5 - 数据排序
将 df2 按照获奖时间升序排列
注意：原始数据可能有一点问题，射击队杨倩应该是东京首金
"""
df2.sort_values(by='获奖时间', ascending=True, inplace=True)
# print(df2.head(5))


# 第六题
"""
6 - 匹配修改
给 df2 新增一列国家，总奖牌数，值根据 国家id 与 df1 匹配
"""
df2['国家'] = df2['国家id'].apply(lambda x: df1.loc[df1['国家id'] == x, '国家奥委会'].values[0])
df2['总奖牌数'] = df2['国家id'].apply(lambda x: df1.loc[df1['国家id'] == x, '总分'].values[0])
# print(df2.head())


# 第七题
"""
7 - 分组统计
通过对 df2 的国家进行分组统计，计算每个国家的奖牌总数（也就是出现次数）
并查看奖牌数前5名，结果可以用 df1 进行验证
"""
np2 = df2['国家'].value_counts()
# print(np2.head(5))


# 第八题
"""
通过 df2 计算获得奖牌最多的运动员
注意：仅统计单人项目
"""
np3 = df2['运动员'].value_counts()
# print(np3.head(5))


# 第九题
"""
9 - 数据查看
查看乒乓球项目的全部信息
"""
df3 = df2.loc[df2['运动类别'] == '乒乓球', :]
# print(df3)


# 第十题
"""
10 - 数据透视
查看各国在不同项目上的获奖牌情况
国家是索引，运动类别是列，值是数量相加
"""
df_p = df2.pivot_table(index=['国家', '运动类别'], aggfunc='count', values='总奖牌数')
# print(df_p)
# print(df_p.loc['中国', :].sum())


# 第十一题
"""
11 - 数据查询
在上一题的基础上，查询中国队的获奖牌详情
"""
# print(df_p.loc['中国', :])


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
df2['获奖时间'] = df2['获奖时间'].apply(lambda x: '%d月%d日' % (x.month, x.day))
# print(df2['获奖时间'])


# 第十四题
"""
14 - 分组统计
查看每天产生奖牌的数量
"""
df_fz = df2['获奖时间'].value_counts()
# print(df_fz)


# 第十五题
"""
15 - 数据透视
查看不同项目在不同国家的分布情况
"""
# print(df2[['运动类别', '国家']].value_counts())
# print(df2.pivot_table(index=['运动类别', '国家'], values='总奖牌数', aggfunc='count'))

# 第十六题
"""
16 - 数据计算
计算中国每日总奖牌数量
"""
df_js = df2.loc[df2['国家'] == '中国', :].pivot_table(index=['获奖时间', '国家'], values='奖牌类型', aggfunc='count')
date = df_js['奖牌类型'].values
newdate = []
for i in range(len(date)):
    newdate.append(date[:i+1].sum())
df_js['奖牌类型'] = newdate
# print(df_js)


# 第十七题
"""
计算前十名各国每日奖牌数量合计
注意：对于第一天没有数据的国家用0填充，其余时间的缺失值用上一日数据填充
"""
fen10 = df1.sort_values(by='总分', ascending=False)['总分'].values[9]  # 获取第10名的奖牌数
df_js10 = df2.loc[df2['总奖牌数'] >= fen10, :].pivot_table(index='获奖时间', columns='国家', values='总奖牌数', aggfunc='count')  # 进行数据透视
df_js10.fillna(0, inplace=True)  # 填充缺失值
df_js10 = df_js10.astype(int)  # 修改数据类型
for i in range(16):  # 让当前行的值为当前行加上上一行
    if i == 0:
        continue
    df_js10.iloc[i, :] = df_js10[i-1: i+1].sum(axis=0).values
# print(df_js10)


# 第十八题
"""
18 - 条形图
对金牌数量排行前10的国家制作条形图
"""


def example18():
    df18 = df1.copy()
    df18.index = df18['国家奥委会']
    df18 = df18[0:10]['金牌数']
    df18.plot(kind='bar')
    plt.ylabel('金牌数')
    plt.title('奥运会金牌数排名')
    plt.show()


# example18()


# 第十九题
"""
19 - 堆叠图
将排行榜前十名的奖牌绘制堆叠图
"""


def example19():
    # 获取前十的奖牌
    df19 = df1.copy()
    df19 = df19.sort_values(by='总分', ascending=False)[:10]
    df19.index = df19['国家奥委会']
    df19 = df19.loc[:, ['金牌数', '银牌数', '铜牌数']]
    df19.plot(kind='bar', stacked=True, title='图')
    plt.show()


# example19()


# 第二十题
"""
20 - 饼图
绘制中国队的奖牌分布饼图
"""


def example20():
    df20 = df2.copy()
    plt.figure(dpi=300)
    # df20 = df20.pivot_table(index=['运动类别', '国家'], values='总奖牌数', aggfunc='count').query('国家 == ["中国"]')
    df20 = df20.loc[df20['国家'] == '中国', '运动类别'].value_counts()
    df20.plot(kind='pie', autopct='%.2f%%')
    plt.show()


# example20()


# 第二十一题
"""
21 - 地图
绘制各国奖牌分布热力地图
"""


def example21():
    from pyecharts import options as opts
    from pyecharts.charts import Map
    import json

    countrys = list(df1['国家奥委会'])
    data = list(df1['总分'])
    with open('name_map.json', 'r', encoding='utf8')as fp:
        name = json.load(fp)

    c = (
        Map()
            .add("", [list(z) for z in zip(countrys, data)], "world", is_map_symbol_show=False, name_map=name)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="东京奥运会奖牌分布"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
            .render(path='各国奖牌分布热力地图.html')
    )


# example21()


# 第二十二题
"""
22 - 动态图
将排行榜前十名的奖牌变化动态展示
"""


def example22():
    pass


# example22()
