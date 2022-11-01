# TODO : http://ggzyjy.sc.gov.cn/cxgl/sincerity-creditinfo.html
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


def parse(item):
    list1 = {}
    list1['法人名称'] = item['legal_name']
    list1['组织机构代码'] = item['legal_code']
    list1['法人角色'] = item['legal_role']
    list1['入库时间'] = item['operatedate']
    list1['资源来源名称'] = item['r_pfcode']
    rowguid = item['rowguid']
    href = 'http://ggzyjy.sc.gov.cn/WebBuilder/rest/credit/getDetail'
    data = {'rowguid': rowguid}
    res = requests.post(href, data=data, headers=headers).json()['creditinfo']
    list1['联系人'] = res['legal_represent']
    list1['联系电话'] = res['legal_contact_phone']
    datas.append(list1)
    print(list1)

def run():
    for i in range(10):
        url = 'http://ggzyjy.sc.gov.cn/WebBuilder/rest/credit/getList'
        data = {
            'type': '00',
            'pageSize': 12000,
            'index': i,
        }
        items = requests.post(url,data=data,headers=headers).json()['creditinfo']
        print(len(items))
        if len(items) == 0:
            break
        with ThreadPoolExecutor() as pool:
            pool.map(parse, items)

if __name__ == '__main__':
    datas = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    run()
    df = pd.DataFrame(datas)
    df.to_excel("ggzyjy.xlsx",index = False)