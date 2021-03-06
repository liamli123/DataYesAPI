# -*- coding: utf-8 -*-
from dataapiclient import Client
import json
import urllib2
from urllib2 import urlopen
import re
import httplib, urllib
import datetime
"""
client.init('U TOKEN')
url = '' change for diff API e.g: https://apidoc.datayes.com/app/APIDetail/9
U can use the print to simple output the data or write it to the csv

API documentation
https://mall.datayes.com/datapreview/106?lang=zh

"""
def getequclient(ticker,secID,type):
    try:
        client = Client()
        client.init('ae8820c8eb8ccd418dd8141b4c685d2d208c58a564a9fd2c22f8c95ac6a2ef23')
        url1='/api/equity/getEqu.json?field=&listStatusCD=&secID='+secID+'&ticker='+ticker+'&equTypeCD='+type
        # ticker = 000001
        # secID 000001.XSHE
        # listStatusCD A
        # equTypeCD
        rawresult = client.getData(url1)
        # rawresult is a 2 elements tuple (200, '{"retCode":1,"retMsg":"Success","data":[{"secID":"000002.XSHE","ticker":"000002","exchangeCD":"XSHE","ListSectorCD":1,"ListSector":"\xe4\xb8\xbb\xe6\x9d\xbf","transCurrCD":"CNY","secShortName":"\xe4\xb8\x87\xe7\xa7\x91A","secFullName":"\xe4\xb8\x87\xe7\xa7\x91\xe4\xbc\x81\xe4\xb8\x9a\xe8\x82\xa1\xe4\xbb\xbd\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb8","listStatusCD":"L","listDate":"1991-01-29","equTypeCD":"A","equType":"\xe6\xb2\xaa\xe6\xb7\xb1A\xe8\x82\xa1","exCountryCD":"CHN","partyID":3,"totalShares":11039152000,"nonrestFloatShares":11024120600,"nonrestfloatA":9709165100,"officeAddr":"\xe5\xb9\xbf\xe4\xb8\x9c\xe7\x9c\x81\xe6\xb7\xb1\xe5\x9c\xb3\xe5\xb8\x82\xe7\x9b\x90\xe7\x94\xb0\xe5\x8c\xba\xe5\xa4\xa7\xe6\xa2\x85\xe6\xb2\x99\xe7\x8e\xaf\xe6\xa2\x85\xe8\xb7\xaf33\xe5\x8f\xb7\xe4\xb8\x87\xe7\xa7\x91\xe4\xb8\xad\xe5\xbf\x83","primeOperating":"\xe6\x88\xbf\xe5\x9c\xb0\xe4\xba\xa7\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x8f\x8a\xe6\x8a\x95\xe8\xb5\x84\xe9\x9b\xb6\xe5\x94\xae\xe4\xb8\x9a\xe5\x8a\xa1\xe3\x80\x82","endDate":"2017-06-30","TShEquity":161157756356.52}]}')
        # first element is 200
        # second element is a string
        # if code==200:
        data=json.loads(rawresult[1])
        # Convert tuple's second element the string to a dictionary, useful information is after 'data':
        # data['data'] is a one element list, so access the content through data['data'][0]
        for item in data['data'][0]:
            print item, data['data'][0][item]
            # primeOperating
            # ListSectorCD
            # exchangeCD
            # secID
            # secFullName
            # nonrestFloatShares
            # endDate
            # officeAddr
            # listDate
            # secShortName
            # TShEquity
            # equType
            # nonrestfloatA
            # listStatusCD
            # ListSector
            # partyID
            # totalShares
            # transCurrCD
            # exCountryCD
            # ticker
            # equTypeCD
        # print type(result)        <type 'tuple'>
        # print type(data)          <type 'dict'>
        # print type(data['data'])  <type 'list'>
        # print type(data['data'][0])<type 'dict'>

    except Exception, e:
        print 'error'

