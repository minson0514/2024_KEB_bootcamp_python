#sequence type 자료형: 순서를 가진 자료형
#cf 튜플 딕셔너리 리스트 등
'''
univ = "inha"
i = 0
while i < len(univ):
    print(univ[i], end=' ') #end는 줄바꿈 대신 띄어쓰기
    i+=1
'''

univ = "inha"
#side effect가 발생할 수 있는 코드
#특정 구간만 출력하고 싶을 때는 이 방식을 사용해야함
i = 0
while i < len(univ):
    print(univ[i], end=' ') #end는 줄바꿈 대신 띄어쓰기
    i+=1
print("\n")

#내부적으로 알아서 동작하는 코드 더 안전함
#side effect 없음 전체 문장 출력 하는 데에 최적화
for letter in univ:
    print(letter, end=' ')
print("\n")

#for문에서 range를 쓰면 구간 지정해서 출력 가능
for k in range(0,len(univ), 1): #0부터 univ변수의 문자열 길이까지 1간격으로
    print(univ[k], end = ' ')
print("\n")

#range 기본 시작값이 0이고 step의 기본값이 1
for k in range(len(univ)): #0부터 univ변수의 문자열 길이까지 1간격으로
    print(univ[k], end = ' ')

#cancel with break
