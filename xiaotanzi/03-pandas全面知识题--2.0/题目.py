import pandas as pd
import matplotlib as plot
from matplotlib import pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
plot.rc('font', family='Microsoft YaHei')

# 知识点可在 https://note.youdao.com/s/6juL6I5Z 中查看（如果想自己百度也行）

# 第三答题——数据规整
def zhengli():
    pass
    # 注意！！！请结合效果图作答！！！

    # 1.设定索引 使用Series创建Series对象 并且设置索引为a, b, c, d
    # 2.设定索引 使用DataFrame创建DataFrame对象 并且设置索引
    # 3.修改第二题索引 改为1,2,3类型
    # 4.给索引命名  my_index
    # 5.分别使用DataFrame 原始方法，和loc与iloc三种方法取到舒祥龙的颜值
    # 6.修改列名 将姓名修改为名字，年龄修改为岁数
    # 7.添加一列 添加一列 出生年月日 '2003-08-20'
    # 8.查看数据类型
    # 9.查看数据形状
    # 10.查看数据大小
    # 11.查看数据详细信息
    # 12.修改数据类型 把岁数修改为float类型，把出生年月日修改为时间类型 再次查看数据类型
    # 13.更改数据内容 给名字前添加'帅哥'两字, 给名字后添加两个空格
    # 14.去除名字中的空值
    # 15.去除孙濠和舒祥龙前面的帅哥  保留帅哥谭方盛  切记！！！（这个是个知识点）
    # 16. 排序  索引排序  按照索引降序排序
    # 17. 按照岁数降序排序
    # 18. 先添加列’出生日‘，按照出生日降序排序

    # 19. 数据拼接 一对一 将本目录文件table_join_exp.xlsx的 Sheet1表，和Sheet2表，通过编号连接（注意：一个Excel文件中可有多个表）
    # 20. 数据拼接 一对多 当一个表的公共列是唯一的，另一个表的公共列则会有重复的数据， 取出table_join_exp.xlsx 的Sheet3 合并 Sheet1
    # 21. 根据上题 修改分数_x, 分数_y 的格式为分数_one,分数_two  在merge中添加参数解决
    # 22. 多对多 取出Sheet4 与 Sheet3合并
    # 23. 连接方式 内连接  内连接就是取两个表中公共的部分  内连接 Sheet5 和 Sheet3
    # 24. 连接方式 左连接  左连接就是已左表为基础，右表像左表上拼数据  左连接  Sheet5 和 Sheet3
    # 25. 连接方式 右连接   sheet5, sheet3
    # 26. 外连接 外连接就是两个表的并集 sheet5  sheet3
    # 27. 纵向拼接  拼接 Sheet5  Sheet6  并且用参数重置索引

    # 28. 数据分组  导入需要操作的数据   epidemic_dxy.xlsx   以continents进行分组  查看七大洲的数据条数
    # 29. 数据分组以continents进行分组  查看七大洲疫情的汇总
    # 30. 以continents provinceName进行分组  并汇总
    # 31. 如果我们想在一次分组中，进行两次汇总运算，aggregate()  以continents分组 取'confirmedCount', 'suspectedCount',
    # 'curedCount', 'deadCount'列， 先计数再汇总

    # 32. 数据透视  在 Pandas 中，实现数据透视表是使用的 pivot_table() 这个方法 查看七大洲(continents)的确诊情况（currentConfirmedCount）（使用数据透视）
    # 33. 上题是按照一维的方式进行拆分，和分组并没有实际上的区别，接下来我们看从二维的方向上对数据进行拆分  以国家（provinceName）为列
    # 大洲（continents）为索引，确诊情况（currentConfirmedCount）为值进行汇总


if __name__ == '__main__':
    zhengli()
