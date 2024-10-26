a = int(input('give me your 3-digit number: '))
if a // 100 > 0 and a // 100 <= 9:
    sum = a % 10 + a // 10 % 10 + a // 100
    print('the sum of digits: ', sum)
else:
    print('your number has more or less 3 digits. please retry')