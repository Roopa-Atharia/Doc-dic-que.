# Q16.Write a Python program to map two lists into a dictionary.
a=["shaina","roopa","riya"]
b=[89,34,23]
c={}
for i in range(len(a)):
    c.update({a[i]:b[i]})
print(c)





