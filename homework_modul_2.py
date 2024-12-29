#number = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def need_password(number):
    password = ' '
    for a in range(1, number):
        for b in range(2, number):
            if b <= a:
                continue
            if number % (a + b) == 0:
                password += str(a) + str(b)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = need_password(n)
print('Пароль:', result)