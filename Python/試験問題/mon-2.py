A = 2
B = 5
C = 0
for i in range(4):
    C = A * B
    print(str(i+1) + "回目" + str(A) + "x" + str(B) + "=" + str(C))
    A += 2
    B += 1
