c1 = "hi"
c2 = "hello"
c3 = "bonjour"

message =input("Enter your message: ")

if((c1 in message)or (c2 in message) or (c3 in message)) :
    print("Typical message")
else :
    print("Its not Typical")