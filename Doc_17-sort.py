# Q17.Write a Python program to sort a dictionary by key.
a={"Roopa":67,"Sunaina":97,"priya":66,"Riya":34}
l=sorted(a.keys())
s=list()
for elements in l:
    s.append(a[elements])
d1=dict(zip(l,s))
print(d1)

