import requests
import re
import time

url = 'https://search.jd.com/Search?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4738.0 Safari/537.36'
}
pageCount = 10
for page in range(1, pageCount+1):
    params = {
        'keyword': '显示器',
        'enc': 'utf-8',
        'wq': '显示器',
        'pvid': '798c132d68e942439372320b7ffcc568',
        'page': page,
        's': 56
    }
    res = requests.get(url, params=params, headers=headers)
    li = r'<ul class="gl-warp clearfix" data-tpl="1">(.*?)</ul>'
    lis = re.findall(li, res.text, re.S)[0]
    img = r'<img width=".*?" height=".*?" data-img=".*?" data-lazy-img="(.*?)" />'
    imgs = re.findall(img, lis)
    for img in imgs:
        img = 'https:' + img
        res = requests.get(img, headers=headers)
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        path = 'image/' + now + '.png'
        time.sleep(1)
        print(path)
        with open(path, 'wb') as f:
            f.write(res.content)
            f.close()

