import csv
from lxml import etree
import json
import os
import requests
import tqdm


# 转化json数据
def data(s: str) -> dict:
    return json.loads(s)


# 发送get请求
def get_data(url: str, **kwargs):
    return requests.get(url, params='params' in kwargs.keys() and kwargs['params'] or None,
                        headers='headers' in kwargs.keys() and kwargs['headers'] or None)


# 获得html对象
def get_html(s: str):
    return etree.HTML(s)


# 主页解析
def main_parse(html):
    for i in html.xpath('//ul[contains(@class, "gl-warp clearfix")]/li'):
        yield i


# 商品页面解析
def goods_parse(html):
    info = [li.text for li in html.xpath('//ul[contains(@class, "parameter2 p-parameter-list")]/li')]
    name = info[0].split('：')[-1]
    return name, info[1:]


# 获取价格
def get_price(s: str):
    return data(s[12:-1])['price']['p']


# 保存图片
def save_img(li):
    url = 'https:' + li.xpath('.//div[contains(@class, "p-img")]//img/@data-lazy-img')[0]
    with open('./img/' + url.split('/')[-1], 'wb') as f:
        f.write(get_data(url).content)


if __name__ == '__main__':
    # 定义需要用到的url以及header
    url = 'https://search.jd.com/Search?keyword=%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&wq=%E6%98%BE%E7%A4%BA%E5%99%A8&pvid=07b4173627c3479c9f067ce9794ba7a8 '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    price_url = 'https://item-soa.jd.com/getWareBusiness'
    params = {
        'callback': 'jQuery16184',
         'skuId': '100012087833',
         'area': '18_1482_48937_0'}
    # 获取主页
    html = get_html(get_data(url, headers=headers).text)
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['商品标题', '商品价格', '商品信息'])
        for i in tqdm.tqdm(main_parse(html)):
            try:
                goods_url = 'https:' + i.xpath('.//div[contains(@class, "p-img")]/a/@href')[0]
            # save_img(i)
                goods_title, goods_info = goods_parse(get_html(get_data(goods_url, headers=headers).text))
                params['skuId'] = goods_url.split('/')[-1].split('.')[0]
                goods_price = get_price(get_data(price_url, headers=headers, params=params).text)
            except:
                pass
            else:
                writer.writerow([goods_title, goods_price, goods_info])
            pass