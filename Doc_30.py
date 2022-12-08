# Q30.Write a Python program to remove spaces from dictionary keys.
a={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
b={}
for i in a:
    c=""
    for j in i:
        if j==" ":
            pass
        else:
            c=c+j
    b[c]=a[i]
print(b)