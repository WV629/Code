#-*- coding:utf-8 -*-
# TODO : http://search.news.cn/?lang=ru#search/0/%D0%A1%D0%B8%D0%BD%D1%8C%D1%86%D0%B7%D1%8F%D0%BD/1/
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
        for _ in range(10):
            try:
                res = requests.get(url,headers=self.headers,timeout=5)
                if res.status_code == 200:
                    return res
            except Exception as e:
                print('error----',e)
        else:
            print('vvvvvvv',url)
            return False

    def parse(self,url):
        results = self.get_res(url).json()['content']['results']
        # 获取新闻列表
        th = []
        for result in results:
            t = Thread(target=self.thread_parse,args=(result,))
            t.start()
            th.append(t)
        [t.join() for t in th]


    def thread_parse(self,result):
        list1 = {}
        list1['标题'] = re.sub('<.*?>', '', result['title']).replace('&nbsp;', ' ')
        list1['链接'] = result['url']
        try:
            detail_html = etree.HTML(self.get_res(list1['链接']).content.decode())
        except:
            list1['图片地址'] = ''
            list1['日期'] = ''
            list1['内容'] = ''
            list1['浏览量'] = ''
            datas.append(list1)
            return
        try:
            list1['图片地址'] = 'http://tpic.home.news.cn/xhCloudNewsPic/'+result['imgUrl'] if result['imgUrl'] else ''
        except:list1['图片地址'] = ''
        try:
            list1['日期'] = result['pubtime'].split(" ")[0]
        except:
            list1['日期'] = ''

        try:
            list1['内容'] = ''.join([i.strip() for i in detail_html.xpath("//div[@id='detailContent']/p//text()") if i.strip() != '']).strip()
            if list1['内容'] == '':
                list1['内容'] = ''.join([i.strip() for i in detail_html.xpath("//div[@id='content']/p//text()") if i.strip() != '']).strip()
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
    page = 11
    urls = [f'http://search.news.cn/getNews?keyword=%D0%A1%D0%B8%D0%BD%D1%8C%D1%86%D0%B7%D1%8F%D0%BD&curPage={i}&sortField=0&searchFields=1&lang=ru' for i in range(1,page+1)]
    th = []
    for url in urls:
    #     t = Thread(target=spider.parse,args=(url,))
    #     t.start()
    #     th.append(t)
    # [t.join() for t in th]
        print('url = ',url)
        spider.parse(url)
    print('save ---- ----')
    spider.save(datas,'file/5_search_news_cn')