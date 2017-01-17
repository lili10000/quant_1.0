# coding=utf-8
import assetMgr
def getMean(priceArray, nDay):
    sumCount = 0
    meanArray = []
    for index in range(len(priceArray)):
        sumCount += priceArray[index]
        if index > nDay:
            sumCount -= priceArray[index-nDay]

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