# a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# for i in a:
#     for j in i:
#         i[j]=int(i[j])
# print(a)

a=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
for i in a:
    for j in i:
        i[j]=float(i[j])
print(a)