# Q21.Write a Python program to print all unique values in a dictionary.
a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dic=[]
for i in a:
    for j in i:
        if i[j] not in dic:
            dic.append(i[j])
print(dic)