import matplotlib.pyplot as plt
import matplotlib as plot
import numpy as np

plot.rc('font', family='Microsoft YaHei')


# 知识点可在 https://note.youdao.com/s/6juL6I5Z 中查看（如果想自己百度也行）（文件--pandas数据可视化）
# 可以先看看文档再做题


# 第一题
def Pie():
    labels = ['孙濠', '小坛子', '谭方盛', '舒祥龙']
    sizes = [14.55, 30.45, 45, 10]
    """
    设置图片大小为 7*6，dpi=200(决定图片像素，值越高，像素越大), 设置饼图的四种颜色为red, 
    yellow, lightskyblue, green, 把舒祥龙的颜值比例突出（效果可看效果图），设置图名为 颜值比例，
    比例百分比保留两位小数。总体来说与效果大致相同。
    """


# 第二题
def Huan():
    labels = ['孙濠', '小坛子', '谭方盛', '舒祥龙']
    sizes = [14.55, 30.45, 45, 10]
    """
    画一张环形图 和上题相似 多了一个参数 wedgeprops = {'width': 数值, 'edgecolor': 边框颜色}
    width是数值，含义是保留原来的百分之多少，如果填1，那么它就是饼图，一般填小于1的值，edgecolor设置边框颜色
    """


# 第三题
def Bar():
    label_list = ['2015', '2016', '2017', '2018']
    data_y1 = [20, 30, 40, 55]
    # 使用ggplot风格画图
    plt.style.use('ggplot')
    """
    画一个柱状图，图片总大小为8*5，柱子宽设置为（默认0.8）0.4, 柱子的边框色设置为 
    天空蓝（lightskyblue）, 边框宽度设置为2（lw=2），柱子填充色设置为#f40
    设置它的y轴限制为65
    设置它的x标签为 2015年 ...  2018年
    """
    plt.figure(figsize=(8, 5), dpi=200)


# 第四题
def Bar2():
    label_list = ['2015', '2016', '2017', '2018']
    data_y1 = [20, 30, 40, 55]
    data_y2 = [20, 25, 24, 19]
    # 使用ggplot风格画图
    plt.style.use('ggplot')
    """
    画堆叠柱状图
    和上题相似，看效果图实现
    注意，bottom参数是设置柱子与 x 轴的距离
    """
    plt.figure(figsize=(8, 5), dpi=200)


# 第五题
def Bar3():
    data_x = np.arange(2015, 2019)
    data_y1 = [20, 30, 40, 55]
    data_y2 = [20, 25, 24, 19]
    # 使用ggplot风格画图
    plt.style.use('ggplot')
    """
    并排柱状图
    和上题相似，看效果图实现
    注意，需要调整柱子的位置，第二个柱子的位置右偏移第一个柱子的宽度
    还需要在顶部标上值，提示 ：用到plt.text()具体位置需要计算
    """
    plt.figure(figsize=(8, 5), dpi=200)


# 第六题
def Hist():
    data = np.random.normal(loc=100, scale=20, size=100)
    plt.figure(figsize=(8, 5), dpi=200)
    plt.style.use('ggplot')
    """
    根据效果图实现，其中填充色为green, 透明度为0.6
    """


# 第七题
def Scatter():
    plt.figure(figsize=(10, 4), dpi=200)
    np.random.seed(1)
    a = 10 * np.random.randn(100)
    b = 10 * np.random.randn(100)
    """
    最简单的一道题，看图吧
    """


# 第八题 压轴题，个人感觉用到的东西比较多 百度不到的话就等着看答案（实话实说有点难百度）
def Line():
    app = [78, 80, 79, 81, 91, 95, 96]
    ban = [70, 80, 81, 82, 75, 90, 89]
    data_x = np.arange(0, 7)
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111)  # 创建画板，也可以不创，看自己
    """
    看效果画图
    """


if __name__ == '__main__':
    Pie()
