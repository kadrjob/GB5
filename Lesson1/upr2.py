# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# получение суммы цифр числа можно вынести и в функцию
def get_digit_sum(in_digit):
    elem_sum = 0
    while in_digit > 0:
        next_digit = in_digit % 10  # извлекаем последний разряд в виде числа
        elem_sum += next_digit  # получаем сумму
        in_digit //= 10  # уменьшаем число на разряд

    return elem_sum

# заполняем список
nums = []
idx = 1
while idx <= 1000:
    nums.append(idx ** 3)
    idx += 1

total_sum = 0             # общая сумма подходящих чисел
for elem in nums:
#    if get_digit_sum(elem) % 7 == 0:           # сумма цифр числа
#        total_sum += elem
    total_sum += elem if get_digit_sum(elem) % 7 == 0 else 0

print(f'Общая сумма чисел {total_sum}')

# увеличиваем числа списка на 17
total_sum = 0             # общая сумма подходящих чисел
for elem in nums:
    # if get_digit_sum(elem + 17) % 7 == 0:
    #     total_sum += elem + 17
    total_sum += elem + 17 if get_digit_sum(elem + 17) % 7 == 0 else 0

print(f'Общая сумма чисел +17 {total_sum}')

# звездочка
print('Звездочка')
total_sum = 0   # для неувеличенных чисел
total_sum17 = 0  # для увеличенных на 17

for elem in range(1, 1001):
    elem_pow = elem ** 3
    if get_digit_sum(elem_pow) % 7 == 0:
        total_sum += elem_pow

    # +17
    if get_digit_sum(elem_pow + 17) % 7 == 0:
        total_sum17 += elem_pow + 17

print(f'*Общая сумма чисел {total_sum}')
print(f'*Общая сумма чисел +17 {total_sum17}')
