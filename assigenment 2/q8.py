a=int(input("enter the 1st side of the thriangle \n"))
b=int(input("enter the 2nd side of the thriangle \n"))
c=int(input("enter the 3rd side of the thriangle \n"))

if (a+b)>c:
    print('Triangle can formed')
    if(a==b and b==c):
        print("The triangle is  Equilateral")
    elif(a!=b and b!=c):
        print('The triangle is Scalene')
    else:
        print("the triangle is Isosceles")
else:
    print("triangle can't be formed")

