# -*- coding: utf-8 -*-
# File       : runJDPM.py
# Time       ：2022/11/24 0:15
# Author     ：袁润和
# version    ：python 3.5
# Description：启动jd爬虫

import xlrd
from mySpider.test import jdProfile as zdpz
from scrapy.cmdline import execute
import sys, os

page = 1
provinceId = ""
city = ""
labelSet = "1027,1028"
multiDisplayStatus = ""
multiPaimaiStatus = ""
childrenCateId = ""

param = {
    "appid": "paimai",
    "functionId": "paimai_unifiedSearch",
    'body': '{'
            '"investmentType":"",'
            '"apiType":12,'
            '"page":' + str(page) + ','
                                    '"pageSize":40,'
                                    '"keyword":"",'
                                    '"provinceId":"' + str(provinceId) + '",'
                                                                         '"cityId":"' + str(city) + '",'
                                                                                                    '"countyId":"",'
                                                                                                    '"multiPaimaiStatus":"' + str(
        multiPaimaiStatus) + '",'
                             '"multiDisplayStatus":"' + str(multiDisplayStatus) + '",'
                                                                                  '"multiPaimaiTimes":"",'
                                                                                  '"childrenCateId":"' + str(
        childrenCateId) + '",'
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
                          '"labelSet":"' + str(labelSet) + '",'
                                                           '"publishSource":""}',
    "jsonp": 'jsonp_1669223374723_57814'}

workbook = xlrd.open_workbook(filename='选项选择.xlsx')
table = workbook.sheet_by_name(sheet_name='选择')
row = table.nrows
pro_text1 = {}
pro_text2 = {}
for i in range(row):
    if i == 0:
        continue
    table_list = table.row_values(rowx=i, start_colx=0, end_colx=None)
    pro_text1[table_list[0]] = table_list[1]
print('选项类型', pro_text1)
# 处理标的物类型
try:
    childrenCateId = pro_text1['标的物类型']
    pro_text2['childrenCateId'] = zdpz.childrenCateId[childrenCateId]
    childrenCateId = zdpz.childrenCateId[childrenCateId]
except Exception as e:
    print("处理标的物类型报错:", e)

# 资产性质
try:
    labelSet = pro_text1['资产性质']
    pro_text2['labelSet'] = str(zdpz.labelSet[labelSet])
    labelSet = str(zdpz.labelSet[labelSet])
except Exception as e:
    print("处理资产性质报错:", e)

# 竞价状态
try:
    Status = pro_text1['竞价状态']
    # pro_text2['labelSet'] = zdpz.labelSet[labelSet]
    if Status in zdpz.multiPaimaiStatus:
        pro_text2['multiPaimaiStatus'] = zdpz.multiPaimaiStatus[Status]
        multiDisplayStats = zdpz.multiPaimaiStatus[Status]
        pro_text2['multiDisplayStatus'] = ''
        multiDisplayStatus = ''
    elif Status in zdpz.multiDisplayStatus:
        pro_text2['multiDisplayStatus'] = zdpz.multiDisplayStatus[Status]
        multiDisplayStatus = zdpz.multiDisplayStatus[Status]
        pro_text2['multiPaimaiStatus'] = ''
        multiPaimaiStatus = ''
    elif Status == '全选':
        pro_text2['multiPaimaiStatus'] = zdpz.multiPaimaiStatus[Status]
        multiPaimaiStatus = zdpz.multiPaimaiStatus[Status]
        pro_text2['multiDisplayStatus'] = zdpz.multiDisplayStatus[Status]
        multiDisplayStatus = zdpz.multiDisplayStatus[Status]
    else:
        pro_text2['multiDisplayStatus'] = ''
        multiDisplayStatus = ''
        pro_text2['multiPaimaiStatus'] = ''
        multiPaimaiStatus = ''
except Exception as e:
    print("处理竞价状态报错:", e)

# 省份
try:
    province = pro_text1['省份']
    pro_text2['province'] = zdpz.province2[province]
    province = zdpz.province2[province]
except Exception as e:
    print("处理省份报错:", e)

# 城市
try:
    city = pro_text1['城市']
    pro_text2['city'] = zdpz.city[pro_text1['省份']][city]
    city = zdpz.city[pro_text1['省份']][city]
except Exception as e:
    print("处理省份报错:", e)

# 页码
try:
    page = int(pro_text1['页数'])
    pro_text2['page'] = page
except Exception as e:
    print("处理页码报错:", e)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
execute(['scrapy', 'crawl', 'jdpm', "-a", "dic=" + str(pro_text2), "-a", "page=1"])
