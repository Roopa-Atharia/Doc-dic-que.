# Q5.Write a Python program to sort (ascending and descending) a dictionary by value.
a={1:4,2:1,3:5,4:2}
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)

a={1:4,2:1,3:2,4:2}
for i in a:
    for j in a:
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)



