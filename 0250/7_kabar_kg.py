#-*- coding:utf-8 -*-
# TODO : https://kabar.kg/search/?q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9
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
        for _ in range(5):
            try:
                res = requests.get(url,headers=self.headers,proxies = self.proxeis,timeout=5)
                if res.status_code == 200:
                    return etree.HTML(res.content.decode())
            except Exception as e:
                print('error----',e)
        else:
            return False

    def parse(self,url):
        html = self.get_res(url)
        # 获取新闻列表
        divs = html.xpath("//div[@class='search-context']/article")
        th = []
        for div in divs:
            t = Thread(target=self.thread_parse,args=(div,))
            t.start()
            th.append(t)
        [t.join() for t in th]


    def thread_parse(self,div):
        list1 = {}
        list1['链接'] = urljoin(url,div.xpath(".//h3/a/@href")[0])
        detail_html = self.get_res(list1['链接'])
        list1['标题'] = detail_html.xpath(".//header[@class='post-header']/h1/text()")[0].strip()
        try:
            list1['日期'] = detail_html.xpath("//span[@class='article-date']/text()")[1].strip().split(" ")[0].split("/")
            list1['日期'] = '20'+list1['日期'][2] + '-' + list1['日期'][1].zfill(2) + '-' + list1['日期'][0].zfill(2)
        except:
            list1['日期'] = ''
        try:
            list1['内容'] = ''.join([i.strip() for i in detail_html.xpath("//div[@class='post-content clearfix']/p//text()") if i.strip() != '']).strip()
            list1['内容'] = re.sub('\s+',' ',list1['内容'])
        except:
            list1['内容'] = ''
        try:
            list1['浏览量'] = ''.join(detail_html.xpath("//h1/following-sibling::div/span[@class='views']/text()")).strip()
        except:
            list1['浏览量'] = ''
        try:
            list1['图片地址'] = urljoin(url,''.join(detail_html.xpath(".//div[@class='post-content clearfix']//img/@src")))
        except:
            list1['图片地址'] = ''
        print(list1)
        datas.append(list1)

    def save(self,datas,name):
        df = pd.DataFrame(datas)
        df.to_excel(f"{name}.xlsx",index=False)

if __name__ == '__main__':
    datas = []
    print('start ---- ----')
    spider = Spider()
    url = 'https://kabar.kg/search/?q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9'
    spider.parse(url)
    print('save ---- ----')
    spider.save(datas,'file/7_kabar_kg')