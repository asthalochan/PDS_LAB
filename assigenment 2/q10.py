from math import sqrt
a=int(input("enter the value of a \n"))
b=int(input("enter the value of b \n"))
c=int(input("enter the value of c \n"))

x1=float((-b+sqrt(pow(b,2)-4*a*c))/2*a)
x2=float((-b-sqrt(pow(b,2)-4*a*c))/2*a)

print(f"the roots of the qadratics eqations are{x1},{x2}")