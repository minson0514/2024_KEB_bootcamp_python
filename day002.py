money = 5,000,000
print(money)
print(type(money)) #class tuple

cash = 5_000_000
print(cash)
print(type(cash)) #class int

base_number = int(input('Input base number : '))
exponent_number = int(input('Input base number : '))
print(type(base_number),type(exponent_number))
#f string: 문자열 포매팅
# **: 거듭제곱
#print(f'밑은 {base_number}, 지수는{exponent_number}, 결과값은 {base_number**exponent_number}')
#중괄호 안에는 바뀔 수 있는 값이 들어감
#pow함수
#print(f'밑은 {base_number}, 지수는 {exponent_number}, 결과값은 {pow(base_number,exponent_number)}')

#format function
#print('밑은 {0}, 지수는{1}, 결과값은 {2}'. format(base_number,exponent_number,pow(base_number,exponent_number)))
#print('밑은 {}, 지수는{}, 결과값은 {}'. format(base_number,exponent_number,pow(base_number,exponent_number)))

#c like c언어랑 비슷하게 하는 방법
#print('밑은 %d, 지수는 %d, 결과값은 %d' %(base_number,exponent_number,pow(base_number,exponent_number)))

