import pandas as pd
import matplotlib as plot
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
plot.rc('font', family='Microsoft YaHei')


# 第一大题——数据读取
def read():
    # 1.读取data.csv文件，把第一行作为列
    df = pd.read_csv('./data.csv', encoding='gbk', header=0)
    # 2.不把第一行作为列 (默认以数字作为列)
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=None)
    # 3.有列名，替换列名
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=0, names=list('abcdefghij'))
    # 4.没有列名，设置列名
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=None, names=list('abcdefghij'))
    # 5.指定订单号和订单行为索引
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=0, index_col=['订单号', '订单行'])
    # 6.仅想读取订单号和订单行
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=0, usecols=['订单号', '订单行'])
    # 7.仅想读取前100行数据
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=0, nrows=100)
    # 8.跳过前100行数据,并设置列名为字母a-j
    df1 = pd.read_csv('./data.csv', encoding='gbk', header=None, skiprows=100, names=list('abcdefghij'))
    # 9.将第1题的数据导出为data1.csv,
    df.to_csv('data1.csv', encoding='gbk')

    # 返回第一题活得的数据
    return df


# 第二大题——数据清洗
def clear():
    # 获取数据
    df1 = read()
    # 1.查看有多少重复值
    print(df1.duplicated().value_counts())
    # 2.查看是重复项的前五项
    print(df1.loc[df1.duplicated(), :].head(5))
    # 3.对订单号与订单行重复的进行删除, 保留第一次出现
    df1.drop_duplicates(subset=['订单号', '订单行'], keep='first', inplace=True)
    print(df1.duplicated().value_counts())
    # 4.查看每一列是否有空值
    print(df1.isnull().any())
    # 5.查看每一列有多少空值
    print(df1.isnull().sum())
    # 6.查看有空值的行
    print(df1.loc[df1.isnull().any(axis=1), :])

    # 7-10操作的是同一个数据源，最终以7的结果为后续的操作值
    # 7.删除缺失值(只要行中有一个缺失值就删除该行)
    df3 = df1.dropna(how='any', axis=0)
    print(df3.isnull().any())
    # 8.缺失值填充01  填充0
    df2 = df1.fillna(0)
    print(df2.loc[[2, 10, 32, 59], :])
    # 9.缺失值填充02  字典填充, 订单号为空时填充"无订单号"， 货品交货状况为空填充中"按时交货"，数量为空填充 中位数
    df2 = df1.fillna({'订单号': '无订单号', '货品交货状况': '按时交货', '数量': df1['数量'].median()})
    print(df2.loc[[2, 10, 32, 59], :])
    # 10.缺失值填充03    向前填充与向后填充  缺失值向后填充
    df2 = df1.fillna(method='bfill')
    print(df2.loc[[2, 10, 32, 59], :])
    # 11.将销售金额转化为float类型
    df3 = df3.copy()
    df3['销售金额'] = df3['销售金额'].replace(',', '.', regex=True).replace('元', '', regex=True).apply(lambda x: getX(x))
    print(df3)
    # 12.对数据进行描述性分析
    print(df3.describe())
    # 13.画出散点图观察异常值
    plt.scatter(df3['数量'], df3['销售金额'])
    plt.xlabel('数量')
    plt.ylabel('金额')
    # plt.show()
    # 14.(用自己的理解直接处理异常值)由图可见，可把数量超过4000，金额大于50000的当作异常值，删除
    df6 = df3.loc[df3['数量'] < 4000, :].loc[df3['销售金额'] < 50000]
    print(df6.describe())
    # 15.(使用均值和标准差进行判断)  公式：数据的正常范围[mean-2 * std, mean+2 * std]  异常值用中位数填充
    df5 = df3.copy()
    df5 = df5['数量']
    mean = df5.mean()
    std = df5.std()
    df5[(df5 <= mean - 2 * std) | (df5 >= mean + 2 * std)] = np.nan
    df5.fillna(df5.median(), inplace=True)
    # df5.dropna(inplace=True)
    print(df5.describe())
    # 16.(使用上四中位数和下四中位数进行异常值判定) 正常值的范围应在 [mean2-1.5×mean3，mean1+1.5×mean2] 异常值用中位数填充
    a = df3['数量'].quantile(0.75)
    b = df3['数量'].quantile(0.25)
    df4 = df3['数量']
    df4 = df4.copy()
    df4[(df4 >= (a - b) * 1.5 + a) | (df4 <= b - (a - b) * 1.5)] = np.nan
    df4.fillna(df4.median(), inplace=True)
    # print(df4.describe())

    print(df6.describe())
    return df6


