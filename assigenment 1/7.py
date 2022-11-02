from math import sqrt
a=int(input("Enter the x cordinate of point 'A' "))
a1=int(input("Enter the y cordinate of point 'A' "))
b=int(input("Enter the x cordinate of point 'B' "))
b1=int(input("Enter the y cordinate of point 'B' "))

dist=sqrt(pow((b-a),2)+pow((b1-a1),2))
print("the distance between the two point a and b is ",dist)
