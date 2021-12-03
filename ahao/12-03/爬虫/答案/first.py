from urllib import request
from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont
import re
import csv


def getInfo(html):
    soup = BeautifulSoup(html, 'html.parser')
    lis = soup.select('ul[class="all-img-list cf"]>li')
    for li in lis:
        title = li.select('div[class="book-mid-info"]>h2>a')[0].string
        print(title)
        author = li.select('p[class="author"]>a')[0].string
        print(author)
        classes = li.select('p[class="author"]>a')[1:3]
        index = []
        for i in classes:
            index.append(i.string)
        classes = '·'.join(index)
        print(classes)
        state = li.select('p[class="author"]>span')[0].string
        print(state)
        intro = list(li.select('p[class="intro"]')[0].stripped_strings)
        print(intro[0])
        # # {’&#100293;’: 8, ‘&#100295;’: 4, ‘&#100296;’: 3, ‘&#100297;’: 1, ‘&#100299;’: 2, ‘&#100300;’: 9, ‘&#100301;’: 5, ‘&#100302;’: 0, ‘&#100303;’: 6, ‘&#100304;’: 7}
        number = li.select('p[class="update"]>span>span')[0].string + '万字'
        print(number)
        f_csv.writerow([title, author, classes, state, intro[0], number])


def getHtml(url):
    res = request.Request(url, headers=headers)
    response = request.urlopen(res).read().decode('utf-8')
    woff = re.search("format\('eot'\); src: url\('(.+?)'\) format\('woff'\)", response, re.S)
    res = request.Request(woff.group(1), headers=headers)
    fontfile = request.urlopen(res).read()
    f = open('./font.woff', 'wb')
    f.write(fontfile)
    f.close()
    return response


def fontProc(text):
    font = TTFont('font.woff')
    camp = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
            'nine': 9, 'period': '.'}
    cp = {}
    for k, v in font.getBestCmap().items():
        try:  # 过滤无用的映射
            cp['&#' + str(k) + ';'] = camp[str(v)]
        except KeyError as e:
            pass
    for key in cp.keys():
        text = re.sub(key, str(cp[key]), text)
    return text


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4743.0 Safari/537.36'
    }
    woffDir = './font.woff'
    with open('起点免费书籍信息.csv', 'w', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(['书名', '作者', '分类', '状态', '介绍', '字数'])
        for i in range(1, 6):
            url = 'https://www.qidian.com/free/all/page{}/'.format(i)
            html = getHtml(url)
            html = fontProc(html)
            getInfo(html)
