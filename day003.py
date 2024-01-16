'''
total = 0
num=[1,2,3]
i=0
while i<3:
    total=total+num[i]
    i=i+1
print(total)
'''

#소수인지 아닌지 판정하는 프로그램
#prime number
number = int(input("input num: "))
cnt = 0 #counter variable
i = 1
while i <= number:
    if number % i == 0:
        cnt += 1
    i+=1
if cnt == 2:
    print("%d is prime number"%number)
else:
    print("%d is NOT prime nuber" %number)

'''
while True:
    value = input('enter integer, press [q] to quit: ')
    if value == 'q':
        break
'''