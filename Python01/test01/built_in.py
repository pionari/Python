# -*- coding:utf-8 -*-

# int() : 정수
print(int(12.34))
print(int('56'))
print(int(True))
print(int(False))
# 값이 있으면 True, 있으면 False

# 2진수, 8진수, 16진수
print(int('1111',2))
print(int('77',8))
print(int('ff',16))

# float() : 실수
print(float('3'))
print(float(3.3))

# str() : 문자열
a = 10
#print("a : " + a) a가 int형이라서 오류
print("a : " + str(a)) #a가 문자열로 바뀔거니까 이제는 출력이 잘 된다.

b = "hobby"
print(b.count('b')) # 입력한 문자의 총 개수
print(b.find('b')) # 입력한 문자가 있으면 첫번째 인덱스 값, 없으면 -1 출력

c = "    hi    "
print(c.strip()) # 공백 삭제

