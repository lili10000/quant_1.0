# coding=utf-8
import tushare as ts

basic = ts.get_stock_basics()
print(type(basic))
print basic.index

print basic.columns
for col in basic.columns:
    for stock in basic.index:
        #print stock
        df = ts.get_h_data("600000", start='2015-01-01')
        df.to_csv("test.csv")
        #print stock
        # print basic[col][stock]
        break
    break
# for stock in basic:
    
#     print stock
#     break
