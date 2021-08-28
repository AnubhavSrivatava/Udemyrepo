test_str = input(('Enter a sting'))
freq = {}

for i in test_str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print ("Count of all characters in Geeks for Geeks is :\n "
                                        +  str(freq))



