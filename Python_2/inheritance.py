class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        print('Animal!')

    def increase_age(self):
        self.age = self.age + 1
        print(f'This is {self.name} and he has {self.age} years')


class Mammal(Animal):
    def __init__(self, age, name):
        Animal.__init__(self, age, name)
        print('Mammal!')

    def introduce_yourself(self):
        print(f'My name is {self.name}')


class Cat(Mammal):
    def __init__(self, age, name, master):
        Mammal.__init__(self, age, name)
        self.master = master
        print('Cat!')

    def purr(self):
        print('purr!')

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f'My master is {self.master}')


class Dog(Mammal):
    def __init__(self, age, name, master, favourite_toy):
        Mammal.__init__(self, age, name)
        self.master = master
        self.favourite_toy = favourite_toy
        print('Dog!')

    def introduce_yourself(self):
        super().introduce_yourself()
        print(f'My master is {self.master}')
        print(f'My favourite toy is {self.favourite_toy}')


mammal_1 = Mammal(10, 'Nemon')
mammal_1.introduce_yourself()
mammal_1.increase_age()

print('-')

cat_1 = Cat(2, 'Garfield', 'Bob')
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()

print("-")

dog_1 = Dog(4, 'Rex', 'Tom', 'monkey')
dog_1.introduce_yourself()
dog_1.increase_age()
