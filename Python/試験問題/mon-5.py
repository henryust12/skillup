sum1 = 0
max1 = 0
min1 = 100

print()
for i in range(3):
    ondo = int(input("点数を入力："))
    sum1 += ondo
    if max1<ondo:
        max1=ondo
    if min1>ondo:
        min1=ondo
avg=sum1/3

print(avg)
print(max1)
print(min1)
