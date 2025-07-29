def neg(n):
    if n >= 0:
        print("Already Zero")
    else:
        for i in range(n, 1):
            print(i, end=" ")
        print(0)

def pos(n):
    if n <= 0:
        print("Already Zero")
    else:
        for i in range(n, -1, -1):
            print(i, end=" ")
        print()
