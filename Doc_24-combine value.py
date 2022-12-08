# Q24.Write a Python program to combine values in python list of dictionaries.
a={"a":100,"b":200,"c":300}
b={"a":300,"b":200,"c":400}
for i in b:
    if i in a:
        a[i]=a[i]+b[i]
print(a)