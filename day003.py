#예외처리 preview
'''
subjects = "python c++ database linux"
subject = input("수강신청과목 입력 : ")

try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스 입니다.")
#try에서 예외가 생기면 valueerror 가 실행됨
except ValueError:
    print(f'해당 과목이 존재하지 않습니다.')
'''
