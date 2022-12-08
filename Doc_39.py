# Q39.Write a Python program to filter a dictionary based on values.
a={'Cierra Vega':175,'Alden Cantrell':180,'Kierra Gentry':165,'Paierre Cox':190}
for i in a:
    for j in a:
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
print(a)