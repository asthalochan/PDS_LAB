s1=int(input("Enter the mark in pds \n"))
s2=int(input("Enter the mark in dsa \n"))
s3=int(input("Enter the mark in dme \n"))
s4=int(input("Enter the mark in statistics \n"))
s5=int(input("Enter the mark in algebra \n"))

per=float(s1+s2+s3+s4+s5)/5

if per>=90:
    print("your grade is O")
elif per>=80 and per<90:
    print("your grade is E")
elif per>=70 and per <80:
    print("your grade is A")
elif per>=60 and per<70:
    print("your grade is B")
elif per>=50 and per<60:
    print("your grade is C")
else:
    print("You are Fail")