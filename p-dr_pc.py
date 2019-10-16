import pandas as pd
import pandas_datareader as pdr

pd.core.common.is_list_like = pd.api.types.is_list_like

# 데이터프레임 저장
# www.quandl.com에 가입하여 api_key받기
tesla = pdr.get_data_quandl('TSLA', api_key = '받은 키 입력~')
# dataframe을 파일로 저장
tesla.to_csv('tesla_stock_quandl.csv')

# date열을 datetime형으로 변환
tesla = pd.read_csv('tesla_stock_quandl.csv', parse_dates=[0])
# date열을 tesla dataframe의 인덱스로 저장
tesla.index = tesla['Date']
# 예시로 2015년의 데이터 추출
print(tesla['2015'].iloc[:5, :5])
# data열의 최솟값을 빼서 데이터 수집이후 시간흘렀는지 확인해보기
# 그 시간을 ref_date열로 추가
tesla['ref_date'] = tesla['Date'] - tesla['Date'].min()
# ref_date열을 인덱스로 지정해서 최초 5일의 데이터 추출
tesla.index = tesla['ref_date']
print(tesla['5 days':].iloc[:5, :5])