
def test(a, b, c):
    go = a + b + c
    if 260 <= go <= 300:
        result = "A"
    elif 200 <= go <= 259:
        result = "B"
    elif 100 <= go <= 199:
        result = "C"
    elif 0 <= go <= 99:
        result = "D"
    return go, result


# main
x = int(input("numb1 : "))
y = int(input("numb2: "))
z = int(input("numb3: "))

# print(test(x, y, z))
gou, hyou = test(x, y, z)

print("合計は " + str(gou) + " 評価 " + hyou)
