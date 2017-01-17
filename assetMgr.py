# coding=utf-8

def buyOperation(cash, stockCount, price):
    buyCount = cash % (price *100)
    stockCount += buyCount
    cash -= buyCount*price
    sum = cash + price*stockCount
    return (cash, stockCount, sum)

def sellOperation(cash, stockCount, price):
    sellCount = stockCount
    stockCount -= sellCount
    cash += sellCount*price
    sum = cash + price*stockCount
    return (cash, stockCount, sum)