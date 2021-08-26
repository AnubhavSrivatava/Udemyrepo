#n = abcaba
#out - abcaabbaaa


inp = input ("Enter string")
l1=[]
for i in inp:
    c=0
    for j in inp:
        l1.append(j)
        if i == j:
            c+=1
            for k in range(c):
                l1.append(j)





 #   print(f"{out_p}{c}")

print(l1)



#n = Area, Street, Town, city, area, town
#out = Area, Town

l1 = ["Area", "Street", "Town", "city", "area", "town"]
l2 =[i.lower() for i in l1 ]
l3=[i for i in l2 if i in l2]


print(l3)