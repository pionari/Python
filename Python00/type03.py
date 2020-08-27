# list : []대괄호 사용. 계속 추가 가능

# 생성자 사용
a = list()
print(a)
a.append(1)
print(a)
a.append('a')
print(a)
a[0] = 3
print(a)
#a[2] = 5
#print(a)
a.append(3)
print(a)
# 추가할 때는 append. 늘어나긴 하지만 자동 추가는 안 된다.

#[] 사용
b = [1,2,3,4,5]
print(b)

# b 안에 있는 숫자 2와 4를 더해서 출력
print(b[1] + b[3])

# 역정렬
b.reverse()
print(b)

# 정렬
b.sort() 
print(b)

# 리스트 안에 리스트를 무한으로 넣을 수 있다
c = ['a','b','c','d',['e','f','g'],'h']
print(c[4])

d = b + c
print(d)

# 리스트끼리 연산도 가능
print(c + b)
