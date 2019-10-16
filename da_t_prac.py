from datetime import datetime

# now 메서드
now1 = datetime.now()
# today 메서드
now2 = datetime.today()
# 둘다 현재 시간 출력 가능

# 시간 직접 입력하여 인자에 전달
t1 = datetime(1970, 1, 1)
t2 = datetime(1970, 1, 1, 13, 24, 34)
print(t1, t2)

# datetime으로 시간계산하기
diff1 = t1 - t2
print(diff1)