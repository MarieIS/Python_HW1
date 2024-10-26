a = int(input('give me your 3-digit number: '))
sum = a % 10 + (a // 10 % 10) + a // 100
print('the sum of digits: ', sum)