# 第三答题——数据规整
def zhengli():
    # 本题创建的是虚拟数据不用获取前面的返回值
    # 1.设定索引 使用Series创建Series对象 并且设置索引为a, b, c, d
    sis = pd.Series(data=[1, 2, 3, 5], index=['a', 'b', 'c', 'd'])
    sis = pd.Series(np.arange(1, 10, 2), list('abcde'))
    print(sis)
    # 2.设定索引 使用DataFrame创建DataFrame对象 并且设置索引
    df = pd.DataFrame(data=[['谭方盛', 18, '帅气'], ['孙濠', 20, '一般子'], ['舒祥龙', 20, '丑一批']], index=['one', 'two', 'three'], columns=['姓名', '年龄', '颜值'])
    print(df)
    # 3.修改第二题索引 改为1,2,3类型
    df.index = [1, 2, 3]
    print(df)
    # 4.给索引命名  my_index
    df.index.name = 'my_index'
    print(df)
    # 5.分别使用DataFrame 原始方法，和loc与iloc三种方法取到舒祥龙的颜值
    yanzhi = df[df['姓名'] == '舒祥龙']['颜值'].values[0]
    yanzhi = df.loc[df['姓名'] == '舒祥龙', '颜值'].values[0]
    yanzhi = df.iloc[2, 2]
    print(yanzhi)
    # 6.修改列名 将姓名修改为名字，年龄修改为岁数
    df.rename(columns={'姓名': '名字', '年龄': '岁数'}, inplace=True)
    print(df)
    # 7.添加一列 添加一列 出生年月日 '2003-08-20'
    df['出生年月日'] = ['2003-08-20', '2000-09-16', '2001-09-16']
    print(df)
    # 8.查看数据类型
    print(df.dtypes)
    # 9.查看数据形状
    print(df.shape)
    # 10.查看数据大小
    print(df.size)
    # 11.查看数据详细信息
    print(df.info())
    # 12.修改数据类型 把岁数修改为float类型，把出生年月日修改为时间类型 再次查看数据类型
    df['岁数'] = df['岁数'].astype(float)
    df['出生年月日'] = pd.to_datetime(df['出生年月日'], errors='coerce')
    print(df.dtypes)
    # 13.更改数据内容 给名字前添加'帅哥'两字, 给名字后添加两个空格
    df['名字'] = df['名字'].apply(lambda x: '帅哥'+x+'  ')
    print(df)
    # 14.去除名字中的空值
    df['名字'] = df['名字'].apply(lambda x: x.strip())
    print(df)
    # 15.去除孙濠和舒祥龙前面的帅哥  保留帅哥谭方盛  切记！！！（这个是个知识点）
    df['名字'] = df['名字'].apply(lambda x: getName(x))
    print(df)
    # 16. 排序  索引排序  按照索引降序排序
    df.sort_index(inplace=True, ascending=False)
    print(df)
    # 17. 按照岁数降序排序
    df.sort_values(by='岁数', ascending=False, inplace=True)
    # 18. 先添加列’出生日‘，按照出生日降序排序
    df['出生日'] = df['出生年月日'].apply(lambda x: x.day)
    df.sort_values(by='出生日', inplace=True, ascending=False)
    print(df)
    # 19. 数据拼接 一对一 将本目录文件table_join_exp.xlsx的 Sheet1表，和Sheet2表，通过编号连接（注意：一个Excel文件中可有多个表）
    df1 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet1')
    df2 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet2')
    df3 = pd.merge(df1, df2)
    print(df3)
    # 20. 数据拼接 一对多 当一个表的公共列是唯一的，另一个表的公共列则会有重复的数据， 取出table_join_exp.xlsx 的Sheet3 合并 Sheet1
    df3 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet3')
    df4 = pd.merge(df1, df3, on='编号')
    print(df4)
    # 21. 根据上题 修改分数_x, 分数_y 的格式为分数_one,分数_two  在merge中添加参数解决
    df4 = pd.merge(df1, df3, on='编号', suffixes=("_one", "_two"))
    print(df4)
    # 22. 多对多 取出Sheet4 与 Sheet3合并
    df5 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet4')
    df6 = pd.merge(df3, df5, on='编号')
    print(df6)
    # 23. 连接方式 内连接  内连接就是取两个表中公共的部分  内连接 Sheet5 和 Sheet3
    df5 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet5')
    df6 = pd.merge(df5, df3, on='编号', how="inner")
    print(df6)
    # 24. 连接方式 左连接  左连接就是已左表为基础，右表像左表上拼数据  左连接  Sheet5 和 Sheet3
    df6 = pd.merge(df5, df3, on='编号', how="left")
    print(df6)
    # 25. 连接方式 右连接   sheet5, sheet3
    df6 = pd.merge(df5, df3, on='编号', how="right")
    print(df5)
    print(df3)
    print(df6)
    # 26. 外连接 外连接就是两个表的并集 sheet5  sheet3
    df6 = pd.merge(df5, df3, on='编号', how="outer")
    print(df6)
    # 27. 纵向拼接  拼接 Sheet5  Sheet6  并且用参数重置索引
    df6 = pd.read_excel('./table_join_exp.xlsx', sheet_name='Sheet6')
    df7 = pd.concat(objs=[df5, df6], ignore_index=True)
    print(df7)
    # 28. 数据分组  导入需要操作的数据   epidemic_dxy.xlsx   以continents进行分组  查看七大洲的数据条数
    df8 = pd.read_excel("./epidemic_dxy.xlsx")
    df9 = df8.groupby(['continents']).count()
    # 29. 数据分组以continents进行分组  查看七大洲疫情的汇总
    df9 = df8.groupby(['continents']).sum()
    print(df9)
    # 30. 以continents provinceName进行分组  并汇总
    df9 = df8.groupby(['continents', 'provinceName']).sum()
    print(df9)
    # 31. 如果我们想在一次分组中，进行两次汇总运算，aggregate()  以continents分组 取'confirmedCount', 'suspectedCount',
    # 'curedCount', 'deadCount'列， 先计数再汇总
    print(df8.columns)
    df9 = df8.groupby(['continents'])[['confirmedCount', 'suspectedCount', 'curedCount', 'deadCount']].aggregate(['count', 'sum'])
    print(df9)
    # 32. 数据透视  在 Pandas 中，实现数据透视表是使用的 pivot_table() 这个方法 查看七大洲(continents)的确诊情况（currentConfirmedCount）（使用数据透视）
    df9 = pd.pivot_table(df8, index='continents', values='currentConfirmedCount', aggfunc='sum')
    print(df9)
    # 33. 上题是按照一维的方式进行拆分，和分组并没有实际上的区别，接下来我们看从二维的方向上对数据进行拆分  以国家（provinceName）为列
    # 大洲（continents）为索引，确诊情况（currentConfirmedCount）为值进行汇总
    df9 = pd.pivot_table(df8, index='continents', values='currentConfirmedCount', columns='provinceName', aggfunc='sum')
    print(df9)



# 数据分析实例
def fenxi():
    pass


def getX(x):
    if '万' in list(x):
        x = float(x.replace('万', ''))*10000
    else:
        x = float(x)
    return x


def getName(x):
    if x != '帅哥谭方盛':
        x = x.replace('帅哥', '')
    return x


if __name__ == '__main__':
    # clear()
    zhengli()
