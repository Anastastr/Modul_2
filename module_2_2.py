first = int(input('Введите любое число'))
second = int(input('Теперь еще одно'))
third = int(input('Давай еще'))
if first == third or second == third:
    print('2')
elif first == second == third:
    print('3')
else:
    print('0')