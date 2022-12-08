# Q22.Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
a={'1':['a','b'], '2':['c','d']}
b=a["1"]
c=a["2"]
for i in b:
    for j in c:
        print(i+j)