# -*- coding: utf-8 -*-
# File       : 获取区县编码.py
# Time       ：2022/10/29 19:22
# Author     ：袁润和
# version    ：python 3.5
# Description：

import requests

headers = {
    'authority': 'api.m.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://pmsearch.jd.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

cityId = 1704  # 城市编码
jsonp = 'jsonp_1667036285291_21485'  # 时间戳

response = requests.get('https://api.m.jd.com/api?appid=paimai&functionId=getAreaInfoMap&body={areaId:' + str(
    cityId) + ',consigneeType:3,headSorted:false}&loginType=3&jsonp=' + jsonp, headers=headers)
print(response.url)
false = False
response_text = eval(str(str(response.text).replace(jsonp, '').rstrip(');').lstrip('(')))
for i in response_text['data']['ALL']:
    print(i)
