print("")
# n = int(input("n"))
# w = int(input("w"))
n = 20
w = 4
for i in range(n):
    print("*", end="")
    if i%w == w-1:
        print(i)

if n%w:
    print()
else:
    print(n)
