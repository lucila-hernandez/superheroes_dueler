from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None
    
    def create_ability(self):
        '''Prompt for Ability information.
          return Ability with values from user Input
        '''
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))

        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''Prompt user for Weapon information.
          return Weapon with values from user input.
        '''
        name = input("What is the weapon's name? ")
        damage = int(input("What is the weapon's damage value? "))

        return Weapon(name, damage)
    
    def create_armor(self):
        '''Prompt user for Armor information.
          return Armor with values from user input.
        '''
        name = input("What is the armor's name? ")
        defense = int(input("What is the defense value of the armor? "))

        return Armor(name, defense)

    def create_hero(self):
        '''Prompt user for Hero information.
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name) 
        
        add_item = None  

        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")

            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)
            
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

        return hero  

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        self.team_one = Team("Team One")
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        self.team_two = Team("Team Two")
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
    
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        print("Surviving heroes from " + self.team_one.name + ":")
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print(hero.name)

        print("Surviving heroes from " + self.team_two.name + ":")
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(hero.name)

        team_one_survivors = len([hero for hero in self.team_one.heroes if hero.deaths == 0])
        team_two_survivors = len([hero for hero in self.team_two.heroes if hero.deaths == 0])

        if team_one_survivors > team_two_survivors:
            print(self.team_one.name + " wins!")
        elif team_two_survivors > team_one_survivors:
            print(self.team_two.name + " wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    game_is_running = True 

    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else: 
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

