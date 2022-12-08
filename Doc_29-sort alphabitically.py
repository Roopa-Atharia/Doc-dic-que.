# Q29.Write a Python program to sort a list alphabetically in a dictionary
a={"a":5,"d":3,"c":3,"e":2}
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)