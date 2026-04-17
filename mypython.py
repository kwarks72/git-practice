


scores=[85,42,91,67,55,78]

print("70점 미만 점수들:")

for s in filter(lambda x:x<70, scores):
    print(s)