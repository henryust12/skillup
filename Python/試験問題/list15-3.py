def check_name(xx,yy,zz):
    go = xx + yy + zz
    avr = go / 3
    print("合計 "+str(go)+" 平均 "+str(avr))
    # return go,avr



#メイン
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

check_name(a,b,c)


# print("合計 "+str(sum1)+" 平均 "+str(avr))
