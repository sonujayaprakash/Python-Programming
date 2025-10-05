s = { 1,3,5,7,9,3,3,2,4,5,7,9,"Appu","Devi" }
# in set elements don't repeat,unordered, unindexed
e = set() # this is an empty set
a = { 22,33,44,1,5,7 }
print(type(s))
print(type(e))
s.add("Alee")
print(s)
print(len(s))
print(s.pop())
print(s.union(a))
print(s.intersection(a))