def getalldata():

    conn = httplib.HTTPSConnection("api.wmcloud.com", 443, timeout=60)
    token = "ae8820c8eb8ccd418dd8141b4c685d2d208c58a564a9fd2c22f8c95ac6a2ef23"
    headers = {"Authorization": "Bearer " + token}
    # params = urllib.urlencode({"listStatusCD": "L","secID":"" ,"ticker":"","equTypeCD":""})
    conn.request("GET", "/data/v1/api/equity/getEqu.json?", "", headers)
    r1 = conn.getresponse()

    dataresult=json.load(r1)
    # print r1.status, r1.reason
    # print r1.read()
    # print type(dataresult)
    # print type(dataresult['data'])
    # print type(len(dataresult['data']))
    for item in dataresult['data']:
        print item['secFullName'],item['ticker'],item['equType'],item['exchangeCD']

def getstockdata(ticker):

    conn = httplib.HTTPSConnection("api.wmcloud.com", 443, timeout=60)
    token = "ae8820c8eb8ccd418dd8141b4c685d2d208c58a564a9fd2c22f8c95ac6a2ef23"
    headers = {"Authorization": "Bearer " + token}
    params = urllib.urlencode({"listStatusCD": "L","secID":"" ,"ticker":ticker,"equTypeCD":""})
    conn.request("GET", "/data/v1/api/equity/getEqu.json?"+params, "", headers)
    r1 = conn.getresponse()

    dataresult=json.load(r1)
    # print r1.status, r1.reason
    # print r1.read()
    # print type(dataresult)
    # print type(dataresult['data'])
    # print type(len(dataresult['data']))
    for item in dataresult['data']:
        print 'secFullName',item['secFullName']
        print 'primeOperating',item['primeOperating']
        print 'ListSector',item['ListSector']
        print 'secFullName',item['secFullName']
        print 'ticker',item['ticker']
        print 'equType',item['equType']
        print 'TotalShares', item['totalShares']
        print ''
        print 'ListSectorCD',item['ListSectorCD']
        print 'exchangeCD',item['exchangeCD']
        print 'secID',item['secID']
        print 'equTypeCD',item['equTypeCD']
        print 'nonrestFloatShares',item['nonrestFloatShares']
        print 'endDate',item['endDate']
        print 'officeAddr',item['officeAddr']
        print 'listDate',item['listDate']
        print 'secShortName',item['secShortName']
        print 'TShEquity',item['TShEquity']
        print 'nonrestfloatA',item['nonrestfloatA']
        print 'listStatusCD',item['listStatusCD']
        print 'partyID',item['partyID']
        print 'transCurrCD',item['transCurrCD']
        print 'exCountryCD',item['exCountryCD']

