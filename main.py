import time
import get_data as gd
import graph

date, high, low, openp, closep, volume, qt_volume, change, sma, ema5, ema15, rsi5, rsi15, macd, macd_signal, cog_date, cog, dateBB, topBB, topBB2, botBB, botBB2, midBB, top_line, mid_line, bot_line = gd.get_data('BTC_ETH', '1800', str(time.time()-(691200+86400)))
graph.visual('BTC_ETH', date, openp, high, low, closep, volume, sma, ema5, ema15, rsi5, rsi15, macd, macd_signal, cog_date, cog, dateBB, topBB, topBB2, botBB, botBB2, midBB, top_line, mid_line, bot_line)

##print(top_line)
##print(mid_line)
##print(bot_line)

##print(dateBB)
##print(topBB)
##print(botBB)
##print(midBB)
#print(sma)
#print(ema5)
#print(ema15)
