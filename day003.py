#split with split()
#문자열을 분리해서 리스트에 담는다
'''
course = "2024 KEB bootcamp"
print(course)
#list_course = course.split() #띄어쓰기 기준으로
list_course = course.split('B') #B를 기준으로
print(list_course)#list 안에 담아서 return해줌
'''
#응용
'''
numbers = input("firstnumber secondnumber : ").split()
#print(numbers[0]+numbers[1]) #두 문자 간의 결합
print((int(numbers[0]) + int(numbers[1]))) #두 숫자 간의 결합
'''

#Combine by using join()
'''
subjects = ["python", "c++", "database"]
subjects_string = " / ".join(subjects)
print(subjects_string)#python / c++ / database
#list 안의 elements 사이에 " / "가 추가되어서 리턴됨
'''

#substitute by using replace
#아래 방법은 원본이 바뀌지는 않음
'''
course = "2024 KEB bootcamp"
print((course.replace('KEB','inha')))#2024 inha bootcamp
print((course))
'''
#원본을 바꾸는 방법
'''
course = "2024 KEB bootcamp"
print((course))
course=course.replace('KEB', "Inha")
print((course))
'''

#여러개 중 하나만 바꾸고 싶을 때
'''
course = "KEB 2024 KEB bootcamp KEB"
print(course)
course=course.replace('KEB', "Inha", 1)#3번째 자리는 count 몇 개 바꾸는 지
print(course)
'''

#strip
'''
course = "KEB #2024 KEB !bootcamp KEB...*!#"
print(course)
course=course.replace('KEB', "Inha", 2)#3번째 자리는 count 몇 개 바꾸는 지
print(course)
print(course.strip("!#.*")) #연속적으로 있는 애들만 지워줌
'''

#find & index
'''
course = "* KEB 2024# KEB !bootcamp KEB...*!#"
print(course.find('KEB')) #2
print(course.rfind('KEB')) #26
print(course.index('KEB')) #2
print(course.rindex('KEB')) #26
print(course.find('Inha')) #find는 없으면 -1 반환
print(course.index('Inha')) #error -> index는 없으면 에러 발생
'''

