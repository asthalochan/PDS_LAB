num=int(input("Enter a number \n"))
if (num%2==0) and (num%3==0):
    print("Divisible by both")

elif (num%2==0) or (num%3==0):
    print("Divisible by either 2 or 3")
else:
    print("Not divisible by any two")