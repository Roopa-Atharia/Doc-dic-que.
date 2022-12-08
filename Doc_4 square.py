# Q4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d=dict()
a=int(input("enter the num:-"))
for x in range(a):
    d[x]=x**2 
print(d)