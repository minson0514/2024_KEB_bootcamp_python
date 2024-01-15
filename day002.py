'''
first = int(input("First number : "))
second = int(input("Second number : "))

print(f'몫은 {divmod(first,second)[1]}, 나머지는 {divmod(first,second)[1]}입니다.')

'''
'''
first = int(input("First number : "))
second = int(input("Second number : "))

quotient = first // second
remainder = first % second
print(f'몫은 {quotient}, 나머지는 {remainder}입니다.')
'''

#print(0b10) #2 -> 알아서 10진수로 바꿔서 출력해줌
#앞에 0이 붙으면 2진수로, 0o, 0O가 붙으면 8진수로 바꿔서 출력해줌
'''
dec = 65
octal = 0o101
hexadecimal = 0x41
binary = 0b01000001
print(dec,octal,hexadecimal,binary) #4개 다 65가 출력됨
#chr ord 아스키코드와 문자 변환하는 예약어
#bin binary값으로 변환하는 예약어
print(chr(dec),chr(octal),chr(hexadecimal),chr(binary)) #4개 다 65가 출력됨
print(ord('B'),ord('Z'),ord('a'),ord('2'))
print(bin(dec),bin(octal),bin(hexadecimal),bin(binary))
'''



