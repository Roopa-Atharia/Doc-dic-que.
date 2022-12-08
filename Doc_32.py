# Q32.Write a Python program to get the key, value and item in a dictionary.
a={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
c=0
for i in a:
    c=c+1
    print(i,end=" ")
    print(a[i],end=" ")
    print(c,end=" ")
    print()
