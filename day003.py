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

#assignment (loop)

#반복문 while
while True: #infinite loop
    menu = input("1) Fahrenheit -> Celsius  2) Celsius -> Fahrenheit : 3) Quit program : ")

    if menu == '1':
        fahrenheit = float(input("input Fahrenheit : "))
        print('Fahrenheit : %f F, Celsius : %.4f C' % (fahrenheit, (fahrenheit - 32.0) * 5.0 / 9.0))
    elif menu == '2':
        celsius = float(input("input Celsius : "))
        print(f'Celsius {celsius}C, Fahrenheit {((celsius * 9.0 / 5.0) + 32.0): .4f}F')
    elif menu =='3':
        print('Terminate Program.')
        break