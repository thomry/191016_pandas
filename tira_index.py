import pandas as pd
import matplotlib.pyplot as plt

ebola = pd.read_csv('country_timeseries.csv', parse_dates=[0])
# 데이터 누락없이 데이터 추출하는 법
head_range = pd.date_range(start='2014-12-31', end='2015-01-05')
# freq 인잣값. 여러 인잣값이 있으니 확인해보고 사용하기
# EX) 평일만 포함시키기
print(pd.date_range('2017-01-01', '2017-01-07', freq='B'))

# ebola dataframe date열을 index로 지정후 x축을 date열로, y축을 사망자 수로 지정해 그래프그리기
ebola.index = ebola['Date']
fig, ax = plt.subplots()
ax = ebola.iloc[0:, 1:].plot(ax=ax)
ax.legend(fontsize = 7, loc=2, borderaxespad=0.)
plt.show()

# 앞 그래프는 나라마다 ebola 발병일이 다르므로 동일 위치로 옮겨서 다시 비교하기
ebola_sub = ebola[['Day', 'Cases_Guinea', 'Cases_Liberia']]
# 날짜가 없는 데이터를 포함시키기
ebola = pd.read_csv('country_timeseries.csv', parse_dates=['Date'])
ebola.index = ebola['Date']
# date열의 최댓값과 최솟값으로 시간 범위를 생성하여 new_idx에 저장
new_idx = pd.date_range(ebola.index.min(), ebola.index.max())
# 시간 순서 맞추기
new_idx = reversed(new_idx)
# reindex 사용해 new_idx을 새로운 인덱스로 지정
ebola = ebola.reindex(new_idx)
# 가장 오래된 데이터랑 최근 데이터 가져오기
last_vaild  = ebola.apply(pd.Series.last_valid_index)
first_vaild = ebola.apply(pd.Series.first_valid_index)
# 가장 처음 발병한 날에서 각 나라의 에볼라 발병일을 빼서 동일한 출발선으로 옮기기
earliest_date = ebola.index.min()
shift_values = last_vaild - earliest_date
print(shift_values)
# 각나라의 에볼라 발병일 옮기기
# shift 메서드는 인잣값 만큼 데이터 밀어내는 메서드
ebola_dict = {}
for idx, col in enumerate(ebola):
    d               = shift_values[idx].days
    shifted         = ebola[col].shift(d)
    ebola_dict[col] = shifted
# ebola_dict dataframe으로 변환
ebola_shift = pd.DataFrame(ebola_dict)
# index를 day열로 지정
ebola_shift.index = ebola_dict['Day']
# 필요없는 date, day열 삭제
ebola_shift       = ebola_shift.drop(['Date', 'Day'], axis=1)

fig, ax = plt.subplots()
ax      = ebola_shift.iloc[:, :].plot(ax=ax)
ax.legend(fontsize = 7, loc=2, borderaxespad=0.)
plt.show()