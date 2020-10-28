N = int(input("Number : "))
a = "*"
for x in range(N):
    y = 2 * x + 1
    N -= 1
    print(" " * N + y * a)
    # print("+" * N + ((2 * x) + 1) * a)