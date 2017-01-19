# coding=utf-8
import assetMgr
def getMean(priceArray, nDay):
    meanArray = []
    arraySize = len(priceArray)
    for index in range(len(priceArray)):
        sumCount = 0
        tmp = nDay
        
        for count in range (0, nDay):
            if (index + count) >= arraySize:
                break
            sumCount += priceArray[index + count]
            
        meanTmp = sumCount/nDay
        meanArray.append(meanTmp)
    return meanArray

def checkSell(now, short, mid, long):
    single = bool(0)

    singleTmp = (now < short) and (now < mid) and (now < long)
    single = single or singleTmp

    singleTmp = (now < short) and (now > mid) and (now < long)
    single = single or singleTmp

    singleTmp = (now < short) and (now < mid) and (now > long)
    single = single or singleTmp

    return single

def checkBuy(now, short, mid, long):
    single = bool(0)

    singleTmp = (now > short) and (now > mid) and (now > long)
    single = single or singleTmp

    singleTmp = (now > short) and (now > mid) and (now < long)
    single = single or singleTmp
    
    singleTmp = (now > short) and (now < mid) and (now > long)
    single = single or singleTmp
    
    return single

def calcMeanComplexe(priceArray):
    shortArray = getMean(priceArray, 5)
    midArray = getMean(priceArray, 30)
    longArray = getMean(priceArray, 60)


    assetSum = 10000*100
    initAsset = assetSum
    initPric = priceArray[0]
    # print "initPric " + str(initPric)
    cash = assetSum
    stockCount = 0

    for index in range(len(priceArray)):
        now = priceArray[index]
        short = shortArray[index]
        mid = midArray[index]
        long = longArray[index]

        buy = checkBuy(now, short, mid, long)
        if buy :
            cash, stockCount, assetSum = assetMgr.buyOperation(cash, stockCount, now)
            #print "buy "

        sell = checkSell(now, short, mid, long)  
        if sell:
            cash, stockCount, assetSum = assetMgr.sellOperation(cash, stockCount, now)

    asserInc = (assetSum *100)/ initAsset 
    priceInc = (priceArray[len(priceArray)-1] *100)/ initPric

    # print "asserInc " + str(asserInc) + "%"
    # print "priceInc " + str(priceInc) + "%"


    return (bool(asserInc > priceInc), (asserInc - priceInc) )

def calcMeanComplexe_today(priceArray):
    shortArray = getMean(priceArray, 5)
    midArray = getMean(priceArray, 30)
    longArray = getMean(priceArray, 60)

    todayIndex = 0
    now = priceArray[todayIndex]
    short = shortArray[todayIndex]
    mid = midArray[todayIndex]
    long = longArray[todayIndex]

    yestodayIndex = 1
    yes_now = priceArray[yestodayIndex]
    yes_short = shortArray[yestodayIndex]
    yes_mid = midArray[yestodayIndex]
    yes_long = longArray[yestodayIndex]

    butFlag = bool(0)
    buy = checkBuy(now, short, mid, long)
    yesBuy = checkBuy(yes_now, yes_short, yes_mid, yes_long)
    if buy and (yesBuy == 0) :
    # if buy:
        butFlag = bool(1)

    sellFlag = bool(0)  
    sell = checkSell(now, short, mid, long)  
    yesSell = checkSell(yes_now, yes_short, yes_mid, yes_long)
    if sell and (checkSell == 0):
    # if sell:
        sellFlag = bool(1)

    return (butFlag, sellFlag, now)