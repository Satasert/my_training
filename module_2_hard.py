import random

def first_digit_num():
    num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers = list(range(3, 21))
    part_code = random.choice(numbers)
    return part_code

def all_passwords(n):
    code = {}
    code.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                     10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
                     14: 1611325212343114105968, 15: 1214114232133124115106978, 16: 1317115262143531341251161079,
                     17: 11621531441351261171089, 18: 12151811724272163631545414513612711810,
                     19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911})
    newcode = code.get(n)
    return newcode
n = first_digit_num()
n = int(input('введите код :'))
print('Код   :', n)
print('Пароль :', all_passwords(n))

number1 = list(range(1, n))
number2 = list(range(1, n))
pairs = []
result = ""

for i in number1:
    for j in number2:
        si1 = i
        si2 = j
        if si1 >= si2:
            continue
        else:
            z = n % (si1 + si2)
            if z == 0:
                pairs.append([si1, si2])
                result = result + str(si1) + str(si2)
print('Числа пары', *pairs)
print('Укажите пароль', result)
if int(result) == all_passwords(n):
    print('Пароль введен верно')