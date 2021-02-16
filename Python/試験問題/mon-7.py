TBL = [10,20,40,42,50,55,75,90,100,120,150]

head = 0
tail = 10

index = -1
target = int(input("入力："))

while index == -1 and head <= tail:
    middle = int((head+tail)/2)

    if TBL[middle] == target:
        index = middle
    elif TBL[middle] < target:
        head = middle+1
    else:
        tail = middle - 1
if index == 1:
    print("見つかりません")
else:
    print("TBLの"+str(index)+"番他です")