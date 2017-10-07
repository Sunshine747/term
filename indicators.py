import numpy as np

def sma(charts, period):
    weights = np.repeat(1.0, period)/period
    smas = np.convolve(charts, weights, 'valid')
    return smas

def ema(charts, period):
    weights = np.exp(np.linspace(-1.,0.,period))
    weights /= weights.sum()
    ema = np.convolve(charts, weights) [:len(charts)]
    ema[:period]=ema[period]
    return ema

def rsi(charts, period):
    deltas = np.diff(charts)
    seed = deltas[:period+1]
    up = seed[seed>=0].sum()/period
    down = -seed[seed<0].sum()/period
    rs = up/down
    rsi = np.zeros_like(charts)
    rsi[:period] = 100. - 100./(1.+rs)

    for i in range(period, len(charts)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(period-1) + upval)/period
        down = (down*(period-1) + downval)/period

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi

def macd(charts, s_period, l_period):
    emaslow = ema(charts, l_period)
    emafast = ema(charts, s_period)
    macd = (emafast - emaslow)
    macd_signal = sma(macd, 6)
    return macd, macd_signal

def standart_deviation(period, charts, dates):
    sd =[]
    sddate = []
    x = period
    while x <= len(charts):
        array2consider = np.array(charts[x-period:x])
        standdev = array2consider.std()
        sd.append(standdev)
        sddate.append(dates[x])
        x += 1
    return sddate, sd

def bb(mult, mult2, period, charts, dates):
    bdate =     []
    topBand =   []
    botBand =   []
    topBand2 =  []
    botBand2 =  []
    midBand =   []

    x = period
    while x < len(dates):
        curSMA = sma(charts[x-period:x], period)[-1]

        d, curSD, = standart_deviation(period, charts[0:period], dates)
        curSD = curSD[-1]

        TB = curSMA + (curSD*mult)
        BB = curSMA - (curSD*mult)
        TB2 = curSMA + (curSD*mult2)
        BB2 = curSMA - (curSD*mult2)
        D = dates[x]

        bdate.append(D)
        topBand.append(TB)
        botBand.append(BB)
        topBand2.append(TB2)
        botBand2.append(BB2)
        midBand.append(curSMA)
        x += 1
    return bdate, topBand, botBand, topBand2, botBand2, midBand

def cog(dates, charts, period):
    COG = []
    x = period

    while x < len(dates):
        consider = charts[x-period:x]

        multipliers = range(1, period+1)

        topFrac = 0
        botFrac = 0

        reversedOrder = reversed(consider)

        ordered = []
        for eachItem in reversedOrder:
            ordered.append(eachItem)

        for eachM in multipliers:
            addMe = (eachM*ordered[eachM-1])
            addMe2 = ordered[eachM-1]
            topFrac+=addMe
            botFrac+=addMe2

        CeOfGr = -(topFrac/float(botFrac))

        COG.append(CeOfGr)

        x+=1

    return dates[period:], COG

def myind(charts, period, width):
    start = len(charts[30-1:])
    width_v = 0
    diviation = []
    top_line = []
    mid_line = []
    bot_line = []
    sma_v = sma(charts, period)

    a = np.array(charts[-start:])
    b = np.array(sma_v[-start:])
    diviation = (a - b)

##    print(diviation)
    diviation = np.absolute(diviation)
##    print(diviation)
    
    
##    print(len(a))
##    print(len(b))
##    print(len(diviation))
        
##    i = len(a)-1
##    while i > 0:
##        print(a[i])
##        print(b[i])
##        print(diviation[i])
##        print()
##        input()
##        i -= 1
        
##    for i in sma_v:
##        for j in charts:
##            dif = (j - i)
##            print(i)
##            print(j)
##            print(dif)
##            input()
##            if dif < 0:
##                diviation.append(dif*(-1))
##            else:
##                diviation.append(dif)
##
##            dif = 0
##    print(1)
##    print(diviation)
    diviation.sort()
    print(diviation)

    print(round(len(diviation)*(width/100)))
    print(diviation[round(len(diviation)*(width/100))])
    print(diviation[round(len(diviation)*(width/100))+1])
    print(diviation[round(len(diviation)*(width/100))-1])
    

    width_v = diviation[round(len(diviation)*(width/100))] + 0.0000001
    print(width_v)
    print(diviation[round(len(diviation)*(width/100))])

##    top_line = [x + width_v for x in b]
##    bot_line = [z - width_v for z in b]
##    top_line = b + width_v
##    bot_line = b - width_v

    i = 0
    while i < len(sma_v)-1:
        top_line.append(sma_v[i] + width_v)
        bot_line.append(sma_v[i] - width_v)
##        print(top_line[i])
##        print(top_line[i] - sma_v[i])
##        print()
##        print(sma_v[i])
##        print()
##        print(sma_v[i] + width_v)
##        print((sma_v[i] + width_v)- sma_v[i])
##        print()
##        print(bot_line[i])
##        print(bot_line[i] - sma_v[i])
##        print()
##        input()
        i += 1

##    i = len(sma_v)-1
##    while i > 0:
##        top_line.append(sma_v[i] + width_v)
##        bot_line.append(sma_v[i] - width_v)
##        print(top_line[i])
##        print(top_line[i] - sma_v[i])
##        print()
##        print(sma_v[i])
##        print()
##        print(sma_v[i] + width_v)
##        print((sma_v[i] + width_v)- sma_v[i])
##        print()
####        print(bot_line[i])
####        print(bot_line[i] - sma_v[i])
####        print()
##        input()
##        i -= 1

##    for i in sma_v:
##        top_line.append(sma_v[i] + width_v)
##        bot_line.append(sma_v[i] - width_v)

    return top_line, sma_v, bot_line
