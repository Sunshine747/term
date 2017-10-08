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

    diviation = np.absolute(diviation)
    diviation.sort()
 
    width_v = diviation[round(len(diviation)*(width/100))] + 0.0000001

    i = 0
    while i < len(sma_v)-1:
        top_line.append(sma_v[i] + width_v)
        bot_line.append(sma_v[i] - width_v)
        i += 1

    return top_line, sma_v, bot_line

def atr(period, closep, highp, lowp):
    start = len(closep[30-1:])
    dates = []
    atr = []
    
    x = h - l
    y = abs(h - yc)
    z = abs(l - yc)

    if y <= x >= z:
        atr = x
    elif x <= y >= z:
        atr = y
    elif x <= z >= y:
        atr = z

    return atr, date
    
