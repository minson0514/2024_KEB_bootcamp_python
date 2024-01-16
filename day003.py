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
#prime number: 1과 자기 자신 외에는 나누어 떨어지지 않음
'''
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

#좀 더 논리적
'''
number = int(input("input num: "))
cnt = 0 #counter variable
i = 2 #2부터 나눔
while i < number: #자기 자신 제외
    if number % i == 0:
        cnt += 1
    i+=1
if cnt == 0: #한번도 나누어 떨어지지 않으면 소수
    print("%d is prime number"%number)
else:
    print("%d is NOT prime nuber" %number)
'''

#성능 이슈 해결
number = int(input("input num: "))
is_prime = True #int type-> boolean
if number <= 1: #1이 소수가 아니니까 해당 코드 추가
    print("%d is NOT prime nuber" % number)
else:

    i = 2 #2부터 나눔
    while i < number: #자기 자신 제외
        if number % i == 0:
            is_prime = False #remove +
            break #약수가 한번이라도 발생하면 루프 탈출
            #number=111 일 때 3번까지 돌고 break
        i += 1
    if is_prime: #remove ==
        print("%d is prime number"%number)
    else:
        print("%d is NOT prime nuber" %number)