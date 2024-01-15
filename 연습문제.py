#3장 연습문제 1
'''
hour = int(input("enter hour: "))
second = hour * 3600
print("%d 시간은 %d 초 입니다." %(hour, second))
'''

#3장 연습문제 3
'''
seconds_per_hour = 1*60*60
seconds_per_day = seconds_per_hour * 24
print(seconds_per_day / seconds_per_hour) #3.5번문제
# -> 24.0 부동소숫점 나눗셈
print(seconds_per_day // seconds_per_hour) #3.6번문제
# -> 24 정수 나눗셈
'''

#4장 연습문제
#4.1
'''
secret = 1
guess = 8
if secret > guess:
    print("too low")
elif secret == guess:
    print("just right")
else:
    print("too high")
'''
#4.2
'''
small = False #false 라고 쓰면 틀리고 대문자를 써야함
green = True
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumkin")
'''

#주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력 해보자
'''
pin="010101-3456789"
print(pin[7])
'''

#홍길동씨의 주민등록번호는 881120-1068234이다. 홍길동씨의 주민등록번호를 연월일 부분과 그 뒤의 숫자 부분으로 나누어 출력해보자
'''
pin= "881120-1068234"
yyyymmdd = pin[0:6]
num=pin[7:]
print(yyyymmdd)
print(num)
'''

#예제: f문자열 포매팅
'''
name="홍길동"
age=30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")
'''
'''
y=3.141592
print(f'{y:0.4f}') #소수점 4자리까지만 표현
'''

#문자열 관련 함수
'''
#객체/변수+ '.' + 함수
a="python is the best choice"
print(a.count('b')) #문자 개수 세기
print(a.find('b')) #특정 문자가 처음 나오는 위치 알려주기 (찾는 문자가 없을 경우 -1 반환)
print(a.index('b')) #특정 문자가 처음 나오는 위치 알려주기 (찾는 문자가 없을 경우 오류 발생)

print(",".join('abcd')) #문자열 삽입
print(a.upper()) #소문자를 대문자로 바꾸는 함수
print(a.lower()) #대문자를 소문자로 바꾸는 함수

b="life is too short"
print(b.replace("Life","Your leg"))#문자열 바꾸기
print(b.split())#문자열 나누기
#()-> 공백 기준으로 나누기, 괄호 안에 기호 넣으면 -> 특정 기호 기준으로 나누기
'''

#다음과 같은 문자열  a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자
'''
a = "a:b:c:d"
b = a.replace(":","#")
print(b)
'''