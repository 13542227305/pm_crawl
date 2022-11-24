# -*- coding: utf-8 -*-
# File       : 详细页查询.py
# Time       ：2022/11/6 19:48
# Author     ：袁润和
# version    ：python 3.5
# Description：

import requests

import requests

headers = {
    'authority': 'api.m.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://paimai.jd.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    "appid": "paimai",
    "functionId": "getProductBasicInfo",
    "body": '{"paimaiId":291717176}',
    "loginType": 3,
    "jsonp": "jsonp_1667735211392_29024"
}

# response = requests.get('https://api.m.jd.com/api?appid=paimai&functionId=getProductBasicInfo&body=\\{%22paimaiId%22:291717176\\}&loginType=3&jsonp=jsonp_1667735211392_29024', cookies=cookies, headers=headers)
response = requests.get('https://api.m.jd.com/api?', headers=headers, params=params)
print(response.text)
print(type(response.text))
data = eval(response.text.replace("jsonp_1667735211392_29024", "").replace('({"code":0,"data":','').split(',"message')[0])
# data = eval(
#             str(response.text, 'UTF-8').replace("jsonp_1667735211392_29024", "").lstrip('({"code":0,"data":').split('message')[0].rstrip(
#                 ',"'))
print(data)
print(type(data))
