# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标的物标题
    currentPrice = scrapy.Field()  # 当前价/成交价
    minPrice = scrapy.Field()  # 起拍价/变卖价
    assessmentPrice = scrapy.Field()  # 评估价
    _id = scrapy.Field()  # 商品id
    productAddress = scrapy.Field()  # 标的物所在地
    auctionStatus = scrapy.Field()  # 当前状态 预告中:0,进行中:1,已结束:2,已暂缓:6,已中止:7,已撤回:5
    shopName = scrapy.Field()  # 处置单位
    province = scrapy.Field()  # 省份
    courtCityName = scrapy.Field()  # 城市
    bidCount = scrapy.Field()  # 出价次数
    priceLowerOffset = scrapy.Field()  # 加价幅度
    ensurePrice = scrapy.Field()  # 保证金
    bidList = scrapy.Field()  # 出价人列表
    currentPriceStr = scrapy.Field()  # 出价最高价
    queryCount = scrapy.Field()  # 优先购买权人数
    queryData = scrapy.Field()  # 购买人数据
