# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter
from openpyxl import Workbook


class MyspiderPipeline:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.item_head = ['_id', 'title', 'province', 'courtCityName', 'productAddress', 'currentPrice', 'minPrice',
                          'assessmentPrice', 'ensurePrice', 'priceLowerOffset', 'auctionStatus', 'shopName', 'bidCount',
                          'bidList', 'currentPriceStr', 'queryCount', 'queryData']

    def open_spider(self, spider):
        self.ws.append(
            ['商品id', '标的物标题', '省份', '城市', '标的物所在地', '当前价/成交价', '起拍价/变卖价', '评估价', '保证金', '加价幅度', '当前状态', '处置单位', '出价次数',
             '出价人列表', '出价最高价', '优先购买权人数', '购买人数据'])  # 设置表头

    def process_item(self, item, spider):
        line = []
        for i in self.item_head:
            # 预告中: 0, 进行中: 1, 已结束: 2, 已暂缓: 6, 已中止: 7, 已撤回: 5
            if i == 'auctionStatus':
                print(i)
                print(str(item[i]))
                auctionStatus = {0: '预告中', 1: '进行中', 2: '已结束', 6: '已暂缓', 7: '已中止', 5: '已撤回'}
                line.append(auctionStatus.get(int(item[i]), str(item[i])))
            else:
                line.append(str(item[i]))
        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
        return item

    def close_spider(self, spider):
        self.wb.save('拍卖数据.xlsx')
        print("close")

## title 标的物标题
## currentPrice 当前价/成交价
## minPrice 起拍价/变卖价
## assessmentPrice 评估价
## _id 商品id
## productAddress 标的物所在地
## auctionStatus 当前状态 预告中:0,进行中:1,已结束:2,已暂缓:6,已中止:7,已撤回:5
## shopName 处置单位
## province 省份
## courtCityName 城市
## bidCount 出价次数
## priceLowerOffset 加价幅度
## ensurePrice 保证金
## bidList 出价人列表
## currentPriceStr 出价最高价
## queryCount 优先购买权人数
## queryData 购买人数据

# ['商品id','标的物标题','省份','城市','标的物所在地','当前价/成交价','起拍价/变卖价','评估价','保证金','加价幅度','当前状态','处置单位','出价次数','出价人列表','出价最高价','优先购买权人数','购买人数据']
# ['_id','title','province','courtCityName','productAddress','currentPrice','minPrice','assessmentPrice','ensurePrice','priceLowerOffset','auctionStatus','shopName','bidCount','bidList','currentPriceStr','queryCount','queryData']
