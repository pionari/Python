# tuple : list와 거의 같다. 튜플은 () 소괄호. 추가, 삭제, 수정 불가능. 길이도 값도 고정.

# 생성자 사용
a = tuple()
print(a)
#a.append(1)
#print(a)
#b = tuple(1, 2, 3, 4)
#print(b)
b = tuple([1, 2, 3, 4])
print(b)

# 리스트 안에 튜플 추가
list_b = list(b)
print(list_b)

list_b.append(5)
print(list_b)

# () 사용
c = (1, 2, '3')
print(c)

# tuple + tuple
d = b + c
print(d)

# unpacking ( 이거 잘 쓰면 우와~ 함)
e = (1, 2, 3, 4)
f, g, h, i = e
print(f)
print(g)
print(h)
print(i)
