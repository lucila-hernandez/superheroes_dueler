import random
from ability import Ability

class Weapon(Ability):
  def attack(self):
    """  This method returns a random value, between one half to the full attack power of the weapon. """
    half_damage = self.max_damage // 2
    return random.randint(half_damage, self.max_damage)
  
if __name__ == "__main__":
    sword = Weapon("Sword", 80)
    print(sword.name)
    print(sword.attack())