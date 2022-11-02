a=int(input("Enter the 1st number \n"))
b=int(input("Enter the 2nd number \n"))
c=int(input("Enter the 3rd number \n"))

if a>b:
    lar=a
    if lar > c:
        lar2=lar
    else:
        lar2=c

else:
    lar=b
    if lar > c:
        lar2=lar
    else:
        lar2=c
print(f"The largest number is {lar2}")