def getstockprice(stock):

    conn = httplib.HTTPSConnection("api.wmcloud.com", 443, timeout=60)
    token = "ae8820c8eb8ccd418dd8141b4c685d2d208c58a564a9fd2c22f8c95ac6a2ef23"
    headers = {"Authorization": "Bearer " + token}
    # enddate=datetime.datetime.strptime(edate,'%y%m%d').date()
    # begdate=datetime.datetime.strptime(bdate,'%y%m%d').date()
    params = urllib.urlencode({"secID":stock})
    # Date format: yyyymmdd
    conn.request("GET", "/data/v1/api/market/getMktEquyJL.json?"+params, "", headers)
    r1 = conn.getresponse()

    priceresult=json.load(r1)

    # secID证券内部编码
    print'证券内部编码', priceresult['data'][0]['secID']
    # ticker证券代码
    print'证券代码', priceresult['data'][0]['ticker']
    # secShortName证券简称
    print'证券简称', priceresult['data'][0]['secShortName']
    # exchangeCD交易市场
    print'交易市场', priceresult['data'][0]['exchangeCD']
    # endDate截止日期

    for i in range(len(priceresult['data'])):
        print'首个交易日', priceresult['data'][i]['firstTradeDate']
        print'开盘价', priceresult['data'][i]['openPrice']
        print'最后交易日', priceresult['data'][i]['lastTradeDate']
        print'收盘价', priceresult['data'][i]['closePrice']

        # print'截止日期', priceresult['data'][i]['endDate']
        # # firstTradeDate首个交易日
        # print'首个交易日', priceresult['data'][i]['firstTradeDate']
        # # lastTradeDate最后交易日
        # print'最后交易日', priceresult['data'][i]['lastTradeDate']
        # # numDays交易天数
        # print'交易天数', priceresult['data'][i]['numDays']
        # # preClosePrice昨收价
        # print'昨收价', priceresult['data'][i]['preClosePrice']
        # # openPrice开盘价
        # print'开盘价', priceresult['data'][i]['openPrice']
        # # highestPrice最高价
        # print'最高价', priceresult['data'][i]['highestPrice']
        # # dayHigh最高价日
        # print'最高价日', priceresult['data'][i]['dayHigh']
        # # lowestPrice最低价
        # print'最低价', priceresult['data'][i]['lowestPrice']
        # # dayLow最低价日
        # print'最低价日', priceresult['data'][i]['dayLow']
        # # closePrice收盘价
        # print'收盘价', priceresult['data'][i]['closePrice']
        # # highClosePrice最高收盘价
        # print'最高收盘价', priceresult['data'][i]['highClosePrice']
        # # dayHcp最高收盘价日
        # print'最高收盘价日', priceresult['data'][i]['dayHcp']
        # # lowClosePrice最低收盘价
        # print'最低收盘价', priceresult['data'][i]['lowClosePrice']
        # # dayLcp最低收盘价日
        # print'最低收盘价日', priceresult['data'][i]['dayLcp']
        # # avgPrice均价
        # print'均价', priceresult['data'][i]['avgPrice']
        # # rangePct振幅
        # print'振幅', priceresult['data'][i]['rangePct']
        # # adChg涨跌(后复权)
        # print'涨跌(后复权)', priceresult['data'][i]['adChg']
        # # adChgPct涨跌幅
        # print'涨跌幅', priceresult['data'][i]['adChgPct']
        # # logReturn对数收益率
        # print'对数收益率', priceresult['data'][i]['logReturn']
        # # turnoverVol成交量
        # print'成交量', priceresult['data'][i]['turnoverVol']
        # # turnoverValue成交额
        # print'成交额', priceresult['data'][i]['turnoverValue']
        # # turnoverRate换手率
        # print'换手率', priceresult['data'][i]['turnoverRate']
        # # avgTurnoverRate平均换手率
        # print'平均换手率', priceresult['data'][i]['avgTurnoverRate']
        # # adPreClosePrice昨收价(后复权)
        # print'昨收价(后复权)', priceresult['data'][i]['adPreClosePrice']
        # # adOpenPrice开盘价(后复权)
        # print'开盘价(后复权)', priceresult['data'][i]['adOpenPrice']
        # # adHighestPrice最高价(后复权)
        # print'最高价(后复权)', priceresult['data'][i]['adHighestPrice']
        # # adDayHigh最高价日(后复权)
        # print'最高价日(后复权)', priceresult['data'][i]['adDayHigh']
        # # adDayLow最低价日(后复权)
        # print'最低价日(后复权)', priceresult['data'][i]['adDayLow']
        # # adLowestPrice最低价(后复权)
        # print'最低价(后复权)', priceresult['data'][i]['adLowestPrice']
        # # adClosePrice收盘价(后复权)
        # print'收盘价(后复权)', priceresult['data'][i]['adClosePrice']
        # # adHighClosePrice最高收盘价(后复权)
        # print'最高收盘价(后复权)', priceresult['data'][i]['adHighClosePrice']
        # # adLowClosePrice最低收盘价(后复权)
        # print'最低收盘价(后复权)', priceresult['data'][i]['adLowClosePrice']
        # # adDayHcp最高收盘价日(后复权)
        # print'最高收盘价日(后复权)', priceresult['data'][i]['adDayHcp']
        # # adDayLcp最低收盘价日(后复权)
        # print'最低收盘价日(后复权)' ,priceresult['data'][i]['adDayLcp']


getstockprice('000001.XSHE')