#raw string
''''
university = r"Inha \n university!"#Inha \n university!
print(university)#특수기호 자체를 보여줌
'''

#문자열에서 + 쓰면 문자열끼리 붙여줌
'''
num1= input("enter first number : ")#str형
num2= input("enter second number : ")
print(num1+num2) #concatenation때문에 문자열끼리 결합함
print(num1*3) #duplicate
print(num1+3) #문자열과 숫자 사이에 산술연산자를 넣어서 error발생
'''
#역방향인덱싱
'''
letters = ("abcdefghijklmnopqrstuvwxyz")
print(letters[-1]) #역방향 인덱싱 z
'''

#get a substring with a slice
#[:] 슬라이싱
'''
university ="Inha\nuniversity!" #\n은 한 글자로 침
print(university[:4]) #inha
print(university[:-11]) #" 처음부터 -11까지, 역방향 인덱싱
print(university[:])
print(len(university)) #문자열 길이 리턴
#16글자고 0부터 시작이니까 마지막 y는 15번
print((university[::1])) #처음부터 끝까지 1 간격으로 리턴
'''