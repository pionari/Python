subject = ['java','javascript','python']

for i in subject:
    print(i, end=' ') # end= ' ' == println
else:
    print('재밌다.')

for i in range(1, 100):
    print(i, end='+')

print('\n구구단')

for i in range(2,10):
    print('<<'+str(i)+'단>>')
    for j in range(1,10):
        #print(str(i) + ' * ' + str(j) + ' = ' + str(i * j))
        #print(str(i), '*',str(j),'=', str(i*j))
        #print(i, '*', str(j), '=', str(i*j), sep='   ')
        print('{} * {} = {}'.format(i, j, i * j))

for i in range(10, 0, -1):
    print(i, end='')

mysum = 0
mycnt = 1
while mycnt <= 10:
    mysum += mycnt
    mycnt += 1
else :
    print('sum',mysum, sep='=')
    print('cnt',mycnt, sep='=')
    # python 에는 ++, --가 없다!!


