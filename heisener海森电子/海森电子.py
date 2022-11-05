import threading
import pandas as pd
import requests
from lxml import etree

# TODO : https://www.heisener.com/Products/Connectors-Interconnects/Card-Edge-Connectors-Edgeboard-Connectors/_Page_1
class Heisener(object):
    def get_response(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        for _ in range(5):
            try:
                res = requests.get(url,proxies=proxies,headers=headers)
                if res.status_code == 200:
                    return etree.HTML(res.content.decode())
                if res.status_code == 404:
                    return 404
            except Exception as e:
                print('error---',e)
        else:
            return False

    def parse(self,url):
        html = self.get_response(url)
        if html != False:
            trs = html.xpath("//tbody/tr")
            for tr in trs:
                list1 = {}
                list1['Part Number'] = tr.xpath("./td[2]//a/@title")[0]
                list1['Manufacturer'] = tr.xpath("./td[3]/div/text()")[0]
                list1['Description'] = tr.xpath("./td[4]/div/p/text()")[0]
                list1['Package'] = tr.xpath("./td[5]/div/text()")[0]
                list1['Stock'] = tr.xpath("./td[6]/div/span/text()")[0]
                print(list1)
                datas.append(list1)
        else:
            with open('log.txt', encoding='utf-8', mode='a') as f:
                f.write(url + '\n')


if __name__ == '__main__':
    datas = []
    proxies = {
        'http': '127.0.0.1:7890',
        'https': '127.0.0.1:7890',
    }
    heisener = Heisener()
    url = 'https://www.heisener.com/Products#Connectors-Interconnects'
    res = etree.HTML(requests.get(url,proxies=proxies).content.decode())
    lis = res.xpath("//h2[@id='Connectors-Interconnects']/following-sibling::div[1]/ul/li")
    hrefs = []
    i = 1
    for li in lis:
        href = 'https://www.heisener.com' + li.xpath("./a/@href")[0]
        num = int(li.xpath("./span/text()")[0][1:-1])
        if num < 10000:
            print(f'正在爬取第{i}个链接', href, num)
            i += 1
            page = num / 30
            pages = num // 30 + 1 if page > num // 30 else int(page)
            th = []
            for page_ in range(1,pages+1):
                url1 = '_'.join(href.split("_")[:-1])+'_'+str(page_)
                t = threading.Thread(target=heisener.parse,args=(url1,))
                t.start()
                th.append(t)
            [t.join() for t in th]
    print('保存------')
    df = pd.DataFrame(datas)
    df.to_excel("E:\Code\heisener海森电子产品1.xlsx",index=False)