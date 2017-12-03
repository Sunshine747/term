import requests
import json
import indicators
import numpy as np
import time



def get_data(cur_pair, period, start_dt):
    end_dt = time.time()
    
    request_hist_txt = 'https://poloniex.com/public?command=returnChartData&currencyPair=%s&start=%s&end=%s&period=%s' \
                          %(cur_pair, start_dt, end_dt, period)
    #request_now_txt = requests.get('https://poloniex.com/public?command=returnTicker')
    print(request_hist_txt)
    response_hist = json.loads(requests.get(request_hist_txt).text)
    #response_now = json.loads(requests.get(request_now_txt).text)

    date =          []
    high =          []
    low =           []
    openp =         []
    closep =        []
    volume =        []
    qt_volume =     []
    change =        []
    
    sma =           []
    ema5 =          []
    ema15 =         []
    macd =          []
    macd_signal =   []
    cog_date =      []
    cog =           []
    dateBB =        []
    topBB =         []
    botBB =         []
    midBB =         []
    bdate2 =        []
    topBB2 =        []
    botBB2 =        []
    
    i = 0
    j = len(response_hist)
    while i != j:
        date.append(response_hist[i]['date'])
        high.append(response_hist[i]['high'])
        low.append(response_hist[i]['low'])
        openp.append(response_hist[i]['open'])
        closep.append(response_hist[i]['close'])
        volume.append(response_hist[i]['volume'])
        qt_volume.append(response_hist[i]['quoteVolume'])
        change.append(response_hist[i]['weightedAverage'])

        i += 1

    sma =   indicators.sma(closep, 3)
    ema5 =  indicators.ema(closep, 3)
    ema15 = indicators.ema(closep, 15)
    rsi5 =   indicators.rsi(closep, 5)
    rsi15 = indicators.rsi(closep, 15)
    macd, macd_signal = indicators.macd(closep, 3, 9)
    cog_date, cog = indicators.cog(date, closep, 20)
    dateBB, topBB, topBB2, botBB, botBB2, midBB = indicators.bb(2, 1, 21, closep, date)
    top_line, mid_line, bot_line = indicators.myind(closep, 28, 60)
    atr = indicators.atr(closep, high, low)
    
    return date, high, low, openp, closep, volume, qt_volume, change, sma, ema5, ema15, rsi5, rsi15, macd, macd_signal, cog_date, cog, dateBB, topBB, topBB2, botBB, botBB2, midBB, top_line, mid_line, bot_line, atr
