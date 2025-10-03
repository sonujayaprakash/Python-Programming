a =int(input("Enter your Age: "))

if(a >= 18) :
    print("You are eligible to have a License")
elif(a == 0) :
    print("Age cannot be zero")
elif(a < 0) :
    print("Invalid Age")
else :
    print("You are not eligible to have a License")