# dictionary : 연관 배열 (또는 Hash) key를 통해 value를 얻는다

# 생성자 사용
dict01 = dict()

dict01[1] = 'one'
dict01['two'] = 2
print(dict01)

# {} 사용
dict02 = {}
dict02['one'] = 1
dict02[2] = 'two'
dict02[3] = 3
print(dict02)

# key를 통해 value값 가져와보자
print(dict01.get(1))
print(dict02['one'])

# key값만 가져오기
print(dict02.keys())

# dict03의 value를 list에 추가하고 1번째 인덱스 값을 출력
print(list(dict02.values())[1])
