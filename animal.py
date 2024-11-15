class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def drink(self):
        print(f"{self.name} is drinkng!")

class Frog(Animal):
    def jump(self):
        print("{self.name} is jumping!")


