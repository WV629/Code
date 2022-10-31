import requests
from lxml import etree


# TODO : http://www.cqgjbt.com/pub/gongshi?pageIndex=9260
def init():
    res = s.get(base_url, headers=headers).text
    html = etree.HTML(res)
    __RequestVerificationToken = html.xpath("//input[@name='__RequestVerificationToken']/@value")[0]
    data = {
        '__RequestVerificationToken': __RequestVerificationToken
    }
    return data

def get_response(url):
    data = {
        "__RequestVerificationToken": "xBJ14dMf5A5wEnz6LnUdu/ijCaQJ5sh0vgptD9gThQcWT2Y0t+w0ErgMwr8J2FNX8rWGuufnkyUQzDdqHQOOWI7dzMBQM87PT6I2SpGWsq1AlVcJ1JtcjX91yDc7VxpkKzX0hWaVF46c5IwUvTdFDo8bc1AdOhTjh7982mnIngo=",
        "YearNum": "",
        "areaName": "",
        "AreaCode": "",
        "qy": "",
        "n": "",
        "JiJuLeiXing": "",
        "JiJuLeiXingCode": "",
        "FactoryName": "",
        "BusinessName": "",
        "ChuCBH": "",
        "StartGJRiQi": "",
        "EndGJRiQi": "",
        "StateValue": "",
        "StateName": "",
        "undefined": ""
    }
    for _ in range(5):
        try:
            res = s.post(url,headers=headers,data=data)
            if res.status_code == 200:
                return res
        except Exception as e:
            print('error ----- ',e)
    else:
        return False

def run(url):
    res = get_response(url).content.decode()
    html = etree.HTML(res)
    trs = html.xpath("//tbody[@id='list-pub']/tr")
    print(len(trs))
    for tr in trs:
        list1 = {}
        list1['序号'] = tr.xpath("./td[1]/text()")[0].strip()
        list1['县'] = tr.xpath("./td[2]/text()")[0].strip()
        list1['所在乡(镇)'] = tr.xpath("./td[3]/text()")[0].strip()
        list1['所在村组'] = tr.xpath("./td[4]/text()")[0].strip()
        list1['购机者姓名'] = tr.xpath("./td[5]/text()")[0].strip()
        list1['机具品目'] = tr.xpath("./td[6]/text()")[0].strip()
        list1['生产厂家'] = tr.xpath("./td[7]/text()")[0].strip()
        list1['产品名称'] = tr.xpath("./td[8]/text()")[0].strip()
        list1['购买机型'] = tr.xpath("./td[9]/text()")[0].strip()
        list1['购买数量(台)'] = tr.xpath("./td[10]/text()")[0].strip()
        list1['经销商'] = tr.xpath("./td[11]/text()")[0].strip()
        list1['购机日期'] = tr.xpath("./td[12]/text()")[0].strip()
        list1['单台销售价格(元)'] = tr.xpath("./td[13]/text()")[0].strip()
        list1['单台补贴额(元)'] = tr.xpath("./td[14]/text()")[0].strip()
        list1['总补贴额(元)'] = tr.xpath("./td[15]/text()")[0].strip()
        list1['出厂编号'] = tr.xpath("./td[16]/text()")[0].strip()
        list1['状态'] = tr.xpath("./td[17]/text()")[0].strip()
        print(list1)



if __name__ == '__main__':
    s = requests.session()
    headers = {
        "Cookie": "__RequestVerificationToken_Lw__=xBJ14dMf5A5wEnz6LnUdu/ijCaQJ5sh0vgptD9gThQcWT2Y0t+w0ErgMwr8J2FNX8rWGuufnkyUQzDdqHQOOWI7dzMBQM87PT6I2SpGWsq1AlVcJ1JtcjX91yDc7VxpkKzX0hWaVF46c5IwUvTdFDo8bc1AdOhTjh7982mnIngo=",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    }
    base_url = 'http://www.cqgjbt.com/pub/gongshi?pageIndex=1'
    url = 'http://www.cqgjbt.com/pub/GongShiSearch?pageIndex=2'
    # data = init()
    run(url)

