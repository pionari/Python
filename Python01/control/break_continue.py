i = 1

while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else:
    print('i', i, sep='=')
# sep='구분자' : 구분자에 의해 띄어쓰기 후 출력
print()


for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('i',i,sep='=')

###############
# while의 실행 결과 : 1 2 3 4 5
# for의 실행 결과 : 1 3 5 7 9 i=10
