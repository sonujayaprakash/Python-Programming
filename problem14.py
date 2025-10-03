sub1 = int(input("Enter your sub1 marks: "))
sub2 = int(input("Enter your sub2 marks: "))
sub3 = int(input("Enter your sub3 marks: "))

total = sub1 + sub2 + sub3
percentage = total / 3

if(sub1 < 33) and (sub2 < 33) and (sub3 < 33) :
    print("Result : Failed")
elif(percentage < 40) :
    print("Result : Failed")
else :
    print("Congratulations, you have passed the exam")