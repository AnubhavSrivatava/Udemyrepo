str = input("Enter any string")
l1 = list(str)
lenth = len(l1)

for i in l1:
    c = 0
    for j in l1:
        if i == j and j != '*':
            c += 1
            j = '*'
    print(f"{i} {c}")
