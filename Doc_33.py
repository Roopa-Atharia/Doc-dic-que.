# Q33.Python: Print a dictionary line by line

students={'Aex':{'class':'V',

        'rolld_id':2},

        'Puja':{'class':'V',

        'roll_id':3}}
for i in students:
    print(i)
    if type(students[i])==dict:
        for j in students[i]:
            print(j,":",students[i][j])
        print()