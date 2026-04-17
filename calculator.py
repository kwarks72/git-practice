import numpy as np

mid=np.array([15,100,45])
final= np.array([78,25,90])
term= np.array([81,45,99])

total = 0.4*mid+0.4*final+0.2*term+5
print("각 학생의 점수:", total)


print("중간고사 평균:", mid.mean())
print("중간고사 표준표차", mid.std())
print("철수의 최종점수", total[0])
