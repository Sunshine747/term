import requests
import json
import indicators
import numpy as np
import time



def get_data(cur_pair, period, start_dt):
    end_dt = time.time()

    date =          []
    closep =        []
    
    request_hist_txt = 'https://poloniex.com/public?command=returnChartData&currencyPair=%s&start=%s&end=%s&period=%s' \
                          %(cur_pair, start_dt, end_dt, period)

##    response_hist = json.loads(requests.get(request_hist_txt).text)
    response_hist = requests.get(request_hist_txt).json()
    
    i = 0
    j = len(response_hist)
    while i != j:
        date.append(response_hist[i]['date'])
        closep.append(response_hist[i]['close'])

        i += 1
    
    return date, closep


def get_price(date, closep, cur_pair):
    end_dt = time.time()


    request_now_txt = 'https://poloniex.com/public?command=returnTicker'

##    response_now = json.loads(requests.get(request_now_txt).text)
    response_now = requests.get(request_now_txt).json()

    current = float(response_now[cur_pair]["last"])

    date.append(end_dt)
    closep.append(current)
    
    sma =   indicators.sma(closep, 3)
    top_line, mid_line, bot_line = indicators.myind(closep, 28, 60)

    return date, closep, sma, top_line, mid_line, bot_line
