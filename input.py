# #국어 80  #영어 75  수학=55 평균 점수를 구해라

# korean =80
# english= 75
# mathmetics = 55
# sum= korean+english+mathmetics
# average= sum/3
# print("홍길동의 평균점수는" , average)

#자연수 13이 홀수인지 짝수인지 판별해라 
#2로 나누어서 0이면 짝수 2로 안 나뉘면 홀수
thirteen=13
residue= thirteen %2
print("13의 나머지는", residue)
if residue == 1:
    print("나머지가 1이므로 홀수다")
else:
    print("나머지가 2이므로 짝수다")