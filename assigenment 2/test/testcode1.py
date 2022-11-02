age=int(input("Enter your age \n"))
if age>=21:
    print("you are eligible for vote")
    print("you are eligible for marriage")
elif age>=18:
    print("you are eligible for vote")
    print("you are not eligible for marriage")


else:
    print("you are not eligible for both")
