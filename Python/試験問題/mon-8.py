TBL = [20,50,30,10,35,45,25,35,75,90]

last = len(TBL)

while last > 0:
    for j in range(0, last-1, 1):
        if TBL[j] > TBL[j+1]:
            temp = TBL[j]
            TBL[j] = TBL[j+1]
            TBL[j+1] = temp
    last = last - 1

print(TBL)
