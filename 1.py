import requests

url = 'https://www.heisener.com/Products/Power-Supplies-Board-Mount/DC-DC-Converters/_Page_41'
tunnel = "tps427.kdlapi.com:15818"

# 用户名密码方式
username = "t15586354322485"
password = "nopucqkl"
proxies ={
            'http':'127.0.0.1:7890',
            'https':'127.0.0.1:7890',
        }
headers= {
    "cookie": "_ga=GA1.1.369914249.1667566871; _fbp=fb.1.1667566871854.1809974710; JSESSIONID=9C37A4436BF8125A3CAC2A68D466D11B; TawkConnectionTime=0; twk_uuid_5c788adba726ff2eea5a0564=%7B%22uuid%22%3A%221.SwmNFjgb6rqA2p89pX8CwCvSabyfBWmOFhBJYetudhChq4tn80I8jS22qKWvgoKiGkShImgWHWcq3j7042fjqwXuQHIgzaxzyepO0FYOx4LVPJscEeYRl%22%2C%22version%22%3A3%2C%22domain%22%3A%22heisener.com%22%2C%22ts%22%3A1668252144427%7D; _ga_S66ELFQ16Q=GS1.1.1668249876.2.1.1668252176.0.0.0; _ga_F8KGWE37EL=GS1.1.1668249877.2.1.1668252176.0.0.0",
    "pragma": "no-cache",
    "referer": "https://www.heisener.com/Products/Power-Supplies-Board-Mount/DC-DC-Converters/_Page_40",
    "sec-ch-ua": "\"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
res = requests.get(url,headers=headers,proxies=proxies).status_code
print(res)
