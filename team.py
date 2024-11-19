import random

class Team:
    def __init__(self,name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        '''Add hero to the team'''
        self.heroes.append(hero)

    def stats(self):
        '''Prints team statistics.'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths if hero.deaths != 0 else hero.kills
            print(f"{hero.name} Kill/Death Ratio: {kd}")

    def revive_heroes(self, health=100):
        '''Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def attack(self, other_team):
        '''Battle each team against each other.'''
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes: 
            living_heroes.append(hero)
        
        for hero in other_team.heroes:
            living_opponents.append(hero)
        
        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)

            hero1.fight(hero2)

            living_heroes = [hero for hero in self.heroes if hero.is_alive()]
            living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]
