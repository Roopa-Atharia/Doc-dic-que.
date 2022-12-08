# Q38.. Write a Python program to drop empty Items from a given Dictionary.
a={'c1': 'Red', 'c2': 'Green', 'c3': None}
for i in a:
    if a[i]==None:
        del a[i]

print(a)