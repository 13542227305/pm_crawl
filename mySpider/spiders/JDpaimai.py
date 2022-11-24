import time

import scrapy
from mySpider.items import MyspiderItem
from urllib.parse import urlencode
import mySpider.settings as set
# import logging


# class ItcastSpider(scrapy.Spider):
class JDPaimai(scrapy.Spider):
    name = 'jdpm'
    # logging.debug("start crawl jdpm")

    # 不带参数的情况下
    # def start_requests(self):
    #     encoded_params = urlencode(set.params)
    #     start_urls = ['https://api.m.jd.com/api?{}'.format(encoded_params)]
    #     for url in start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 带参数的情况下
    def __init__(self, dic, page=1, **kwargs):
        super().__init__(**kwargs)
        self.dic = dic
        self.page = page
        # logging.debug("param:[page:%s,dic:%s]" % (dic, page))

    def start_requests(self):
        start_urls = []
        print("共爬取页数为：", self.page)
        for i in range(int(self.page) + 1):
            encoded_params = urlencode(set.get_params(eval(self.dic), i+1))
            start_urls.append('https://api.m.jd.com/api?{}'.format(encoded_params))
        print(start_urls)
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, *args, **kwargs):
        # print(response.body)
        data = eval(
            str(response.body, 'UTF-8').replace(set.jsonp, "").lstrip('({"code":0,"datas":').split('message')[0].rstrip(
                ',"'))
        # temp = {}
        for da in data:
            temp = {}
            temp['title'] = da['title']  # 标的物标题
            temp['currentPrice'] = da['currentPrice']  # 当前价/成交价
            temp['minPrice'] = da['minPrice']  # 起拍价/变卖价
            temp['assessmentPrice'] = da['assessmentPrice']  # 评估价
            temp['_id'] = da['id']  # 商品id
            temp['productAddress'] = da['productAddress']  # 标的物所在地
            temp['auctionStatus'] = da['auctionStatus']  # 当前状态 预告中:0,进行中:1,已结束:2,已暂缓:6,已中止:7,已撤回:5
            temp['shopName'] = da['shopName']  # 处置单位
            temp['province'] = da['province']  # 省份
            # temp['courtCityName'] = da['courtCityName']  # 城市
            temp['courtCityName'] = da.get('courtCityName', "")  # 城市
            # temp['bidCount'] = da['bidCount']  # 出价次数
            jsonp = set.jsonp
            paimaiId = da['id']
            getDetailsParams = set.getDetailsParams(paimaiId)
            encoded_getDetailsParams = urlencode(getDetailsParams)
            getDetails_url = 'https://api.m.jd.com/api?{}'.format(encoded_getDetailsParams)
            yield scrapy.Request(url=getDetails_url, callback=self.getDetails_parse,
                                 meta={"temp": temp, "jsonp": jsonp, "paimaiId": da['id']})

    def getDetails_parse(self, response, *args, **kwargs):
        item = response.meta["temp"]
        jsonp = response.meta["jsonp"]
        paimaiId = response.meta['paimaiId']
        data = eval(
            str(response.body, 'UTF-8').replace(jsonp, "").replace('({"code":0,"data":', '').split(',"message')[0])
        item['priceLowerOffset'] = data['priceLowerOffset']  # 加价幅度
        item['ensurePrice'] = data['ensurePrice']  # 保证金

        getbidCountParams = set.getbidCountParams(paimaiId)
        encoded_getbidCountParams = urlencode(getbidCountParams)
        getBidCount_Url = 'https://api.m.jd.com/api?{}'.format(encoded_getbidCountParams)
        yield scrapy.Request(url=getBidCount_Url, callback=self.getBidCount_parse,
                             meta={"temp": item, "jsonp": jsonp, "paimaiId": paimaiId})

    # 获取竞价次数
    def getBidCount_parse(self, response, *args, **kwargs):
        item = response.meta["temp"]
        jsonp = response.meta["jsonp"]
        paimaiId = response.meta['paimaiId']
        data = eval(str(response.body, 'UTF-8').replace(jsonp, "").replace('({"code":0,"data":', '').split(',"message')[
                        0].replace("null", '"null"'))  # 因字符中有包含null，而非字符串'null'，故作替换
        item['bidCount'] = data['bidCount']  # 出价次数
        item['bidList'] = data['bidList']  # 出价人列表
        item['currentPriceStr'] = data['currentPriceStr']  # 出价最高价
        """
        数据样式：列表形式，每个出价为一个字典
        bidTime:拍卖时间戳
        paimaiId:拍卖产品id
        price：出价价格
        username：用户id
        """
        getQueryAllPriorPurchaserLevelParams = set.getQueryAllPriorPurchaserLevelParams(paimaiId)
        encoded_getQueryAllPriorPurchaserLevelParams = urlencode(getQueryAllPriorPurchaserLevelParams)
        getQueryAllPriorPurchaserLevel_Url = 'https://api.m.jd.com/api?{}'.format(
            encoded_getQueryAllPriorPurchaserLevelParams)
        yield scrapy.Request(url=getQueryAllPriorPurchaserLevel_Url, callback=self.getqueryAllPriorPurchaserLevel_parse,
                             meta={"temp": item, "jsonp": jsonp, "paimaiId": paimaiId})
        # yield item

    # 获取优先购买人
    def getqueryAllPriorPurchaserLevel_parse(self, response, *args, **kwargs):
        item = response.meta["temp"]
        jsonp = response.meta["jsonp"]
        data = eval(str(response.body, 'UTF-8').replace(jsonp, "").replace(";", ""))
        # {'code': 0, 'status': 0, 'data': [], 'message': '成功'}
        if len(data['data']) == 0:
            item['queryCount'] = 0  # 优先购买权人数
            item['queryData'] = "无"  # 购买人数据
        else:
            item['queryCount'] = len(data['data'])  # 优先购买权人数
            item['queryData'] = data['data']  # 购买人数据
        print(item)
        yield item
