import requests

s = 'https://app.dewu.com/api/v1/app/search/entry/search/list'
headers = {
    "shumeiid": "2022110620132284e930f6dd650abcf85fceefa78c7ce50125f03e5113aed7",
    "User-Agent": "duapp/5.4.1(android;6.0.1)",
    "X-Auth-Token": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Njc3MzY4MDAsImV4cCI6MTY5OTI3MjgwMCwiaXNzIjoiYWYyNTg5MWQ5NGMxZjMyYyIsInN1YiI6ImFmMjU4OTFkOTRjMWYzMmMiLCJ1dWlkIjoiYWYyNTg5MWQ5NGMxZjMyYyIsInVzZXJJZCI6MTI3NzE2NjM0NiwiaXNHdWVzdCI6dHJ1ZX0.F0fozofMn6XTzhe9-p3YBWBJFT90D0Py8_8dMb8yqkndBKZ7hZRMfqsleIL9gpShFoJ4ONuVhiHozDOGSm8mq7ZMIsIAG2GhCk-PHeLqSxxkolOEUTb-cM52qaHG0pEXZ-lqkAT6EtLLvchOz2kJjQxFWnx_UJq2MoKkhalrXjhcxjz7K8Q1HKkgJji3MAYc2V6fjGPPSOXsJN2B4ddsrew4V4BIbqpJ3OcCkhPH4P5whWBpw-po_yrAN9zp2zlM6hRWLGZe861M09wDpc59J-3XS05UWWcKuOpAvdAuSPFSjkN7fYQphn2HONXFLKwsNx152QqhpQk6Q1NBoB2TPw",
    "SK": "9JoIDIgRJyimr2GfmI1CjBbcDcbVGlFXY8miVjp4f4UexuuvSGBzrH0wW8eHn9W5byHn3FDqmq6Ri0LclAUa5Z7JVj1w",
    "x-dus-token": "1667737319990;M3mgX5zD4TSQfa/Q52l0f1WRiwM/",
    "duproductid": "1356970333D43DCFEEBF5A66D2763E17BDFE24914A4EEF24D4D5C25559243BDD",
    "Content-Type": "application/json; charset=utf-8",
}
data = {"abTest":[{"name":"cspupro","value":"0"},{"name":"piclocate","value":"2"},{"name":"510_hxdjsp","value":"0"},{"name":"500_qtbq","value":"0"},{"name":"filter_opt","value":"1"}],"enhancedSearch":0,"firstInterfaceStatus":"1","limit":"20","loginToken":"","newSign":"5185bea848283f1bb2a45de04030ba26","originSearch":'false',"page":0,"platform":"android","scene":"trans_product","showHot":1,"smartMenuStatus":0,"sortMode":1,"sortType":0,"timestamp":"1667737319990","title":"婴童鞋","v":"5.4.1"}
res = requests.post(s,headers=headers,data=data).json()
print(res)
