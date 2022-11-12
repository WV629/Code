import execjs
import re
import requests

# TODO : https://www.aqistudy.cn/historydata/daydata.php?city=%E4%B8%8A%E6%B5%B7&month=201810
def get_data_name():
    url = 'https://www.aqistudy.cn/historydata/resource/js/deRCti2h8FM8A.min.js'
    res = requests.get(url=url,headers=headers).text
    result = re.search('check\|(.*?)\|object',res,re.S).group(1)
    return result

def get_data(data_name):
    cxt = execjs.compile(open('空气质量网.js').read())
    data = cxt.call('getData')
    data = {
        # 'h5pd1h5QD':data
        data_name:data
    }
    return data

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/api/historyapi.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    data = get_data(get_data_name())
    res = requests.post(url,data=data,headers=headers).text
    print(res)
