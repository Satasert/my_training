
# Домашнее задание по теме "Зачем нужно наследование"

class Animal:                    # Создаем 1 класс родителя
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

class Plant:                      # Создаем 2 класс родителя
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):               # Наследник класса №1
    def eat(self, food):             # У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):             # Наследник класса №2
    def eat(self, food):   # У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):                # Наследник класса №3
    pass  # У цветка по умолчанию edible = False

class Fruit(Plant):                 # Наследник класса №4
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # У плода edible = True




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.