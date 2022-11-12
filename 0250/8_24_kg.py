#-*- coding:utf-8 -*-
# TODO : https://24.kg/poisk_po_sajtu/page_1/?SearchForm%5Btext%5D=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9&per-page=30
import re
import requests
from urllib.parse import urljoin
from threading import Thread
from lxml import etree
import pandas as pd


class Spider(object):
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
        self.proxeis = {
            'http':'127.0.0.1:7890',
            'https':'127.0.0.1:7890',
        }

    def get_res(self,url):
        for _ in range(10):
            try:
                res = requests.get(url,headers=self.headers,proxies = self.proxeis,timeout=10)
                if res.status_code == 200:
                    return etree.HTML(res.content.decode())
            except Exception as e:
                print('error----',e)
        else:
            return False

    def parse(self,url):
        html = self.get_res(url)
        # 获取新闻列表
        divs = html.xpath("//div[@class='one']")
        th = []
        for div in divs:
            t = Thread(target=self.thread_parse,args=(div,))
            t.start()
            th.append(t)
        [t.join() for t in th]


    def thread_parse(self,div):
        list1 = {}
        list1['标题'] = div.xpath(".//div[@class='title']/a[1]/span/text() | .//div[@class='title']/a[1]/strong/text()")[0].strip()
        list1['链接'] = urljoin(url,div.xpath(".//div[@class='title']/a[1]/@href")[0])
        try:
            list1['图片地址'] = ''.join(div.xpath(".//img/@src"))
        except:
            list1['图片地址'] = ''
        detail_html = self.get_res(list1['链接'])
        try:
            list1['日期'] = detail_html.xpath("//span[@itemprop='datePublished']/@content")[0].strip().replace('\\','')
        except:
            list1['日期'] = ''
        try:
            list1['内容'] = ''.join([i.strip() for i in detail_html.xpath("//div[@class='cont']//p//text()") if i.strip() != '']).strip()
            list1['内容'] = re.sub('\s+',' ',list1['内容'])
        except:
            list1['内容'] = ''
        try:
            list1['浏览量'] = ''.join(detail_html.xpath("//h1/following-sibling::div/span[@class='views']/text()")).strip()
        except:
            list1['浏览量'] = ''

        print(list1)
        datas.append(list1)

    def save(self,datas,name):
        df = pd.DataFrame(datas)
        df.to_excel(f"{name}.xlsx",index=False)

if __name__ == '__main__':
    datas = []
    print('start ---- ----')
    spider = Spider()
    page = 60
    urls = [f'https://24.kg/poisk_po_sajtu/page_{i}/?SearchForm%5Btext%5D=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9&per-page=30' for i in range(1,page+1)]
    th = []
    for url in urls:
    #     t = Thread(target=spider.parse,args=(url,))
    #     t.start()
    #     th.append(t)
    # [t.join() for t in th]
        print('url = ',url)
        spider.parse(url)
    print('save ---- ----')
    spider.save(datas,'file/8_24_kg')