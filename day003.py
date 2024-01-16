#성능 이슈 해결
'''
number = int(input("input num: "))
is_prime = True #int type-> boolean
if number <= 1: #1이 소수가 아니니까 해당 코드 추가
    print("%d is NOT prime nuber" % number)
else:
    for i in range(2,number): #이부분 수정함
        if number % i == 0:
            is_prime = False #remove +
            break #약수가 한번이라도 발생하면 루프 탈출
            #number=111 일 때 3번까지 돌고 break
        i += 1
    if is_prime: #remove ==
        print("%d is prime number"%number)
    else:
        print("%d is NOT prime nuber" %number)
'''

#range is the generater
'''
print(range(3,9))#range(3, 9)
print(list(range(3,9)))#[3, 4, 5, 6, 7, 8]
print(tuple(range(3,9)))#(3, 4, 5, 6, 7, 8)
#generater: 그때 그때 숫자 발생 시키고 그 전 것은 삭제
#-> 속도를 위해서 발생 시키고 사용 하고 삭제함
#-> 메모리 공간을 효율적으로 사용
#tuple data structure: read only -> cannot be popped
'''
'''
numbers = input("input first second number : ").split()
#input two nums and split them
#data type -> list (it has two components)
n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2: #non temporary variable
    n1, n2 = n2, n1 #unpacking
for number in range(n1,n2+1): #from n1 ~ to n2+1
    is_prime = True #reset
    if number <= 1:
        pass #just pass doin nothin
    else:
        for i in range(2,number):
            if number % i == 0:
                is_prime = False
                break #escape ^for^
        if is_prime: print(number, end=' ')
'''
