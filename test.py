# coding=utf-8
import tushare as ts
import strategy

basic = ts.get_stock_basics()

winCount = 0
lostCount = 0
sum = 0
mean = 0


for stock in basic.index:
    print stock
    try:
        df = ts.get_h_data(stock, start='2016-01-01')
    except:
        print "[err] get_h_data err"
        continue

    if df is None:
        print "[err] df is None"
        continue

    ok, inc = strategy.calcMeanComplexe(df["close"])
    print ""
    if ok :
        winCount += 1
        print "[win] inc = " + str(inc) + " winCount = " + str(winCount) + " lostCount = " + str(lostCount) + " sum = " + str(sum)
    else :
        lostCount += 1
        print "[lost] inc = " + str(inc) + " winCount = " + str(winCount) + " lostCount = " + str(lostCount) + " sum = " + str(sum)

    sum += inc
# mean = sum / (winCount + lostCount)
# print "winCount = " + str(winCount)
# print "lostCount = " + str(lostCount)
# print "EV = " + str(mean)

#mean = sum / (winCount + lostCount)

        
    
# for stock in basic:
    
#     print stock
#      break
# df = ts.get_h_data("600000")
# strategy.calcMeanComplexe(df["close"])
# for col in df.columns:
#     print col
#     break