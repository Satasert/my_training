class House: #1.Создаем класс
    def __init__(self, name, number_of_floors): #2.Определяем метод
        self.name = name # 3.Создаем атрибут и присваиваем переданное значение
        self.number_of_floors = number_of_floors # 3.Создаем атрибут и присваиваем переданное значение
    def go_to(self, new_floor): #4.Создаем метод с параметрами, и пишем логику внутри метода.
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# !!!!!!!!!! Продолжение дрмашнего задания module_5_3.py !!!!!!!

    def __eq__(self, other): # 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other. (Количество этажей разные поэтому = False)
        if isinstance(other, House): # isinstance(other, House) - other указывает на объект типа House.
            return self.number_of_floors == other.number_of_floors
        return False

    def __add__(self, value): # 3.__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
        if isinstance(value, int): # isinstance(other, int) - other указывает на объект типа int.
            self.number_of_floors += value
        return self
# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.number_of_floors += value
        return self

# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
    def __gt__(self, other):
         return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
         return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
         return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
         return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
         return self.number_of_floors != other.number_of_floors




#h1 = House('ЖК Горский', 18) # 5.Создаем объект класса House с произвольным названием и количеством этажей.
#h2 = House('Домик в деревне', 2) # 5.Создаем объект класса House с произвольным названием и количеством этажей.
#h1.go_to(5) #6. Вызываем метод объекта с произвольным числом
#h2.go_to(10) #6. Вызываем метод объекта с произвольным числом
#print(h1.name, h1.number_of_floors) # *** Уважаемый преподователь, это я для себя вывел и закоментировал.
#print(h2.name, h2.number_of_floors) # *** Уважаемый преподователь, это я для себя вывел и закоментировал для личного понимания.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#print(len(h1))
#print(len(h2))

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
#
h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__


