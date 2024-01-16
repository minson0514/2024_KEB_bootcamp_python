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
subjects = ["python", "c++", "database"]
subjects_string = " / ".join(subjects)
print(subjects_string)#python / c++ / database
#list 안의 elements 사이에 " / "가 추가되어서 리턴됨
