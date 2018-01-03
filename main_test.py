import time
import get_data_test as gd
from datetime import datetime
import signals as sig

commission = 0.0025
eth_b = 1
btc_b = 1
long_order = 0
short_order = 0
long_f = 0
short_f = 0

a = 0
i = 50
while 1 == 1:
    if i == 50:
        date_data, closep_data = gd.get_data('BTC_ETH', '1800', str(time.time()-(691200+86400)))
        i = 0

    date, closep, sma, top_line, mid_line, bot_line = gd.get_price(date_data, closep_data, 'BTC_ETH')

##    print(datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d') + ';' \
##          + datetime.fromtimestamp(int(date[-1])).strftime('%H:%M:%S') + ';' \
##          + str(sma[-1]) \
##          + str(top_line[-1]) \
##          + str(bot_line[-1]))

    if (sma[-1] >= top_line[-1]) & (sma[-2] < top_line[-2]) & (long_f == 0):
        long_f, btc_b, long_order = sig.open_long(date, long_f, btc_b, top_line, sma, closep, commission)
    elif (sma[-1] <= bot_line[-1]) & (sma[-2] > bot_line[-2]) & (short_f == 0):
        short_f, eth_b, short_order = sig.open_short(date, short_f, eth_b, bot_line, sma, closep, commission)
    elif (sma[-1] <= top_line[-1]) & (sma[-2] > top_line[-2]) & (long_f == 1):
        long_f, btc_b, long_order = sig.close_long(date, long_f, long_order, top_line, sma, closep, commission)
    elif (sma[-1] >= bot_line[-1]) & (sma[-2] < bot_line[-2]) & (short_f == 1):
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
