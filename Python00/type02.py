# 문자 (single quotation / double quotation 의 차이 없음)

# single * 1 : 기본형
a = 'Hello, Python!'
print('a는 '+ a)

# single * 3 : 엔터도 인식된다
b = '''python's
    Hello, World!        !!!!
    Hello, Python'''
print('b는 ' + b)

a = 'python\'s\nHello, World!'
print(a)

# \ : escape character

# double * 1
c = "python's\nHello, World!"
print('c-1는 ' + c)

c = "python's\nHello, \"World!\""
print('c-2는 ' + c)

# double * 3
d = """python's
"Hello, World!" """
print('d는 ' + d)

e = "c:\test"
print('e는 ' + e) #\t는 탭!

# r = raw string : \를 문자로 인식
f = r"c:\test"
print('f는 ' + f)

str01 = "Hello, "
str02 = "World!"
print('str01+str02 = ' + str01 + str02)
print('str01 * 3 + str02 = ' + str01 * 3 + str02)

