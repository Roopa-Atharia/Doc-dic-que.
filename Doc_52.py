dict1={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
max=0
b=[]
for i in dict1:
    if dict1[i]>max:
        max=dict1[i]
print(max)
