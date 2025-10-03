a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

greatest = a

if(b > greatest) :
    greatest = b
if(c > greatest) :
    greatest = c
if(d > greatest) :
    greatest = d

print("Greatest number is: ",greatest)