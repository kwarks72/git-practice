# [1] 쓰기 작업 (Write)
f = open("새파일.txt", "w", encoding="UTF-8")
for i in range(1, 11):
    data = "%d 번째 줄입니다\n" % i
    f.write(data)
f.close()  # 중요: 여기서 파일을 닫아야 하드디스크에 완전히 저장됩니다.

# [2] 읽기 작업 (Read)
f = open("새파일.txt", "r", encoding="UTF-8") # 'r' 모드로 다시 열기
content = f.read()
print(content)
f.close()
