from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    def __init__ (self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
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

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def add_armor(self, armor):
        """Add armor to self.armors
            Armor: Armor Object
        """
        self.armors.append(armor)

    def defend(self):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        if self.current_health <= 0:
            return 0
        
        total_block = 0 
        for armor in self.armors:
            total_block += armor.block()
        return total_block
    
    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense"""
        defense = self.defend()
        damage_taken = max(0, damage - defense)
        self.current_health -= damage_taken
        print(f"{self.name} takes {damage_taken} damage, current health is now {self.current_health}.")

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0
    
    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
            return
        while self.is_alive() and opponent.is_alive():
            damage_to_opponent = self.attack()
            opponent.take_damage(damage_to_opponent)

            if not opponent.is_alive():
                print(f"{self.name} won!")
                return
            
            damage_to_hero = opponent.attack()
            self.take_damage(damage_to_hero)

            if not self.is_alive():
                print(f"{opponent.name} won!")
                return
    
    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)
            
        

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())