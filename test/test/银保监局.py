import requests
from lxml import etree

page = 1
flag = 0
while True:
    url = f'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId=4113,pageIndex={page},pageSize=18.json'
    rows = requests.get(url)
    if rows.status_code == 404:
        url = f'http://www.cbirc.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild?itemId=4113&pageSize=18&pageIndex={page}'
        rows = requests.get(url)
    page += 1
    for row in rows.json()['data']['rows']:
        docId = row['docId']
        docSubtitle = row['docSubtitle']
        publishDate = row['publishDate']
        date = int(publishDate.split(" ")[0].replace("-",''))
        if date < 20210101:
            flag = 1
            break
        detail_url = f'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectByDocId/data_docId={docId}.json'
        res = requests.get(detail_url).json()['data']['docClob']
        html = etree.HTML(res)
        print(res)
        break
    if flag == 1:
        break
    break
