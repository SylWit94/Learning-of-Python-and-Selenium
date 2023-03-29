# Creating classes with __init__:
class Human:
    def __init__(self):
        print('New Human was born')

    def speak(self):
        print('I can speak!')


class Animal:
    def speak(self):
        print('I cannot speak')


# Class usage examples:
print("Let's create Adam!")
adam = Human()

print("Let's create a dog!")
dog = Animal()

print('Now all speak!')
adam.speak()
dog.speak()


# Creating classes with __init__ and paramiter:
class Human:
    def __init__(self, name):
        self.name = name
        print(f'New Human was born! His name is {self.name}')

    def speak(self):
        print(f'I can speak! My name is {self.name}')


class Animal:
    def speak(self):
        print('I cannot speak!')


print("Let's create Adam!")
adam = Human('Adam')
print("Let's create a dog!")
dog = Animal()
print('Now all speak!')
adam.speak()
dog.speak()