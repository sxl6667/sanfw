from urllib import request
from bs4 import BeautifulSoup
import os


def getUrl(url):
    res = request.Request(url, headers=headers)
    response = request.urlopen(res).read().decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    lis = soup.select('ul[class="all-img-list cf"]>li')
    for li in lis[:1]:
        next_url = li.select('div[class="book-mid-info"]>h2>a')[0]['href']
        next_url = 'https:' + next_url
        getInfo(next_url)


def getInfo(next_url):
    res = request.Request(next_url, headers=headers)
    response = request.urlopen(res).read().decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.select('div.book-info>h1>em')[0].string
    print(title)
    chapters = soup.select('div.volume-wrap>div.volume')
    for chapter in chapters:
        chapter_name = list(chapter.select('h3')[0].stripped_strings)
        chapter_name = ''.join(chapter_name)
        print(chapter_name)
        lis = chapter.select('ul.cf>li')
        for li in lis:
            title_name = li.select('h2.book_name>a')[0].string
            print(title_name)
            title_url = li.select('h2.book_name>a')[0]['href']
            title_url = 'https:' + title_url
            context = getText(title_url)
            save(title, chapter_name, title_name, context)


def getText(title_url):
    res = request.Request(title_url, headers=headers)
    response = request.urlopen(res).read().decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    context = list(soup.select('div[class="read-content j_readContent"]')[0].strings)
    context = '\n'.join(context).strip()
    context = '   ' + context
    print(context)
    return context


def save(title, chapter_name, title_name, context):
    path = './{0}/{1}'.format(title, chapter_name)
    if not os.path.exists(path):
        os.makedirs(path)
    path = './{0}/{1}/{2}.txt'.format(title, chapter_name, title_name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(context)
        f.close()


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4743.0 Safari/537.36'
    }
    for i in range(1, 2):
        url = 'https://www.qidian.com/free/all/page{}/'.format(i)
        getUrl(url)
