N = int(input("Number : "))
a = "*"
for x in range(N):
    N -= 1
    print(" " * N + ((2 * x) + 1) * a)