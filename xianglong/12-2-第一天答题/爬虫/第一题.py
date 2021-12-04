import requests
from lxml import etree
import os


def response(url: str, headers) -> requests.models.Response:
    return requests.get(url, headers=headers)


def mkdir(mypath):
    path = os.path.join(os.getcwd(), mypath)
    if not os.path.exists(path):
        os.makedirs(path)
        print('目录已创建')

if __name__ == '__main__':
    url = 'https://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&wq=%E6%98%BE%E7%A4%BA%E5%99%A8&pvid=07b4173627c3479c9f067ce9794ba7a8 '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    myResponse = response(url, headers)
    html = etree.HTML(myResponse.text)
    lis = html.xpath('//li[@class="gl-item"]')
    mkdir('img')
    for i in lis:
        # print(etree.tostring(i.xpath('.//div[contains(@class, "p-img")]//img')[0], encoding='utf-8').decode('utf-8'))
        url = 'https:'+i.xpath('.//div[contains(@class, "p-img")]//img/@data-lazy-img')[0]
        data = response(url, headers)
        with open('./img/'+url.split('/')[-1], 'wb') as f:
            f.write(data.content)

