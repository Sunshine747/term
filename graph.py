import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, epoch2num, date2num
from matplotlib.ticker import MultipleLocator
from matplotlib import style

import numpy as np
import datetime as dt

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

def visual(cur_pair, date, openp, high, low, closep, volume, sma, ema_s, ema_l, rsi5, rsi15, macd, macd_signal, cog_date, cog, dateBB, topBB, topBB2, botBB, botBB2, midBB, top_line, mid_line, bot_line, atr):

    start = len(date[30-1:])
    space = 1000
    minorLocator = MultipleLocator(space)
    
    style.use ('ggplot')
    #dark_background
    #ggplot
    #fivethirtyeight
    
    fig = plt.figure('''facecolor='#f0f0f0''')
    ax1 = plt.subplot2grid((5,1), (0,0), rowspan=3, colspan=1)
    plt.ylabel('Stok Prices/Volume/COG/BB')
    plt.title(cur_pair)
    ax2 = plt.subplot2grid((5,1), (3,0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('MACD')
    ax3 = plt.subplot2grid((5,1), (4,0), rowspan=1, colspan=1, sharex=ax1)
    plt.ylabel('RSI')
    ax1v = ax1.twinx()
    ax1cog = ax1.twinx()
    
##    ax1sma = ax1.twinx()
##    ax1ema_s = ax1.twinx()
##    ax1ema_l = ax1.twinx()
##    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
##
##    datec =[]
##    
##    i=0
##    for d in date:
##        datec.append(mdates.epoch2num(d))
##        i+=1
##
##    xfmt = mdates.DateFormatter('%Y-%m-%d H%:%M:%S')      
##    date_arr = np.loadtxt(date,
##                          delimiter=',',
##                          unpack=True)
##
##    date_arr = np.asarray(date)
##    dateconv = np.vectorize(dt.datetime.fromtimestamp)
##    datec = dateconv(date)
##
##    print(datec)

    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], high[x], low[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    candlestick_ohlc(ax1, ohlc[-start:], width=120, colorup = 'g', colordown='r')

    bbox_props = dict(boxstyle='round',fc='w', ec='k',lw=0.3, alpha = 0.4)
    ax1.annotate(str("%.4f" % closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1]+1000, closep[-1]), size=7, bbox=bbox_props)

##    ax3.plot(date[-start:], rsi5[-start:], linewidth=0.6, label = 'RSI')
##    ax3.plot(date[-start:], rsi15[-start:], linewidth=0.6, color = 'k')
##    ax3.axhline(90, color = 'r', linewidth=0.5)
##    ax3.axhline(10, color = 'r', linewidth=0.5)
##    ax3.axhline(70, color = 'b', linewidth=0.5)
##    ax3.axhline(30, color = 'b', linewidth=0.5)

    ax3.plot(date[-start:], atr[-start:], linewidth=0.6, label = 'ATR')
    
    ax2.plot(date[-start:], macd[-start:], linewidth=0.2, color = 'r')
    ax2.plot(date[-start:], macd_signal[-start:], linewidth=0.6, color = 'k')
    ax2.fill_between(date[-start:], macd[-start:], 0, alpha=0.2, facecolor= '#0079a3')
    ax2.axhline(0, color = 'k', linewidth=0.2)
    ax2.axhline(0.00017, color = 'r', linewidth=0.4)
    ax2.axhline(-0.00017, color = 'r', linewidth=0.4)

    
    ax1v.plot([],[], color = '#0079a3', alpha=0.2)       
    ax1v.fill_between(date[-start:], 0, volume[-start:], facecolor = '#0079a3', alpha = 0.2)
    

##    ax1cog.plot([],[], color = 'k', alpha = 0.9)  
##    ax1cog.plot(cog_date[-start:], cog[-start:], color = 'k', linewidth = 0.4, alpha = 0.9)

##    ax1.plot(dateBB[-start:], topBB[-start:], color = 'b',linewidth = 0.4, alpha = 0.9)
##    ax1.plot(dateBB[-start:], midBB[-start:], color = '#efdb21',linewidth = 0.6, alpha = 1)
##    ax1.plot(dateBB[-start:], botBB[-start:], color = 'k',linewidth = 0.4, alpha = 0.9)
##    ax1.plot(dateBB[-start:], topBB2[-start:], color = 'b',linewidth = 0.4, alpha = 0.9)
##    ax1.plot(dateBB[-start:], botBB2[-start:], color = 'k',linewidth = 0.4, alpha = 0.9)

    ax1.plot(date[-start:], top_line[-start:], color = 'r',linewidth = 0.5, alpha = 0.8)
    ax1.plot(date[-start:], mid_line[-start:], color = 'r',linewidth = 0.5, alpha = 0.8)
    ax1.plot(date[-start:], bot_line[-start:], color = 'r',linewidth = 0.5, alpha = 0.8)

##    ax1.plot(date[-start:], ema_s[-start:], color = 'g',linewidth = 0.5, alpha = 0.8)
    ax1.plot(date[-start:], sma[-start:], color = 'b',linewidth = 0.5, alpha = 0.8)

##    ax1midBB.plot([],[], color = 'b', alpha = 0.9) 
##    ax1midBB.plot(dateBB[-start:], midBB[-start:], color = 'k', linewidth = 0.4, alpha = 0.9)
##
##    ax1topBB.plot([],[], color = 'b', alpha = 0.9) 
##    ax1topBB.plot(dateBB[-start:], topBB[-start:], color = 'b', linewidth = 0.4, alpha = 0.9)
##
##    ax1botBB.plot([],[], color = 'b', alpha = 0.9) 
##    ax1botBB.plot(dateBB[-start:], botBB[-start:], color = 'r', linewidth = 0.4, alpha = 0.9)
    
##    ax1sma.plot([],[], color = '#1874cd', alpha = 0.9, label='SMA(30)')   
##    ax1sma.plot(date[-start:], sma[-start:], linewidth=0.6, color = '#1874cd', alpha = 0.9)
##    ax1ema_l.plot([],[], linewidth=0.6, color = '#ff4500', alpha = 0.9, label='EMA(15)')  
##    ax1ema_l.plot(date[-start:], ema_l[-start:], linewidth=0.6, color = '#ff4500', alpha = 0.9)
##    ax1ema_s.plot([],[], linewidth=0.6, color = '#9a32cd', alpha = 0.9, label='EMA(5)')  
##    ax1ema_s.plot(date[-start:], ema_s[-start:], linewidth=0.6, color = '#9a32cd', alpha = 0.9)

##    ax1.yaxis.set_minor_locator(minorLocator)
##    ax1.xaxis.set_minor_locator(minorLocator)
##    ax1.grid(which = 'minor')
##    ax1v.axes.yaxis.set_ticklabels([])
##    ax1v.axes.xaxis.set_ticklabels([])
##    ax1v.yaxis.set_ticks_position('none')
##    ax1v.grid(False)
##    ax1v.set_ylim(0, 1.5*max(volume))


##    ax1.axes.yaxis.set_ticklabels([])
    ax1.xaxis.set_minor_locator(minorLocator)
    ax1.yaxis.tick_right()
    ax1.grid(which = 'minor')
    
    ax2.xaxis.set_minor_locator(minorLocator)
    ax2.yaxis.tick_right()
    ax2.grid(which = 'minor')

    ax3.xaxis.set_minor_locator(minorLocator)
    ax3.yaxis.tick_right()
    ax3.grid(which = 'minor')

    ax1cog.axes.yaxis.set_ticklabels([])
    ax1cog.grid(False)
    
    ax1v.axes.yaxis.set_ticklabels([])
    ax1v.grid(False)
    ax1v.set_ylim(0, 1.5*max(volume))

    
##    ax1sma.axes.yaxis.set_ticklabels([])
##    ax1sma.grid(False)
##    ax1ema_l.axes.yaxis.set_ticklabels([])
##    ax1ema_l.grid(False)
##    ax1ema_s.axes.yaxis.set_ticklabels([])
##    ax1ema_s.grid(False)
    
##    ax3.plot(date[-start:], sma[-start:], linewidth=0.6, label = ('SMA(30)'))
##    ax3.plot(date[-start:], ema_l[-start:], linewidth=0.6, label = ('EMA(15)'))
##    ax3.plot(date[-start:], ema_s[-start:], linewidth=0.6, label = ('EMA(5)'))

##    for label in ax3.xaxis.get_ticklabels():
##        label.set_rotation(45)

##    ax3.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M:%S'))
    
##    plt.setp(ax1v.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, hspace=0.01)

##    ax2v.legend()
##    leg = ax2v.legend(loc=1, ncol=1, prop={'size':6})
##    leg.get_frame().set_alpha(0.4)
##    ax2sma.legend()
##    leg = ax2sma.legend(loc=2, ncol=1, prop={'size':6})
##    leg.get_frame().set_alpha(0.4)
##    ax2ema_l.legend()
##    leg = ax2ema_l.legend(loc=2, ncol=3, prop={'size':6})
##    leg.get_frame().set_alpha(0.4)
##    ax2ema_s.legend()
##    leg = ax2ema_s.legend(loc=2, ncol=3, prop={'size':6})
##    leg.get_frame().set_alpha(0.4)
##    ax3.legend()
##    leg = ax3.legend(ncol=2, prop={'size':6})
##    leg.get_frame().set_alpha(0.4)

    plt.show()
