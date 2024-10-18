# print(int.__mro__)
# print(object)
class User:
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, values in kwargs.items():
            setattr(self, key, values)
        # self.kwargs = kwargs.get('name')
        # self.age = kwargs.get('age')

other = [1,2,3]
user = {'name': 'Den', 'age': 25,'gender': 'male'}

user1 = User(*other, **user)
# user2 = User()
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)