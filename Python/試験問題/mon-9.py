name = input("名前")
koku = int(input("国語"))
math = int(input("数学"))
eng = int(input("英語"))


total = koku + math + eng
avg = total / 3


print(name+"さんの３教科の合計は"+str(total)+"点・平均は"+str(avg)+"点です。")