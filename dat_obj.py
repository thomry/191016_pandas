import pandas as pd
import matplotlib.pyplot as plt

ebola = pd.read_csv('country_timeseries.csv')
ebola['date_dt'] = pd.to_datetime(ebola['Date'])

date_series = pd.Series(['2018-05-16', '2018-05-17', '2018-05-18'])
d1          = pd.to_datetime(date_series)
# year, month, day 속성을 이용하여 년, 월, 일 정보 바로 추출
print(d1[0].year, d1[0].month, d1[0].day)
# index가 아닌 열에 접근해서 연도값 추출
ebola['year'] = ebola['date_dt'].dt.year
print(ebola[['Date', 'date_dt', 'year']].head())
# 위 응용
ebola['month'], ebola['day'] = (ebola['date_dt'].dt.month, ebola['date_dt'].dt.day)
print(ebola[['Date', 'date_dt', 'year', 'month', 'day']].head())

# min 메서드 사용해 ebola 최초 발병일을 찾기
print(ebola['date_dt'].min())

# 파산한 은행 데이터 집합을 불러 year, quarter 속성이용해 파산 연도, 분기 추가
banks  = pd.read_csv('banklist.csv')
banks['Closing Date']    = pd.to_datetime(banks['Closing Date'])
banks['closing_quarter'] = banks['Closing Date'].dt.quarter
banks['closing_year']    = banks['Closing Date'].dt.year
print(banks.head())

# groupby 메서드를 사용해 연도별, 분기별로 파산한 은행 개수 알아보기
closing_year = banks.groupby(['closing_year', 'closing_quarter']).size()
# print(closing_year)
# 이대로 그래프 그리기
fig, ax = plt.subplots()
ax = closing_year.plot()
plt.show()


