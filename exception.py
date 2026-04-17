class NumberCheckError(Exception):
    def __init__(self,msg="error"):
        self.msg=msg
    def ___str__(self):
        return self.msg
    
try:
    number=int(input("숫자를 입력하라"))
    if number <0:
        raise NumberCheckError("0보다 작다")
    
except NumberCheckError as e:
    print(e)