import time
import get_data_test as gd
from datetime import datetime
import signals as sig

commission = 0.0025
eth_b = 0
btc_b = 1
long_order = 0
short_order = 0
long_f = 0
short_f = 0

a = 0
i = 100
while a != 1000:
    if i == 100:
        date_data, closep_data = gd.get_data('BTC_ETH', '300', str(time.time()-(691200+86400)))
        i = 0

    date, closep, sma, top_line, mid_line, bot_line = gd.get_price(date_data, closep_data, 'BTC_ETH')

    if (sma[i] >= top_line[i]) && (sma[i-1] < top_line[i-1]) && long_f == 0:
        long_f, btc_b, long_order = sig.open_long(date, long_f, btc_b, top_line, sma, closep, commission)
    elif (sma[i] <= bot_line[i]) && (sma[i-1] > bot_line[i-1]) && short_f == 0:
        short_f, eth_b, short_order = sig.open_short(date, short_f, eth_b, bot_line, sma, closep, commission)
    elif (sma[i] <= top_line[i]) && (sma[i-1] > top_line[i-1]) && long_f == 1:
        long_f, btc_b, long_order = sig.close_long(date, long_f, long_order, top_line, sma, closep, commission)
    elif (sma[i] >= bot_line[i]) && (sma[i-1] < bot_line[i-1]) && short_f == 1:
        short_f, eth_b, short_order = sig.close_short(date, short_f, short_order, bot_line, sma, closep, commission)




##    sig.myind_trade(date, closep, eth_b, btc_b, sma, top_line, bot_line, flag_l)

##    print (datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d %H:%M:%S') \
##                  + '  LAST: ' + str(closep[-1]) \
##                  + '  SMA(3): ' + str(sma[-1]) \
##                  + '  TOP: ' + str(top_line[-1]) \
##                  + '  BOT: ' + str(bot_line[-1]))
    i += 1
    a += 1
    time.sleep(0.5)
