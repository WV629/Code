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

    def get_res(self,url):
        for _ in range(10):
            try:
                res = requests.get(url,headers=self.headers,timeout=10,proxies = self.proxeis)
                if res.status_code == 200:
                    return res
            except Exception as e:
                print('error----',e)
        else:
            print('vvvvvvv',url)
            return False

    def parse(self,url):
        results = self.get_res(url).json()['data']
        # 获取新闻列表
        th = []
        for result in results:
            t = Thread(target=self.thread_parse,args=(result,))
            t.start()
            th.append(t)
        [t.join() for t in th]


    def thread_parse(self,result):
        list1 = {}
        list1['标题'] = result['title']
        list1['链接'] = 'https://uza.uz/ru/posts/'+result['slug']
        try:
            list1['图片地址'] = 'https://cdn.uza.uz/'+result['files']['folder'] + '/'+result['files']['file']
        except:list1['图片地址'] = ''
        try:
            list1['日期'] = result['publish_time'].split(" ")[0]
        except:
            list1['日期'] = ''

        try:
            list1['内容'] = re.sub('\s+','',re.sub('<.*?>','',result['content']).replace('&nbsp;','').replace('\r\n','')).strip()
        except:
            list1['内容'] = ''
        try:
            list1['浏览量'] = result['viewed']
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
    page = 50
    urls = [f'https://api.uza.uz/api/v1/posts/search?page={i}&per_page=21&q=%D0%BA%D0%B8%D1%82%D0%B0%D0%B9&_f=json&_l=ru' for i in range(1,page+1)]
    th = []
    for url in urls:
        t = Thread(target=spider.parse,args=(url,))
        t.start()
        th.append(t)
    [t.join() for t in th]
        # print('url = ',url)
        # spider.parse(url)
    print('save ---- ----')
    spider.save(datas,'file/4_api_uza_uz')