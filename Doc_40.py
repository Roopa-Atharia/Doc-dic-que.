# Q40.Write a Python program to convert more than one list to nested dictionary.
a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d={}
i=0
while i<len(a):
    d.update({a[i]:{b[i]:c[i]}})
    i=i+1
print(d)