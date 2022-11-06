import requests


# TODO : http://xysh888.com/
def Chinese_to_English(text):
    url = 'http://xysh888.com/ggtranslate.php'
    data = {
        'from': 'zh-CN',
        'fromtxt': '中文',
        'to': 'en',
        'totxt': '英语',
        'content': text
    }
    res = requests.post(url,data=data).json()['trans']
    return res

def English_to_Chinese(text):
    url = 'http://xysh888.com/ggtranslate.php'
    data = {
        'from': 'en',
        'fromtxt': '英语',
        'to': 'zh-CN',
        'totxt': '中文',
        'content': text
    }
    res = requests.post(url, data=data).json()['trans']
    return res

if __name__ == '__main__':
    print(Chinese_to_English('你好'))
    print(English_to_Chinese("hello"))