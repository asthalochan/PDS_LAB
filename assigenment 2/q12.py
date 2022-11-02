
num1=int(input("Enter 1st number \n"))
num2=int(input("Enter 2nd number \n"))

operat=int(input('''Enter
                         '1' for addition(+)
                         '2' for substraction(-)
                         '3' for multiplication(*)
                         '4' for intger division(\)
                         '5' for floor division(\\)
                         '6' for remender (%) \n'''   ))

match(operat):
    case 1:
        print(f"The addition of two number is {num1+num2}")
    case 2:
        print(f"The substraction of two number is {num1-num2}")

    case 3:
        print(f"The multiplication of two number is {num1*num2}")    
    case 4:
        print(f"The integer division of two number is {num1/num2}")
    case 5:
        print(f"The floor division of two number is {num1//num2}")
    case 6:
        print(f"The remender of two number is {num1%num2}")
        