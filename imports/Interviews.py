#prime numbers

for i in range(3, 50):
    c = 0
    for j in range(2, i):
        if i % j  == 0:
            c += 1
    if c < 1:
        print(f"prime {i}")
    else:
        print(f"Not a prime {i}")
