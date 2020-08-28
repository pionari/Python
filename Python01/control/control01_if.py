# if ~ else
a = 1

# python 의 들여쓰기 : space 2, space 4, tab 1 (space 4를 권장)
if a == 1:
    print('a == 1')
else :
    print('a != 1')
    
# 조건부 표현식 (3항 연산자와 비슷)
score=70
message = "success" if score >= 60 else "failure"
print(message)

# if elif else
b = 2

if b == 1:
    print('b == 1')
elif b == 2:
    print('b == 2')
else:
    print('b != 1 & b != 2')
