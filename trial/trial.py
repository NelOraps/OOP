

class Character_customization:

    def __init__(self, character, weapon, ability1, ability2):
        self.character = character
        self.weapon = weapon
        self.ability1 = ability1
        self.ability2 = ability2

    def setCustom_character(self):
        print("Character: " + self.character)
        print("Weapon: " + self.weapon)
        print("1st Ability: " + self.ability1)
        print("2nd Ability: " + self.ability2)

class Character:
    character_list = {1: 'Wizard', 2: 'Knight', 3: 'Archer', 4: 'Assasin'}

    def getCharacter(self):
        
        for key in self.character_list.keys(): 
            print("[{}] {}".format(key, self.character_list[key]))

        while True:
            print()
            character_choice = int(input("Choose your character: "))
            
            if character_choice >= 1 and character_choice <= 4:
                print("You have chosen the " + self.character_list[character_choice] + " as your character")
                print()
                return self.character_list[character_choice]
            else:
                print("Invalid Input!")

class Weapon:
    weapon_list = {1: 'Wizard Staff', 2: 'Sword', 3: 'Bow & Arrow', 4: 'Katar'}

    def getWeapon(self):
        
        for key in self.weapon_list.keys():
            print("[{}] {}".format(key, self.weapon_list[key]))

        while True:
            print()
            weapon_choice = int(input("Choose your weapon: "))
            print()

            if weapon_choice >= 1 and weapon_choice <= 4:
                print("You have chosen the " + self.weapon_list[weapon_choice] + " as your weapon")
                print()
                return self.weapon_list[weapon_choice]    
            else:
                print("Invalid Input!")

class Ability:
    ability_list = {1: ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hail Storm"],
                    2: ["Fire Slash", "Power Slash", "Gigantic Storm", "Chaotic Disaster"],
                    3: ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"],
                    4: ["Cloaking", "Enchant Posion", "Sonic Acceleration", "Meteor Assault"]}

    def getAbility(self, ch):

        j = 1

        for i in self.ability_list.get(ch):
            print("[{}] {}".format(j, i))
            j += 1

        while True:
            print()
            ability1_choice = int(input("Choose your 1st ability: "))
            print()

            if ability1_choice >= 1 and ability1_choice <= 4:
                while True:
                    print("You have chosen the : " + self.ability_list.get(ch)[ability1_choice-1] + " as your 1st ability")
                    print()

                    ability2_choice = int(input("Now, Choose your 2nd ability: " ))
                    print()

                    if ability2_choice >= 1 and ability2_choice <= 4:
                            print("You have chosen the : " + self.ability_list.get(ch)[ability2_choice-1] + " as your 2nd ability")
                            print()
                            return self.ability_list.get(ch)[ability1_choice-1], self.ability_list.get(ch)[ability2_choice-1]

                    elif ability_choice == ability2_choice:
                         print("You can't adapt same skills, Try again!")
    
                    else:
                        print("Invalid Input!")
            else:
                print("Invalid Input!")


character_info = []
avatar = 0


while avatar < 2:
    print("Choose your Avatar No. " + str(avatar + 1))
    print()
  
    character = Character()
    weapon = Weapon()
    ability = Ability()
    
    ch = character.getCharacter()   
    
    print("Choose your Avatar " + str(avatar + 1) + "'s Weapon")
    print()
  
    wp = weapon.getWeapon()
   
    print("Choose your Avatar " + str(avatar + 1) + "'s Ability")
    print()
    
    ab = ability.getAbility(ch[0])
    
    character_info.append(Character_customization(ch[1], wp, ab[0], ab[1]))
    avatar += 1

print()
print("Your Customized Characters are now ready!")
print()

for user in character_info:
    print("Character No. " + str(avatar) + ":")
    print()
    user.setCustom_character()
    avatar += 1