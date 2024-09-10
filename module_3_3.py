
#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True): # Создаем фунцию которая принимает три параметра со значениями по умолчанию
    print(a, b, c)
print_params("Black", 'Urban') # Вызов функции с разным количеством аргументов
print_params("Университет") # Вызов функции с разным количеством аргументов
print_params () # Вызов без аргумента.
print_params(b=25) # Проверка работы вызова
print_params(c = [1,2,3]) # Проверка работы вызова

#2.Распаковка параметров:
values_list = [15, "Привет, друг!", 3.15]
values_dict = {'a' : 1, 'b' : 'строка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

