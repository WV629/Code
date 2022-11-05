#-*- coding:utf-8 -*-
# TODO : https://uza.uz/ru/search?q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9
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
        self.dict = {
            'Сентября':'09',
            'Октября':'10',
            'Августа':'08',
            'Июня':'06',
            'Июля':'07',
            'Мая':'05',
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
        divs = html.xpath("//div[@class='news-list__col news-list__col_main']/article")
        th = []
        for div in divs:
            t = Thread(target=self.thread_parse,args=(div,))
            t.start()
            th.append(t)
        [t.join() for t in th]


    def thread_parse(self,div):
        list1 = {}
        list1['标题'] = div.xpath(".//h3/text()")[0].strip()
        list1['链接'] = urljoin(url,div.xpath(".//a[@class='anounce-news__link']/@href")[0])
        detail_html = self.get_res(list1['链接'])
        try:
            list1['日期'] = detail_html.xpath("//div[@class='time_article_bl']/text()")[0].strip().split(",")[0].split(" ")
            list1['日期'] = list1['日期'][2] + '-' + self.dict[list1['日期'][1]] + '-' + list1['日期'][0]
        except:
            list1['日期'] = ''

        try:
            list1['内容'] = ''.join([i.strip() for i in detail_html.xpath("//div[@class='body_article_bl']//text()") if i.strip() != '' and 'unction' not in i and '{' not in i]).strip()
            list1['内容'] = re.sub('\s+',' ',list1['内容'])
        except:
            list1['内容'] = ''
        try:
            list1['浏览量'] = ''.join(detail_html.xpath("//h1/following-sibling::div/span[@class='views']/text()")).strip()
        except:
            list1['浏览量'] = ''
        try:
            list1['图片地址'] = ''.join(detail_html.xpath("//div[@class='main_img_article']/img/@src"))
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
    page = 4
    urls = [f'https://www.inform.kz/ru/search/{i}?sword=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9' for i in range(1,page+1)]
    th = []
    for url in urls:
    #     t = Thread(target=spider.parse,args=(url,))
    #     t.start()
    #     th.append(t)
    # [t.join() for t in th]
        print('url = ',url)
        spider.parse(url)
    print('save ---- ----')
    spider.save(datas,'inform_kz')