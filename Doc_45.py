a=[{'id':'#FF0000','color':'Red'},{'id':'#800000','color':'Maroon'},{'id':'#FFFF00','color':'Yellow'},{'id':'#808000','color':'Olive'}]
remove=(input("enter the num:-"))
i=0
while i<len(a):
    if i==remove:
        a.pop(i)
    i+=1
print(a)