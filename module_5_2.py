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



h1 = House('ЖК Горский', 18) # 5.Создаем объект класса House с произвольным названием и количеством этажей.
h2 = House('Домик в деревне', 2) # 5.Создаем объект класса House с произвольным названием и количеством этажей.
#h1.go_to(5) #6. Вызываем метод объекта с произвольным числом
#h2.go_to(10) #6. Вызываем метод объекта с произвольным числом
#print(h1.name, h1.number_of_floors) # *** Уважаемый преподователь, это я для себя вывел и закоментировал.
#print(h2.name, h2.number_of_floors) # *** Уважаемый преподователь, это я для себя вывел и закоментировал для личного понимания.
print(len(h1))
print(len(h2))
print(h1)
print(h2)