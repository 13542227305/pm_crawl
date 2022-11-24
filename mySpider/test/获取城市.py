import requests
import time
import json

headers = {
    'authority': 'api.m.jd.com',
    'accept': '*/*',
    'referer': 'https://pmsearch.jd.com/',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

sf = {
    1: "北京", 2: "上海", 3: "天津", 4: "重庆", 5: "河北", 6: "山西", 7: "河南", 8: "辽宁", 9: "吉林", 10: "黑龙江", 11: "内蒙古", 12: "江苏",
    13: "山东", 14: "安徽", 15: "浙江", 16: "福建", 17: "湖北", 18: "湖南", 19: "广东", 20: "广西", 21: "江西", 22: "四川", 23: "海南",
    24: "贵州", 25: "云南", 26: "西藏", 27: "陕西", 28: "甘肃", 29: "青海", 30: "宁夏", 31: "新疆", 32: "台湾", 52993: "港澳"
}
city_q = {}
for i in sf:
    dd = {'body': '{"areaId": ' + str(i) + ',"consigneeType":2,"headSorted":false}',
          'loginType': '3',
          'jsonp': 'jsonp_1665921832166_77008'}
    response = requests.get('https://api.m.jd.com/api?appid=paimai&functionId=getAreaInfoMap',
                            params=dd,
                            headers=headers)
    text = str(response.text).replace('jsonp_1665921832166_77008({"code":0,"data":{"ALL":[', "").split("]")[0]
    false = False
    t = eval(text)
    sptext = {}
    print(t)
    if 'tuple' not in str(type(t)):
        sptext[t['name']] = t['id']
    else:
        for tt in t:
            sptext[tt['name']] = tt['id']
    city_q[sf[i]] = sptext
    time.sleep(1)
print(city_q)
