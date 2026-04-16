 
# txt=input("저장할 내용을 입력하세요")

# with open("test2.txt","a") as file:
#     file.write(txt+"\n")
with open("test.txt", "r") as file:
    content = file.read()

content = content.replace("java", "python")

with open("test.txt", "w") as file:
    file.write(content)