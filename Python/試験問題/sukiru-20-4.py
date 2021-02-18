def kan_A(n):
    n = n + 2
    return n

def kan_B(n):
    n = n + 3
    return n


def print_(a,b):
    a = kan_A(a)
    b = kan_B(b)
    c = a * b
    print(str(a) + "x" + str(b) + "=" + str(c))




A = int(input("A : "))
B = int(input("B : "))
print_(A,B)


