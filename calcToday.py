# coding=utf-8
import tushare as ts
import strategy
import sendEmail

def checkToday():
    try:
        basic = ts.get_stock_basics()
    except:
        print "get_stock_basics err"
        return -1

    winCount = 0
    lostCount = 0
    sum = 0
    mean = 0
    buy = bool(0)
    sell = bool(0)

    stockPool = ["600816", "600309", "600196", "600535", "600519", "600674", "002053"]


    buyInfo = ""
    sellInfo = ""
    today = ""
    for stock in stockPool:
        stockName = (basic['name'][basic.index==stock])[0]
        print "\n start " + stockName + "\n"
        try:
            df = ts.get_h_data(stock, start='2015-01-01')
            today = df.index[0]
        except:
            continue

        if df is None:
            continue
        price = 0
        buy, sell, price = strategy.calcMeanComplexe_today(df["close"])
        if buy:
            buyInfo += "    " + stockName +"    " + str(today) +" buy,  price = " + str(price) + "\n"
        if sell:
            sellInfo += "   " + stockName +"    " + str(today) +" sell, price = " + str(price) + "\n"

    emailText = "今天的投资建议\n"
    emailText += "【买入】\n"
    emailText +=  buyInfo
    emailText += "【卖出】\n"
    emailText +=  sellInfo
    print emailText
    sendEmail.sendMailToMe_quantDaily(emailText)
    return 0