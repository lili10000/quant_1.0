# coding=utf-8
import tushare as ts
import strategy
import sendEmail

def testStrategy():
    try:
        basic = ts.get_stock_basics()
    except:
        print "get_stock_basics err"
        stock_basic_info.csv
        return -1

    winCount = 0
    lostCount = 0
    sum = 0
    mean = 0

    for stock in basic.index:
        print "\nstaty " + stock +"\n"
        try:
            df = ts.get_h_data(stock, start='2015-01-01')
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

    mean = sum / (winCount + lostCount)
    result = "winCount = " + str(winCount) + "\n"
    result += "lostCount = " + str(lostCount) + "\n"
    result += "sumCount = " + str(lostCount + winCount) + "\n"
    result += "EV = " + str(mean) + "\n"

    sendEmail.sendMailToMe_comm("量化策略分析",result)
    return 0