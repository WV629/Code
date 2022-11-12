import re
import pandas as pd
import requests
from lxml import etree



def parse(table):
    list1 = {}
    list1['链接'] = f'http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId={docId}&itemId={temId}'
    list1['标题'] = re.sub('\s+',' ',docSubtitle)
    list1['发布日期'] = publishDate.split(" ")[0]
    list1['行政处罚决定书文号'] = ''.join(table.xpath(".//*[contains(text(),'决定书文号')]/ancestor::tr/td[2]//text()")).strip()
    list1['被处罚单位名称'] = ''.join(table.xpath(".//*[text() = '名称']/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['被处罚单位法定代表人姓名'] = ''.join(table.xpath(".//*[contains(text() , '法定代表人')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['被处罚当事人'] = ''.join(table.xpath(".//*[contains(text() , '个人姓名')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    if list1['被处罚单位法定代表人姓名'] == '' and list1['被处罚当事人'] == '':
        list1['被处罚当事人'] = ''.join(table.xpath(".//*[contains(text() , '被处罚当事')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['主要违法违规事实'] = ' '.join(
        table.xpath(".//*[contains(text() , '主要违法')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['行政处罚依据'] = ''.join(
        table.xpath(".//*[contains(text() , '行政处罚依据')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['行政处罚决定'] = ''.join(
        table.xpath(".//*[contains(text() , '行政处罚决定')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['作出处罚决定的机关名称'] = ''.join(
        table.xpath(".//*[contains(text() , '机关名称')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    list1['作出处罚决定的日期'] = ''.join(
        table.xpath(".//*[contains(text() , '的日期')]/ancestor::td/following-sibling::td[1]/p/span//text()")).strip()
    print(list1)
    print("*" * 50)
    datas.append(list1)


def main(url):
    try:
        res = requests.get(url).json()['data']['docClob']
    except:
        try:
            res = requests.get(url).json()['data']['docClob']
        except:
            with open('log.txt','a',encoding='utf-8')as f:
                f.write(url+'\n')
                return
    html = etree.HTML(res)
    tables = html.xpath("//table[@class='MsoNormalTable']")
    if len(tables) == 1:
        parse(tables[0])
    elif len(tables) >= 1:
        for table in tables:
            parse(table)
    else:
        parse1(html)

# def parse1(html):
#     list1 = {}
#     list1['链接'] = f'http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId={docId}&itemId={temId}'
#     list1['标题'] = docSubtitle
#     list1['发布日期'] = publishDate.split(" ")[0]
#     ps = html.xpath("//div[@class='Section0']/p")
#     content = []
#     for p in ps:
#         text = re.sub('\s','',''.join(p.xpath(".//text()"))).strip()
#         if text != '':
#             content.append(text)
#     content = '\n'.join(content)
#     list1['内容'] = content
#     datas.append(list1)

def parse1(html):
    list1 = {}
    list1['链接'] = f'http://www.cbirc.gov.cn/cn/view/pages/ItemDetail.html?docId={docId}&itemId={temId}'
    list1['标题'] = re.sub('\s+',' ',docSubtitle)
    list1['发布日期'] = publishDate.split(" ")[0]
    try:
        list1['行政处罚决定书文号'] = re.search('（(.*?)）',docSubtitle).group()
    except:
        list1['行政处罚决定书文号'] = ''
    ps = html.xpath("//div[contains(@class,'Section')]/p")
    contents = []
    for p in ps:
        text = re.sub('\s','',''.join(p.xpath(".//text()"))).strip()
        if text != '':
            contents.append(text)
    content = '\n'.join(contents)
    try:
        list1['被处罚单位名称'] = re.search('当事人：(.*)',content).group(1)
    except:
        list1['被处罚单位名称'] = ''
    try:
        list1['被处罚单位法定代表人姓名'] = re.search('法定代表人：(.*)',content).group(1)
    except:list1['被处罚单位法定代表人姓名'] =''
    try:
        list1['被处罚当事人'] = ';'.join(re.findall('当事人：(.*)',content)[1:])
    except:list1['被处罚当事人'] = ''
    try:
        list1['主要违法违规事实'] = re.sub('\s',' ',re.search('违法行为：(.*?)综上，',content,re.S).group(1).strip())
    except:
        try:
            list1['主要违法违规事实'] = re.sub('\s', ' ', re.search('违法行为：(.*?)上述，', content, re.S).group(1).strip())
        except:list1['主要违法违规事实'] = ''
    try:
        list1['行政处罚依据'] = ';'.join(re.findall('违反了?(.*?)的?规定',content)).strip()
    except:list1['行政处罚依据'] =''
    try:
        list1['行政处罚决定'] = ''.join(re.findall('上述.*?违反.*?根据.*?，(.*)',content)).strip()
    except:list1['行政处罚决定'] =''
    list1['作出处罚决定的机关名称'] = ''.join(html.xpath("//div[@class='Section0']/p[last()-2]/text()"))
    try:
        list1['作出处罚决定的日期'] = contents[-1]
    except:
        list1['作出处罚决定的机关名称'] = ''.join(html.xpath("//div[@class='Section0']/p[last()-1]/text()"))

    print(list1)
    # list1['内容'] = content
    datas.append(list1)


if __name__ == '__main__':
    # for temId in range(4113,4116):
    # main('http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectByDocId/data_docId=973858.json')
    temId = 4114
    datas = []
    page = 1
    flag = 0
    while True:
        url = f'http://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectDocByItemIdAndChild/data_itemId={temId},pageIndex={page},pageSize=18.json'
        rows = requests.get(url)
        if rows.status_code == 404:
            url = f'http://www.cbirc.gov.cn/cbircweb/DocInfo/SelectDocByItemIdAndChild?itemId={temId}&pageSize=18&pageIndex={page}'
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
            main(detail_url)
        if flag == 1:
            break
    df = pd.DataFrame(datas)
    df.to_excel(f"{temId}.xlsx",index=False)
