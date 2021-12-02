import requests
from lxml import etree
import re
import csv


def geturl():
    url = 'https://search.jd.com/Search?'
    params = {
        'keyword': '显示器',
        'enc': 'utf-8',
        'page': page,
        's': 56
    }
    res = requests.get(url, params=params, headers=headers)
    html = etree.HTML(res.text)
    lis = html.xpath('//ul[@class="gl-warp clearfix"]/li')
    for li in lis:
        price = li.xpath('.//div[@class="p-price"]/strong/i/text()')[0] + '元'
        next_url = li.xpath('.//div[@class="p-name p-name-type-2"]/a/@href')[0]
        next_url = "https:" + next_url
        title, content = getinfo(next_url)
        print([title, price, content])
        f_csv.writerow([title, price, content])


def getinfo(next_url):
    res = requests.get(next_url, headers=headers)
    judge = re.search("<script>window.location.href='.*?'</script>", res.text)
    while judge:
        res = requests.get(next_url, headers=headers)
        judge = re.search("<script>window.location.href='.*?'</script>", res.text)
        print('页面被拦截，重新访问')
    html = etree.HTML(res.text)
    lis = html.xpath('//ul[@class="parameter2 p-parameter-list"]/li')
    title = lis[0].xpath('.//text()')[0].replace('商品名称：', '')
    content = ''
    for li in lis[1:]:
        index = li.xpath('.//text()')
        index = ''.join(index).replace('：', ':')
        content = content + index + ';'
    return title, content


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4738.0 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'cookie': '__jdu=1771575836; areaId=18; ipLoc-djd=18-1482-48937-0; PCSYCityID=CN_430000_430100_430111; unpl=V2_ZzNtbUQDExclDkcHeU5aUmIKRw0SB0ETfVoSBnIbVAM3UUYOclRCFnUURlRnG10UZwcZWUtcQBNFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfWgVjBRZUQFBzJXI4dmRzGlsDYjMTbUNnAUEpCk5ReBxeSGcFFF1GUUccdw92VUsa; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_7ea3a70b3f7f48daaa379cec8397aceb|1638259108106; shshshfpa=94ab5b15-84b0-bd48-c44c-8f0898b2246b-1638259110; shshshfpb=j5GwHU5mGnz%2Fqf0YEltC5mQ%3D%3D; shshshfp=4b3915161657ea4ed7a19731b039559a; __jdc=122270672; rkv=1.0; qrsc=3; __jda=122270672.1771575836.1638175080.1638259108.1638270321.3; pinId=vzuBYexX3W2HIgF6wc4tw7V9-x-f3wj7; pin=jd_562e28b7ef515; unick=jd_562e28b7ef515; _tp=x6r0FR4hzJmL4bsJ5pS112KXeopU34v305OkPcGbHfE%3D; _pst=jd_562e28b7ef515; token=ed75b139d10c216136c103999e4148cf,3,910151; __tk=7aade5d0ec49c32b5a1b6cf8d16689b8,3,910151; wlfstk_smdl=jcw6h8269i5biaoyy09so54hwwoq1lwk; TrackID=1azryWuL7lBIcD2GXmTStSUfx2_YSFggbFZkZ-sHfUkFofa2hsPNRwjRQdTQKcVU7xjnHXJJB--1YYM2smY_zApkhjvIM60wBbeZwEtTewoI; thor=32A3A520B8F7F5D6C4CC8BECFB14213A6C72D3629D01AE3C4AE6CC236E8F01BDFA76169F91041209967A1FE0562648E7E99D0C72DBDD4E606510071B4AF3B60BFA09628DCF68E9BB8D5510C1BED5E0FA1CFDAE09FE2B7E506EC6ADB6256332141FB2CDF3D6DF7FFF2532F3A12C1B9A2B7332C0BDCC60B0363074B3DE4DC3C881264DAE9E2EC3955FE63188DF5E81A771049D200541AD1570D40275D055E55AF1; ceshi3.com=103; __jdb=122270672.27.1771575836|3.1638270321; shshshsID=b2abf955cc8f0f8024782f30401fc3cb_13_1638273752750; 3AB9D23F7A4B3C9B=CLQIMOAMVRHU4VKVXZ7VKEK6FGJ6AWGFQUYTJ5OOVD2TLSOPVTATTB23AZ2455S5ZYNDZOU4HIOISJQGN5JVS7257I',
        'accept-language': 'zh-CN,zh;q=0.9'
    }
    with open('jd.csv', 'w', encoding='utf-8', newline='') as f:
        f_csv = csv.writer(f, dialect='excel')
        top = ['商品名称', '价格', '简介']
        f_csv.writerow(top)
        pageCount = 10
        for page in range(1, pageCount + 1):
            geturl()