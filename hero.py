import random

class Hero:
    def __init__ (self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        """Current Hero Will take turn fighting the opponent hero passed in."""
        winner = random.choice([self, opponent])
        if winner == self:
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}")

if __name__ == "__main__":
    """
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    """
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.fight(hero2)