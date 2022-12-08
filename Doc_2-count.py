# Q2.Write a Python program to create a dictionary from a string.
# Sample string : 'w3resource

a="w3resource"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(b)
