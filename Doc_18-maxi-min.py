# Q18.Write a Python program to get the maximum and minimum value in a dictionary.

dic={"six":6,"one":1,"two":2,"seven":7,"nine":9}
max=0
min=dic["six"]
for i in dic:
    if dic[i]>max:
        max=dic[i]
    elif dic[i]<min:
        min=dic[i]
print("Maximum is=",max,"\n","Minimum is=",min)