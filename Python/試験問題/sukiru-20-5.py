# sukiru-20-5

sumxx = 0

def player(x):
    global sumxx
    sumxx += x



#mainです
for i in range(5):
    x = int(input(str(i+1)+"人分目: "))
    player(x)


avr = sumxx / 5
print("合計 "+str(sumxx)+" 平均 "+str(avr))
