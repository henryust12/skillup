def check_name(name):
    if len(your_name) < 8:
        return False
    else:
        return True

your_name = input('君の名は>')

if check_name(your_name):
    print('OK')
else:
    print('名前が不正です')
