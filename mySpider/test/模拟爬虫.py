import requests
import time

jsonp = "jsonp_" + str(int(time.time() * 1000)) + "_18137"

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

params = {
    "appid": "paimai",
    "functionId": "paimai_unifiedSearch",
    'body': '{'
            '"investmentType":"",'
            '"apiType":12,'
            '"page":1,'
            '"pageSize":40,'
            '"keyword":"",'
            '"provinceId":"",'
            '"cityId":"",'
            '"countyId":"",'
            '"multiPaimaiStatus":"",'
            '"multiDisplayStatus":"",'
            '"multiPaimaiTimes":"",'
            '"childrenCateId":"",'
            '"currentPriceRangeStart":"",'
            '"currentPriceRangeEnd":"",'
            '"timeRangeTime":"endTime",'
            '"timeRangeStart":"",'
            '"timeRangeEnd":"",'
            '"loan":"",'
            '"purchaseRestriction":"",'
            '"orgId":"",'
            '"orgType":"",'
            '"sortField":8,'
            '"projectType":1,'
            '"reqSource":0,'
            '"labelSet":"1027,1028",'
            '"publishSource":""}',
    "jsonp": jsonp}

response = requests.get(
    'https://api.m.jd.com/api?',
    params=params,
    headers=headers)
print(response.url)
data = eval(str(response.text).replace(jsonp, "").lstrip('({"code":0,"datas":').split('message')[0].rstrip(',"'))
print(type(data[0]))
print(data[0])

"""
有多个类型的以逗号隔开，全部的为空
项目类型projectType:1竞价项目,2招商项目
开始时间和
结束时间timeRangeStart-timeRangeEnd  格式2022-06-15
资产性质当项目类型为1时{labelSet:全部:"",诉讼资产:1027,刑案资产:1028,破产资产:1029,海关罚没:1030,政府罚没:1039,国有资产:1031,商业资产:1032,金融资产:1033}。为2时{publishSource：9商业资产/金融资产/国有资产，10破产资产}
标的物类型childrenCateId:{住宅用房:101,商业用房:102,工业用房:103,其他用房:104,机动车:105,船舶:106,其他交通运输工具:107,股权:108,债权:109,矿权:110,林权:111,土地:112,工程:113,机械设备:114,无形资产:115,知识产权:116,租赁/经营权:117,奢侈品:118,生活物资:119,工业物资:120,库存物资:121,打包处置:122,其他财产:123}
省份provinceId:{北京:1,上海:2,天津:3,重庆:4,河北:5,山西:6,河南:7,辽宁:8,吉林:9,黑龙江:10,内蒙古:11,江苏:12,山东:13,安徽:14,浙江:15,福建:16,湖北:17,湖南:18,广东:19,广西:20,江西:21,四川:22,海南:23,贵州:24,云南:25,西藏:26,陕西:27,甘肃:28,青海:29,宁夏:30,新疆:31,台湾:32,港澳:52993}
城市cityId:见省份和城市txt
区县编码countyId:具体获取用获取区县编码.py
竞价状态1multiPaimaiStatus:{预告中:0,进行中:1,已结束:2,全选:0,1,2}
竞价状态2multiDisplayStatus:{已暂缓:6,已中止:7,已撤回:5,全选:6,7}
拍卖阶段multiPaimaiTimes:{一拍:1,二拍:2,变卖:4,全选:1,2,4}
当前/起拍价currentPriceRangeStart":"1"/"currentPriceRangeEnd":"100000"
拍卖开始时间和结束时间:"timeRangeStart":"2022-08-03","timeRangeEnd":"2022-10-22"
"""
