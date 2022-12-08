# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
a=int(input("enter the num:-"))
b={}
i=0
while i<a:
    n=input("enter the key:-")
    m=int(input("enter the value:-"))
    b.update({n:m})
    i=i+1
print(b)
max=0
for i in b:
    if b[i]>max:
        max=b[i]
    b.update({n:m})
print("Maximum is=",max,)