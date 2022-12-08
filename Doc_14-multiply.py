# Q14.Write a Python program to multiply all the items in a dictionary.
a={1:1,2:2,3:7,4:5}
multiply=1
multiply2=1
for i in (a):
    multiply*=i
    multiply2*=a[i]
print("keys",multiply)
print("value",multiply2)