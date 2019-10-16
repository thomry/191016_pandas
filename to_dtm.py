import pandas as pd
import os
from datetime import datetime

ebola = pd.read_csv('country_timeseries.csv')
ebola['date_dt'] = pd.to_datetime(ebola['Date'])

# 시간 형식 지정자(%d %m %y)와 /,-조합해 format 인자에 전달시 형식에 맞게 전달된 datetime object 얻는게 가능
test_df1 = pd.DataFrame({'order_day':['01/01/15','02/01/15','03/01/15']})
test_df1['date_dt1'] = pd.to_datetime(test_df1['order_day'], format='%d/%m/%y')
test_df1['date_dt2'] = pd.to_datetime(test_df1['order_day'], format='%m/%d/%y')
test_df1['date_dt3'] = pd.to_datetime(test_df1['order_day'], format='%y/%m/%d')
print(test_df1)

# strftime 메서드
now = datetime.now()
nowDate = now.strftime('%Y-%m-%d')
nowTime = now.strftime('%H:%M:%S')
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDate, nowTime, nowDatetime, sep='\t')