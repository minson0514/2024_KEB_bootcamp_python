#앞에 is 가 붙은 함수는 true false를 리턴함
'''
subjects = "python c++ database linux"
print(subjects.isalnum()) #자주쓰는 함수는 아님
subject = input("수강신청과목 입력 : ")

try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스 입니다.")
#try에서 예외가 생기면 valueerror 가 실행됨
except ValueError:
    print(f'해당 과목이 존재하지 않습니다.')
'''

#print('%e' %0.7045)

#default 매개변수
#format함수 안에 디폴트 매개변수를 줌
#cf 'the {thing} is in the {place}'.format(thing='duck', place = 'bathtub')

#{"0[]"}.format()
'''
subjects = {'python' : "kim", "c++" : 'sung', 'data structure' : "kim", "database" : "kang"}
print("{0[python]} {0[data structure]}".format(subjects))
#정렬 시 ^ 이건 중앙 정렬이라는 뜻
'''

#f string이 최신 스타일 가장 편함
#capitalize-> 맨 앞글자만 대문자로 바꿈
#upper-> 전체 다 대문자로 바꿈