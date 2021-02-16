sei = 0
sum1 = 0
while True:
    if sei%3 == 0:
        sum1 += sei
    if sum1 > 50:
        atai = sei
        break;
    sei += 1


print(str(atai))
