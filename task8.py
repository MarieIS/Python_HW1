n = int(input('введите n долек: '))
m = int(input('введите m долек: '))
k = int(input('введите k долек: '))
if k % n == 0 or k % m == 0:
    print('можно')
else:
    print('нельзя')