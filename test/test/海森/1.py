import math
import random
import threading
import pandas as pd
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor

# TODO : https://www.heisener.com/Products/Connectors-Interconnects/Card-Edge-Connectors-Edgeboard-Connectors/_Page_1
class Heisener(object):
    def get_response(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        for _ in range(10):
            try:
                res = requests.get(url,proxies=proxies,headers=headers,timeout=20)
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
    PROXY_LIST = [
        "http://104.223.212.104:65432",
        "http://104.223.212.106:65432",
        "http://104.223.212.110:65432",
        "http://104.223.212.112:65432",
        "http://104.223.212.114:65432",
        "http://104.223.212.116:65432",
        "http://104.223.212.12:65432",
        "http://104.223.212.123:65432",
        "http://104.223.212.125:65432",
        "http://104.223.212.127:65432",
        "http://104.223.212.129:65432",
        "http://104.223.212.131:65432",
        "http://104.223.212.133:65432",
        "http://104.223.212.136:65432",
        "http://104.223.212.138:65432",
        "http://104.223.212.14:65432",
        "http://104.223.212.142:65432",
        "http://104.223.212.144:65432",
        "http://104.223.212.146:65432",
        "http://104.223.212.148:65432",
        "http://104.223.212.155:65432",
        "http://104.223.212.157:65432",
        "http://104.223.212.159:65432",
        "http://104.223.212.16:65432",
        "http://104.223.212.161:65432",
        "http://104.223.212.163:65432",
        "http://104.223.212.165:65432",
        "http://104.223.212.168:65432",
        "http://104.223.212.170:65432",
        "http://104.223.212.172:65432",
        "http://104.223.212.174:65432",
        "http://104.223.212.176:65432",
        "http://104.223.212.178:65432",
        "http://104.223.212.18:65432",
        "http://104.223.212.180:65432",
        "http://104.223.212.185:65432",
        "http://104.223.212.187:65432",
        "http://104.223.212.189:65432",
        "http://104.223.212.191:65432",
        "http://104.223.212.193:65432",
        "http://104.223.212.195:65432",
        "http://104.223.212.197:65432",
        "http://104.223.212.2:65432",
        "http://104.223.212.20:65432",
        "http://104.223.212.200:65432",
        "http://104.223.212.202:65432",
        "http://104.223.212.204:65432",
        "http://104.223.212.206:65432",
        "http://104.223.212.208:65432",
        "http://104.223.212.210:65432",
        "http://104.223.212.212:65432",
        "http://104.223.212.219:65432",
        "http://104.223.212.221:65432",
        "http://104.223.212.223:65432",
        "http://104.223.212.225:65432",
        "http://104.223.212.227:65432",
        "http://104.223.212.232:65432",
        "http://104.223.212.234:65432",
        "http://104.223.212.236:65432",
        "http://104.223.212.238:65432",
        "http://104.223.212.240:65432",
        "http://104.223.212.242:65432",
        "http://104.223.212.244:65432",
        "http://104.223.212.251:65432",
        "http://104.223.212.253:65432",
        "http://104.223.212.27:65432",
        "http://104.223.212.29:65432",
        "http://104.223.212.3:65432",
        "http://104.223.212.31:65432",
        "http://104.223.212.33:65432",
        "http://104.223.212.35:65432",
        "http://104.223.212.37:65432",
        "http://104.223.212.40:65432",
        "http://104.223.212.42:65432",
        "http://104.223.212.44:65432",
        "http://104.223.212.46:65432",
        "http://104.223.212.48:65432",
        "http://104.223.212.5:65432",
        "http://104.223.212.50:65432",
        "http://104.223.212.52:65432",
        "http://104.223.212.59:65432",
        "http://104.223.212.61:65432",
        "http://104.223.212.63:65432",
        "http://104.223.212.65:65432",
        "http://104.223.212.67:65432",
        "http://104.223.212.69:65432",
        "http://104.223.212.72:65432",
        "http://104.223.212.74:65432",
        "http://104.223.212.76:65432",
        "http://104.223.212.78:65432",
        "http://104.223.212.80:65432",
        "http://104.223.212.82:65432",
        "http://104.223.212.84:65432",
        "http://104.223.212.91:65432",
        "http://104.223.212.93:65432",
        "http://104.223.212.95:65432",
        "http://104.223.212.97:65432",
        "http://104.223.212.99:65432",
    ]
    heisener = Heisener()
    # names = ['5-Capacitors','6-Resistors','7-Potentiometers-Variable-Resistors','8-Inductors-Coils-Chokes']
    # for name in names:
    datas = []
    pr = random.choice(PROXY_LIST)
    proxies = {
        'http': pr,
        'https': pr,
    }
    # url = 'https://www.heisener.com/Products#Connectors-Interconnects'
    # res = heisener.get_response(url)
    # lis = res.xpath(f"//h2[@id='{name[2:]}']/following-sibling::div[1]/ul/li")
    # hrefs = []
    i = 1
    hrefs = ['https://www.heisener.com/Products/Resistors/Through-Hole-Resistors/_Page_1']
    nums = [51000]
    for href,num in zip(hrefs,nums):
        # href = 'https://www.heisener.com' + li.xpath("./a/@href")[0]
        # num = int(li.xpath("./span/text()")[0][1:-1])
        # if num < 10000:
        #     if sum > 10000:
        #         print(sum)
        #         break
        #     sum += num
        print(f'正在爬取第{i}个链接', href, num)
        i += 1
        page = num / 30
        pages = num // 30 + 1 if page > num // 30 else int(page)
        # pages = math.floor(10000 / 30) + 10
        th = []
        urls = []
        for page_ in range(1,pages+1):
            url1 = '_'.join(href.split("_")[:-1])+'_'+str(page_)
            print(url1)
            urls.append(url1)
        with ThreadPoolExecutor(max_workers=1000) as pool:
            pool.map(heisener.parse,urls)
            #     t = threading.Thread(target=heisener.parse,args=(url1,))
            #     t.start()
            #     th.append(t)
            # [t.join() for t in th]
    print('保存------',sum(nums),'-------',len(datas))
    df = pd.DataFrame(datas)
    df.to_excel(f"6-Resistors-10000.xlsx",index=False)