# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств."
# Цели: Применить сокрытие атрибутов и повторить наследование. Рассмотреть на примере объекта из реального мира.
#
# Задача "Изменять нельзя получать":
# Пункты задачи:
# Создайте классы Vehicle и Sedan.
# Напишите соответствующие свойства в обоих классах.
# Не забудьте сделать Sedan наследником класса Vehicle.
# Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle.

class Vehicle: # Создаем первый класс Vehicle
    __COLOR_VARIANTS = ['Red', 'Blue', 'Green', 'Black', 'White'] # Это атрибут класса

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner # Создаем Атрибут объекта
        self.__model = model # Создаем Атрибут объекта
        self.__engine_power = engine_power # Создаем Атрибут объекта
        self.__color = color # Создаем Атрибут объекта

    def get_model(self) -> str:    #Создаём метод объекта
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str: #Создаём метод объекта
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str: #Создаём метод объекта
        return f"Цвет: {self.__color}"

    def print_info(self) -> None: #Создаём метод объекта
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None: #Создаём метод объекта - Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        if (new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle): # Создаем второй класс Sedan(седан) - наследник класса Vehicle
    __PASSENGERS_LIMIT = 5 # (в седан может поместиться только 5 пассажиров)

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        super().__init__(owner, model, color, engine_power,) # Использовался метод super(), тем самым мы обращаемся к классу родителю (Vehicle) чтобы вызвать его методы, через __init__



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()