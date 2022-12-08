# Q8.Write a Python program to check whether a given key already exists in a dictionary.
key={1:"one",2:"two",3:"three",4:"four"}
n=int(input("enter the num:-"))
if n in key:
    print("The key is present")
    print("the value",key[n])
else:
    print("The key is not present")
