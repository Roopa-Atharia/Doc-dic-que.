# Q15.Write a Python program to remove a key from a dictionary.
a={1:"one",2:"two",3:"three"}
remove=int(input("enter the number :" ))
i=0
while i<len(a):
    if i==remove:
        a.pop(i)
    i+=1
print(a)