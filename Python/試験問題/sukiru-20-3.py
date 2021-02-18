max1 = 0
min1 = 100
def kakunin():
    global max1
    global min1
    for i in range(5):
        x = int(input("数字 : "))
        if x < min1:
            min1 = x
        if x > max1:
            max1 = x
    return max1, min1


# main
maxx, minx = kakunin()
print("最大値　"+str(maxx)+" 最小値 "+str(minx))
