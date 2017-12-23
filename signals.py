##myind
def open_long(date, long_f, btc_b, top_line, sma, closep, commission):
    print ('###############################################------BUY(LONG)------################################################')
    long_order = btc_b / closep[-1]
    com = long_order * commission
    long_order = long_order - com
    print ('TIME: ' + datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d %H:%M:%S') \
        + '  COMISSION: ' + str(com) \
        + '  BALANCE ETH: ' + str(long_order) \
        + '  BALANCE BTC: ' + str(0))
    f = open('long.csv', 'a')
    f.write(datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d') + ';' \
            + datetime.fromtimestamp(int(date[-1])).strftime('%H:%M:%S') + ';' \
            + 'BUY;' \
            + closep[-1] + ';' \
            + '0;' \
            + long_order + ';' \
            + com + ';' \
            + commission + ';\n')
    f.close()
    return 1, 0, long_order

def open_short(date, short_f, eth_b, bot_line, sma, closep, commission):
    print ('###############################################------BUY(SHORT)------################################################')
    short_order = eth_b * closep[-1]
    com = short_order * commission
    short_order = short_order - com
    print ('TIME: ' + datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d %H:%M:%S') \
        + '  COMISSION: ' + str(com) \
        + '  BALANCE ETH: ' + str(0) \
        + '  BALANCE BTC: ' + str(short_order))
    f = open('short.csv', 'a')
    f.write(datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d') + ';' \
            + datetime.fromtimestamp(int(date[-1])).strftime('%H:%M:%S') + ';' \
            + 'BUY;' \
            + closep[-1] + ';' \
            + short_order + ';' \
            + '0;' \
            + com + ';' \
            + commission + ';\n')
    f.close()
    return 1, 0, short_order

def close_long(date, long_f, long_order, top_line, sma, closep, commission):
    print ('###############################################------SELL(LONG)------################################################')
    btc_b = long_order * closep[-1]
    com = btc_b * commission
    btc_b = btc_b - com
    print ('TIME: ' + datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d %H:%M:%S') \
        + '  COMISSION: ' + str(com) \
        + '  BALANCE ETH: ' + str(0) \
        + '  BALANCE BTC: ' + str(btc_b))
    f = open('long.csv', 'a')
    f.write(datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d') + ';' \
            + datetime.fromtimestamp(int(date[-1])).strftime('%H:%M:%S') + ';' \
            + 'SELL;' \
            + closep[-1] + ';' \
            + btc_b + ';' \
            + '0;' \
            + com + ';' \
            + commission + ';\n')
    f.close()
    return 0, btc_b, 0

def close_short(date, short_f, short_order, bot_line, sma, closep, commission):
    print ('###############################################------SELL(SHORT)------################################################')
    eth_b = short_order / closep[-1]
    com = eth_b * commission
    eth_b = eht_b - com
    print ('TIME: ' + datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d %H:%M:%S') \
        + '  COMISSION: ' + str(com) \
        + '  BALANCE ETH: ' + str(eth_b) \
        + '  BALANCE BTC: ' + str(0))
    f = open('short.csv', 'a')
    f.write(datetime.fromtimestamp(int(date[-1])).strftime('%Y-%m-%d') + ';' \
            + datetime.fromtimestamp(int(date[-1])).strftime('%H:%M:%S') + ';' \
            + 'SELL;' \
            + closep[-1] + ';' \
            + '0;' \
            + eth_b + ';' \
            + com + ';' \
            + commission + ';\n')
    f.close()
    return 0, eth_b, 0


##def myind_trade(date, price, eth_b, btc_b, ma, myind_top, myind bot, flag):
##    if (ma[i] >= myind_top[i]) && (ma[i-1] < myind_top[i-1]) && flag == 0:
##        flag = open_long(eth_b, btc_b, commission, price, tm)
##    elif (ma[i] <= myind_bot[i]) && (ma[i-1] > myind_bot[i-1]) && flag == 0:
##        open_short(price, volume)
##    elif (ma[i] <= myind_top[i]) && (ma[i-1] > myind_top[i-1]) && flag == 1:
##        close_long(price, volume)
##    elif (ma[i] >= myind_bot[i]) && (ma[i-1] < myind_bot[i-1]) && flag == 1:
##        close_short(price, volume)
##
##
##
##def myind_trade(order_f_btc, order_f_eth, order_btc, order_eth, balance_btc, balance_eth, comission, price, bot_line, top_line, sma):
##    if (sma[i] >= top_line[i]) && (sma[i-1] < top_line[i-1]) && flag == 0:
##        flag = open_long(eth_b, btc_b, commission, price, tm)
##    elif (ma[i] <= myind_bot[i]) && (ma[i-1] > myind_bot[i-1]) && flag == 0:
##        open_short(price, volume)
##    elif (ma[i] <= myind_top[i]) && (ma[i-1] > myind_top[i-1]) && flag == 1:
##        close_long(price, volume)
##    elif (ma[i] >= myind_bot[i]) && (ma[i-1] < myind_bot[i-1]) && flag == 1:
##        close_short(price, volume)
