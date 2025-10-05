marks = {
    "Sonu" : 93,
    "Sidharth" : 87,
    "Aleena" : 95,
    "Jasmine" : 90
}
# this dictionary is unordered, mutable, indexed list wih keyvalue pairs
print(marks)

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sidharth" : 91, "Vysakh" : 85})
print(marks)
#difference between these 2 are
print(marks.get("Vysakh")) #this will give none if the key is not in the dictionary
print(marks["Vysakh"]) #this will give error if it is not present

#empty dictionary
e = {}