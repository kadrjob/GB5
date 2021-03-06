# 5. Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

my_list = [57.8, 46.51, 97, 88.16, 57.08, 12.04, 88.41, 18, 88.57]

# для дальнейшего подтверждения что список не изменялся
id_before_sort = id(my_list)
print(f'id_before_sort {id_before_sort}')

# for el in my_list:
#     print('{0} руб {1:02d} коп'.format(el * 100 // 100, int(el * 100 % 100)))

# или так
print('\n'.join(str('{0} руб {1:02d} коп'.format(el * 100 // 100, int(el * 100 % 100))) for el in my_list))

# проверим что список остался тем же (ссылка на область памяти)
my_list.sort()
id_after_sort = id(my_list)
print(f'id_after_sort {id_after_sort}')
if id_before_sort == id_after_sort:
    print('List sorted in place')
else:
    print('Error sort in place')

# вывели сортированный список
print('\n'.join(map(str,my_list)))

# новый список
new_list = list(reversed(my_list))
print(f'new list id {id(new_list)}')                     # проверим новый ли

# берем пять максимальных значений упорядоченного по убыванию списка (берем с конца списка)
print('generator')
print('\n'.join(str(val) for val in new_list[:5]))

print('map')
print('\n'.join(map(str, new_list[:5])))

# ну или вывод поэлементно
print('for')
for el in new_list[:5]:
    print(str(el))
