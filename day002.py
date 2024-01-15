#섭씨 화씨 간 변환
'''
menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit : ")

if menu == '1':
    fahrenheit =float(input("input Fahrenheit : "))
    print('Fahrenheit : %f F, Celsius : %.4f C' %(fahrenheit,(fahrenheit-32.0)*5.0/9.0))
elif menu == '2':
    celsius = float(input("input Celsius : "))
    print(f'Celsius {celsius}C, Fahrenheit {((celsius*9.0/5.0)+32.0): .4f}F')
'''

#줄 바꿀 때 역슬래쉬 사용
'''
sum = 1 + \
    + 2\
    +3
print(sum)
'''

#if elif else
# temp =[0]
# temp = []
# if temp:
#     print("원소가 존재하는 리스트")
# else:
#     print("비어있는 리스트")

letter = 'k'
vowels = {'a','e','i','o','u'} #set
#vowels ="aeiuo" #str
print(type(vowels))
if letter in vowels:
    print(f'{letter} is vowel~')
else:
    print(f'{letter} is consonant~')