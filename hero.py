from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team
import random

class Hero:
    def __init__ (self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

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
                self.add_kill(1)
                opponent.add_death(1)
                return
            
            damage_to_hero = opponent.attack()
            self.take_damage(damage_to_hero)

            if not self.is_alive():
                print(f"{opponent.name} won!")
                opponent.add_kill(1)
                self.add_death(1)
                return
                
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

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.
        '''
        return self.current_health > 0
    
    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""
        self.abilities.append(weapon)
    
    def add_kill(self, num_kills):
        '''Update self.kills by num_kills amount'''
        self.kills += num_kills
    
    def add_death(self,num_deaths):
        '''Update deaths with num_deaths'''
        self.deaths += num_deaths


        




        
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
