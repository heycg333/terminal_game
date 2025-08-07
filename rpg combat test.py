import random
import sys
import time

class Hero: #hero stats and combat methods
    def __init__(self, name, maxhp, hp, atk, atkmin, atkmax, defense, block, potion, sword, shield, armor, fireshield, slayersword, rangervolley, venom):
        self.name = name
        self.max_hp = maxhp
        self.hp = hp
        self.atk = atk
        self.atk_min = atkmin
        self.atk_max = atkmax
        self.defense = defense
        self.block = block
        self.potion = potion
        self.sword = sword
        self.shield = shield
        self.armor = armor
        self.fire_shield = fireshield
        self.slayer_sword = slayersword
        self.ranger_volley = rangervolley
        self.venom = venom
    
    def equipment_check(self):
        print(f"Inventory - {hero.sword}, {hero.shield}, {hero.armor}, {hero.potion} potion")      

    def sleep(self):
        sleep_lines = ["zzzz...", "zzz...", "*snoooore*", "zz...", 'z...']
        for i in sleep_lines:
            print(i)
            time.sleep(1)

    # === COMBAT LOOP - HERO ACTION ===
    def std_atk(self, monster): #standard attack with 1/20 chance for crit/miss
        print(f"\n{self.name} attacks!")
        d20 = random.randint(1,20)
        rng = (random.randint(self.atk_min,self.atk_max))
        dmg = (self.atk + rng)
        if d20 == 20:
            print("\n**********************")
            print("⚔️  \033[1;33mCRITICAL HIT!\033[0m  ⚔️")
            print("**********************")
            dmg *= 2  
        elif d20 == 1:
            print(f"\n{self.name} Missed!")
            return

        if self.block: #blocking adds 2 dmg to next attack
            dmg += 2
            self.block = False
        
        monster.take_dmg(dmg)

    def block_atk(self): #sets block attribute to add atk dmg and reduce next incoming dmg
        print(f"\n{self.name} conserves energy, raises shield, and braces for impact\n")
        self.block = True
    
    def heal_potion(self): #heals 10 up to max hp
        self.hp = min(self.hp + 10, self.max_hp)
        if self.hp == self.max_hp:
            print(f"\n{self.name} is fully healed")
        else:
            print(f"\n{self.name} heals 10 hp")
        print(f"{self.name} has {self.hp} hp\n")
        self.potion -= 1

    def take_dmg(self, dmg): #applies monster attack dmg
        print(f"\n{hero.name} takes {dmg} damage")
        self.hp -= dmg
        '''if self.hp <= 0:
            print("")
            print(f"{self.name} has perished")
            print("")
            gameover(hero)
        else:
            print(f"{self.name} has {self.hp} hp left\n")'''

    def ranged_atk(self, monster):
        d20 = random.randint(1, 20)
        if d20 == 20:
            print("\n**********************")
            print("  \033[1;33mCRITICAL HIT!\033[0m  ")
            print("**********************")
            dmg = monster.hp - 25
        else:
            dmg = 1
            print(f"\n{self.name}'s arrow hits. It will take much more to bring the beast down!")
            
        monster.take_dmg(dmg)


    def special_atk_ranged(self, monster, round):
        d20 = random.randint(1, 20)
        print("")
        if hero.ranger_volley:
            print("You signal the rangers!")
            if round > 5 or d20 == 20:
                print("\n**********************")
                print("  \033[1;33mCRITICAL HIT!\033[0m  ")
                print("**********************")
                dmg = monster.hp - 25
            elif d20 > 16:
                dmg = random.randint(8, 11)
                print("\nThe volley strikes true")
            else: 
                print("The dragon spins to avoid the worst of the attack")
                dmg = random.randint(2, 4)
        elif hero.slayer_sword:
            print("You point the sword skyward as its vibrations explode into a beam of energy!")
            if round > 5 or d20 == 20:
                print("\n**********************")
                print("  \033[1;33mCRITICAL HIT!\033[0m  ")
                print("**********************")
                dmg = monster.hp - 25
            elif d20 > 16:
                dmg = random.randint(8, 11)
                print("\nThe beam strikes true")
            else: 
                print("The dragon spins to avoid the worst of the attack")
                dmg = random.randint(2, 4)
        elif hero.fire_shield:
            print("\nYou signal the dwarves!")
            print("As the dragon swoops down they launch their claw traps")
            if round > 5 or d20 == 20:
                print("\n**********************")
                print("  \033[1;33mCRITICAL HIT!\033[0m  ")
                print("**********************")
                dmg = monster.hp - 25
            elif d20 > 16:
                dmg = random.randint(8, 11)
                print("\nSevaral traps hit their mark, but the dragon shakes free and takes to the sky again")
            else: 
                print("The dragon spins to avoid the worst of the attack and mighty wings take it out of reach")
                dmg = random.randint(2, 4)
        print("")
        monster.take_dmg(dmg)           

    def special_atk_melee(self, monster):
        d20 = random.randint(1, 20)
        rng = random.randint(1, 5)
        dmg = 10 + rng
        if hero.ranger_volley:
            print("You signal the rangers!")
            if d20 == 20:
                print("\n**********************")
                print("  \033[1;33mCRITICAL HIT!\033[0m  ")
                print("**********************")
                dmg *= 2
            elif d20 > 10:
                print("\nThe volley strikes true")
            else: 
                print("The dragon spins to avoid the worst of the attack")
                dmg = random.randint(2, 4)
        elif hero.slayer_sword:
            print("The sword thrums with energy, unleashing in a boom at your enemy!")
            if d20 == 20:
                print("\n**********************")
                print("  \033[1;33mCRITICAL HIT!\033[0m  ")
                print("**********************")
                dmg *= 2
            elif d20 > 10:
                print("\nThe beam strikes true")
            else: 
                print("The dragon dodges the worst of the attack")
                dmg = random.randint(2, 4)
        print("")
        monster.take_dmg(dmg)
     

class Monsters: #enemy stats and combat actions
    def __init__(self, hero, name, hp, atk, atkmin, atkmax, defense, poisoned, special, specdmg, specprep, specdesc):
        self.hero = hero
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_min_base = atkmin
        self.atk_max_base = atkmax
        self.defense = defense
        self.poisoned = poisoned
        self.special = special
        self.spec_dmg = specdmg
        self.spec_prep = specprep
        self.spec_desc = specdesc

    # atk min/max set as dynamic properties to scale with hero defense 
    @property
    def atk_min(self):
        return max(self.atk_min_base, hero.defense)
        
    @property
    def atk_max(self):
        return max(self.atk_max_base, hero.defense + 2)


    # === COMBAT LOOP - MONSTER ACTION ===
    def m_std_atk(self, hero):  
        print(f"{self.name} attacks!")
        d20 = random.randint(1,20)
        rng = (random.randint(self.atk_min, self.atk_max))
        dmg = max(0, self.atk - hero.defense + rng)
        if d20 == 20:
            print("\n**********************")
            print("⚔️  \033[1;31mCRITICAL HIT!\033[0m  ⚔️")
            print("**********************")
            dmg *= 2 
        elif d20 == 1:
            print(f"\n{self.name} Missed!")
            return
        
        if hero.block: #checks for block, halves dmg (rounded down)
            dmg //= 2
        
        hero.take_dmg(dmg)

    def m_special_prep(self, hero): #every 3rd round skip attack to prep special attack
        print("-------------------------------------------------------------------------")
        print(f"Watch out {hero.name}, the {self.name} {self.spec_prep}")
        print("----------------------------------------------------================-----\n")

    def m_special_atk(self, hero): #special attack every 4th round
        print("************************")
        print("💀------------------⚔️")
        print(f"        {self.special}        ")
        print("⚔️-------------------💀")
        print("************************")
        print(f"The {self.name} {self.spec_desc}\n")
        rng = (random.randint(self.atk_min,self.atk_max))
        dmg = max(0, self.spec_dmg - hero.defense + rng)
        if hero.fire_shield and hero.block:
            dmg = 0
        elif hero.block:
            dmg //= 2

        hero.take_dmg(dmg)

    def take_dmg(self, dmg): #applies dmg from hero attack
        print(f"{self.name} takes {dmg} damage")
        self.hp -= dmg
        if self.hp <= 0:
            print("*******************")
            print(color_text(f"{hero.name} defeated the {self.name}", "1;33"))
            print("*******************\n")
            print("\n-------------------------------------")
            hero.hp = hero.max_hp
        else:
            print(f"{self.name} has {self.hp} hp left\n")

    def take_poison_dmg(self):
        dmg = random.randint(1, 3)
        print(f"\n {self.name} takes {dmg} poison damage \n")
        self.hp -= dmg
        

    def dragon_air(self, hero):
        d20 = random.randint(1, 20)
        dodge = random.randint(1, 10)
        rng = (random.randint(self.atk_min,self.atk_max))

        if d20 <= 10:
            print("The dragon unleashes a torrent of fire from its gaping maw")
            if hero.fire_shield:
                dmg = 0
                print("\n You raise the Emberguard and the flames pass harmlessly around you ")
            else:
                dmg = max(0, self.spec_dmg - hero.defense)
        else:
            if d20 in (11, 12, 13, 14, 15):
                print("The dragon swoops low, dragging its tail like a spiked plow")
            else:
                print("The dragon pins its wings back diving straight at you!")
            dmg = max(0, self.atk - hero.defense + rng)
            if hero.block:
                dmg //= 2

        if dodge >= 7:
            if hero.fire_shield and d20 <= 10:  #no need to dodge if flame attack hits fire shield
                pass
            else:
                print("You roll out of the way\n")
        else:
            hero.take_dmg(dmg)

        
#hero = Hero("Coxx", 20, 20, 1, 1, 3, 1, False, 1, "Shortsword", "Wood Shield", "No Armor", False, False, False, False)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 1, False, 1, "Longsword", "Wood Shield", "No Armor", False, False, True, False)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 3, False, 1, "Longsword", "Wood Shield", "Leather Armor", False, False, True, False)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 3, False, 1, "Longsword", "Wood Shield", "Leather Armor", False, False, True, True)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 4, False, 1, "Longsword", "Leather Shield", "Leather Armor", False, False, True, False)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 4, False, 1, "Longsword", "Leather Shield", "Leather Armor", False, False, True, True)
hero = Hero("Coxx", 20, 20, 1, 1, 3, 5, False, 1, "Shortsword", "Emberguard", "Dwarven Mail", True, False, False, False)
#hero = Hero("Coxx", 20, 20, 3, 1, 3, 2, False, 1, "Longsword", "Emberguard", "Dwarven Mail", True, False, False, False)
#hero = Hero("Coxx", 20, 20, 5, 1, 3, 3, False, 1, "Slayer Sword", "Wood Shield", "Leather Armor", False, True, False, False)
#hero = Hero("Coxx", 20, 20, 5, 1, 3, 4, False, 1, "Slayer Sword", "Reinforced Shield", "Leather Armor", False, True, False, False)




wolf = Monsters(hero, "Wolf", 12, 2, 2, 4, 0, False, "none", 0, "", "")
roadbandit = Monsters(hero, "Bandit", 14, 3, 1, 3, 0, False, "none", 0, "", "")
durgrin = Monsters(hero, "Durgrin", 14, 2, 2, 4, 0, False, "none", 0, "", "")
troll = Monsters(hero, "Troll", 30, 2, 2, 5, 0, False, "RAMPAGE", 5, "is winding up for a devastating strike!", "roars and thrashes around wildly with his giant club")
goblin = Monsters(hero, "Goblin", 14, 3, 2, 4, 0, False, "none", 0, "", "")
orc = Monsters(hero, "Orc", 13, 2, 2, 5, 0, False, "none", 0, "", "")
spider = Monsters(hero, "Spider", 12, 3, 1, 3, 0, False, "none", 0, "", "")
forestbandit = Monsters(hero, "Forest Bandit", 12, 3, 2, 3, 0, False, "none", 0, "", "")
giantspider = Monsters(hero, "Giant Spider", 30, 4, 2, 6, 0, False, "Fang Leap", 5, "rears back hissing, ready to pounce!", "launches itself at you, fangs glinting, legs outstretched")
dragon = Monsters(hero, "Dragon", 75, 4, 3, 6, 1, False, "Fire Breath", 12, "stands and its throat begins to glow orange!", "spews flames that engulf you")

def color_text(text, color_code): 
    return f"\033[{color_code}m{text}\033[0m"

def pause(text = "Press Enter to continue..."):
    input(color_text(f"{text}", 36))

def gameover(hero):
    print(f"\nIt looks like {hero.name} won't be saving the village. Game over")
    sys.exit()

def combat(hero, monster): # === COMBAT LOOP FUNCTION ===
    round = 0
    while hero.hp > 0 and monster.hp > 0:
        round += 1
        time.sleep(1)
        print("********************************************")
        print(f"Round - {round}")
        print(f"{hero.name}: {hero.hp} HP     {monster.name}: {monster.hp} HP")
        valid_action = False 
        while not valid_action: #loops back if try to heal with no potions
            print("BATTLE OPTIONS") #should I add options to check HP? or always print hero/monster hp at top?
            print("   1- Attack ")
            print("   2- Block ") 
            print("   3- Heal Potion ")
            try:
                hero_action = int(input("Enter number 1-3 -- "))
                if hero_action == 1:
                    hero.std_atk(monster)
                    valid_action = True
                elif hero_action == 2:
                    hero.block_atk()
                    valid_action = True
                elif hero_action == 3:
                    if hero.potion > 0:
                        hero.heal_potion()
                        valid_action = True
                    else: 
                        print(f"Oh no! {hero.name} is out of potions") 
            except ValueError:
                print("please enter a number 1-3")
        if monster.hp <= 0:
            break
        elif monster.special != "none" and round > 2 and (round + 1) % 4 == 0: #prep special attack before every 4th round
            monster.m_special_prep(hero)
        elif monster.special != "none" and round % 4 == 0: #special attack every 4th round
            monster.m_special_atk(hero)
        else:
            monster.m_std_atk(hero) 
def final_battle_air(hero, monster):  # === COMBAT LOOP DRAGON IN AIR ===
    round = 0
    while monster.hp > 25:
        round += 1
        print("********************************************")
        print(f"Round - {round}")
        print(f"{hero.name}: {hero.hp} HP     {monster.name}: {monster.hp} HP")
        valid_action = False 
        while not valid_action: #loops back if try to heal with no potions
            print("BATTLE OPTIONS") #should I add options to check HP? or always print hero/monster hp at top?
            print("   1- Attack 🏹")
            print("   2- Block 🛡️") 
            print("   3- Heal Potion 💗")
            if hero.ranger_volley:
                print("   4- Ranger Volley ⭐")
            elif hero.slayer_sword:
                print("   4- Slayer Sword Blast ⭐")
            elif hero.fire_shield:
                print("   4- Call For Dwarven Traps ⭐")          

            try:
                hero_action = int(input("Enter number 1-4 -- "))
                if hero_action == 1:
                    hero.ranged_atk(monster)
                    valid_action = True
                elif hero_action == 2:
                    hero.block_atk()
                    valid_action = True
                elif hero_action == 3:
                    if hero.potion > 0:
                        hero.heal_potion()
                        valid_action = True
                    else: 
                        print(f"Oh no! {hero.name} is out of potions") 
                elif hero_action == 4:
                    if round % 2 != 0:  #only use special on odd turns
                        hero.special_atk_ranged(monster, round)
                        valid_action = True
                    else:
                        print("\nNot available this round\n")
            except ValueError:
                print("please enter a number 1-4")
        if monster.hp > 25:
            monster.dragon_air(hero)

    if hero.fire_shield:
        print("The dragon shrieks as the traps take hold and tear at its wing. It can no longer carry its weight in air")
    else:
        print("The dragon crashes to the ground with a shriek, its wing torn and fire sputtering from its jaws")

    print("The earth quakes with its rage\n")


def final_battle_ground(hero, monster):  # === COMBAT LOOP DRAGON ON GROUND ===
    round = 0
    while monster.hp > 0:
        round += 1
        print("********************************************")
        print(f"Round - {round}")
        print(f"{hero.name}: {hero.hp} HP     {monster.name}: {monster.hp} HP")
        valid_action = False 
        while not valid_action: #loops back if try to heal with no potions
            print("BATTLE OPTIONS") 
            print("   1- Attack ⚔️")
            print("   2- Block 🛡️") 
            print("   3- Heal Potion 💗")
            if hero.ranger_volley:
                print("   4- Ranger Volley ⭐")
            elif hero.slayer_sword:
                print("   4- Slayer Sword Blast ⭐")

            try:
                hero_action = int(input("Enter number 1-3 -- ")) if hero.fire_shield else int(input("Enter number 1-4 -- "))
                if hero_action == 1:
                    hero.std_atk(monster)
                    valid_action = True
                    if hero.venom and not monster.poisoned:
                        print("The dragon recoils as the venom does its job. The beast is poisoned!")
                        monster.poisoned = True
                elif hero_action == 2:
                    hero.block_atk()
                    valid_action = True
                elif hero_action == 3:
                    if hero.potion > 0:
                        hero.heal_potion()
                        valid_action = True
                    else: 
                        print(f"Oh no! {hero.name} is out of potions") 
                elif hero_action == 4 and not hero.fire_shield:
                    if round % 2 != 0:  #only use special on odd turns
                        hero.special_atk_melee(monster)
                        valid_action = True
                    else:
                        print("Not available this round")
            except ValueError:
                print("please enter a number")
        
        if monster.hp <= 0:
            break
        elif monster.poisoned:
            monster.take_poison_dmg()
            if monster.hp <= 0:
                break

        if monster.special != "none" and round > 2 and (round + 1) % 4 == 0: #prep special attack before every 4th round
            monster.m_special_prep(hero)
        elif monster.special != "none" and round % 4 == 0: #special attack every 4th round
            monster.m_special_atk(hero)
        else:
            d10 = random.randint(1, 10)
            if d10 <= 5:
                print("The dragon slashes at you with its claws")
            elif d10 in (6, 7, 8):
                    print("The dragon quickly spins, hammering you with its tail")
            else:
                print("The dragon snarls and chomps at you, aiming to dismember!")
            monster.m_std_atk(hero)


def final_boss():
    print("---------------------------------------------------------------------------------------------------------------------")
    print("The wind carries the scent of ash as you return home. The village seems far too quiet and your heart races")
    print("As you begin to fear the worst, a window pops open and an old woman hisses 'off the streets you fool, it's not safe'")
    print(f"Her face softens a bit as she recognizes you. 'Oh, apologies {hero.name}, we keep ourselves indoors lately'") 
    print("'As meager a snack as I'd be, best not tempt the flying beast. Speaking of, shouldn't you be up at the farm with everyone else?'")
    print("She explains the Elder has brought everyone to the northeast plains to help prepare the old abandoned farm for the dragon")
    print("-" * 15)
    print("The Elder greets you with open arms when you arrive at the farm")
    print(f"'Welcome back {hero.name}!!!'")
    if hero.fire_shield:
        print("'And a very warm welcome to the Hill Dwarves, your aid shall not be forgotten'")
    elif hero.ranger_volley:
        print("'And a very warm welcome to the Forest Rangers, your aid shall not be forgotten'")
    elif hero.slayer_sword:
        print("'That sword certainly looks the part, let us hope it lives up to its legend'")

    print("'All able-bodied villagers have gathered here in preparation for your confrontation'")
    print("'There has been some debate ")

    print("The dwarves hammer iron stakes into carts and weld makeshift barricades")
    print("The rangers sharpen arrows and find hiding spots to blend into the fields like shadows")
    print("When you draw the slayer's sword, it's glow cuts through dusk like fire through fog. It pulses eagerly")
    print("You coat your weapon in the green venom, careful not to let it touch your skin")

    print("The field is now a battlefield-in-waiting. A makeshift corral holds terrified livestock in a circle of bait")
    print("")

    print("The sun hangs low when the first scream splits the sky")
    print("The clouds ripple as a shadow breaks through. With a sound like mountains cracking, the dragon dives")
    print("Wings stretched like sails, the creature descends toward the bait")

    print("Someone throws you a bow and a quiver. 'You need to bring the dragon to ground, you can't fight it in the air!")

    final_battle_air(hero, dragon)


    final_battle_ground(hero, dragon)


def simulate_combat(hero, monster_template, runs=100):
    print(f"\nSimulating {runs} battles vs {monster_template.name}...\n")
    wins = 0
    losses = 0
    total_rounds = 0
    total_potions = 0

    for i in range(runs):
        # Create fresh instances
        test_hero = Hero(
            name=hero.name,
            maxhp=hero.max_hp,
            hp=hero.max_hp,
            atk=hero.atk,
            atkmin=hero.atk_min,
            atkmax=hero.atk_max,
            defense=hero.defense,
            block=False,
            potion=1,
            sword=hero.sword,
            shield=hero.shield,
            armor=hero.armor,
            fireshield=False,
            slayersword=False,
            rangervolley=False,
            venom=False
        )

        test_monster = Monsters(
            hero=test_hero,
            name=monster_template.name,
            hp=monster_template.hp,
            atk=monster_template.atk,
            atkmin=monster_template.atk_min_base,
            atkmax=monster_template.atk_max_base,
            defense=monster_template.defense,
            poisoned=False,
            special=monster_template.special,
            specdmg=monster_template.spec_dmg,
            specprep=monster_template.spec_prep,
            specdesc=monster_template.spec_desc
        )

        round_count = 0

        while test_hero.hp > 0 and test_monster.hp > 0:
            round_count += 1
            # Simulated simple AI
            if test_hero.hp <= 8 and test_hero.potion > 0:
                test_hero.heal_potion()
            elif round_count % 4 == 0:
                test_hero.block_atk()
            else:
                test_hero.std_atk(test_monster)

            if test_monster.hp <= 0:
                break

            if test_monster.special != "none" and round_count > 2 and (round_count + 1) % 4 == 0:
                test_monster.m_special_prep(test_hero)
            elif test_monster.special != "none" and round_count % 4 == 0:
                test_monster.m_special_atk(test_hero)
            else:
                test_monster.m_std_atk(test_hero)

        if test_hero.hp > 0:
            wins += 1
        else:
            losses += 1
        total_rounds += round_count
        total_potions += 1 - test_hero.potion

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {wins / runs * 100:.1f}%")
    print(f"Avg Rounds per Battle: {total_rounds / runs:.1f}")
    print(f"Avg Potions Used: {total_potions / runs:.2f}")

def simulate_final_boss(hero, dragon_template, runs=100):
    print(f"\nSimulating {runs} battles vs Dragon (Full Final Battle)...\n")
    wins = 0
    losses = 0
    total_rounds = 0
    total_potions = 0

    for _ in range(runs):
        test_hero = Hero(
            name=hero.name,
            maxhp=hero.max_hp,
            hp=hero.max_hp,
            atk=hero.atk,
            atkmin=hero.atk_min,
            atkmax=hero.atk_max,
            defense=hero.defense,
            block=False,
            potion=3,
            sword=hero.sword,
            shield=hero.shield,
            armor=hero.armor,
            fireshield=hero.fire_shield,
            slayersword=hero.slayer_sword,
            rangervolley=hero.ranger_volley,
            venom=hero.venom
        )

        test_dragon = Monsters(
            hero=test_hero,
            name=dragon_template.name,
            hp=dragon_template.hp,
            atk=dragon_template.atk,
            atkmin=dragon_template.atk_min_base,
            atkmax=dragon_template.atk_max_base,
            defense=dragon_template.defense,
            poisoned=False,
            special=dragon_template.special,
            specdmg=dragon_template.spec_dmg,
            specprep=dragon_template.spec_prep,
            specdesc=dragon_template.spec_desc
        )

        round_count = 0

        # === AIR PHASE ===
        while test_dragon.hp > 25 and test_hero.hp > 0:
            round_count += 1
            if test_hero.hp <= 8 and test_hero.potion > 0:
                test_hero.heal_potion()
            elif round_count % 2 != 0 and (test_hero.ranger_volley or test_hero.slayer_sword or test_hero.fire_shield):
                test_hero.special_atk_ranged(test_dragon, round_count)
            elif round_count % 4 == 0:
                test_hero.block_atk()
            else:
                test_hero.ranged_atk(test_dragon)

            if test_dragon.hp > 25:
                test_dragon.dragon_air(test_hero)

        # === GROUND PHASE ===
        while test_dragon.hp > 0 and test_hero.hp > 0:
            round_count += 1
            if test_hero.hp <= 8 and test_hero.potion > 0:
                test_hero.heal_potion()
            elif round_count % 2 != 0 and (test_hero.ranger_volley or test_hero.slayer_sword):
                test_hero.special_atk_melee(test_dragon)
            elif round_count % 4 == 0:
                test_hero.block_atk()
            else:
                test_hero.std_atk(test_dragon)
                if test_hero.venom and not test_dragon.poisoned:
                    test_dragon.poisoned = True

            if test_dragon.poisoned and test_dragon.hp > 0:
                test_dragon.take_poison_dmg()

            if test_dragon.hp > 0:
                if round_count > 2 and (round_count + 1) % 4 == 0:
                    test_dragon.m_special_prep(test_hero)
                elif round_count % 4 == 0:
                    test_dragon.m_special_atk(test_hero)
                else:
                    test_dragon.m_std_atk(test_hero)

        if test_hero.hp > 0:
            wins += 1
        else:
            losses += 1

        total_rounds += round_count
        total_potions += 3 - test_hero.potion

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Win Rate: {wins / runs * 100:.1f}%")
    print(f"Avg Rounds per Battle: {total_rounds / runs:.1f}")
    print(f"Avg Potions Used: {total_potions / runs:.2f}")


def balance_table(hero, enemies, runs=100):
    print("\n=== Combat Balance Table ===")
    print(f"Simulating {runs} battles per enemy...\n")

    results = []

    for enemy in enemies:
        wins = 0
        losses = 0
        total_rounds = 0
        total_potions = 0

        for _ in range(runs):
            test_hero = Hero(
                name=hero.name,
                maxhp=hero.max_hp,
                hp=hero.max_hp,
                atk=hero.atk,
                atkmin=hero.atk_min,
                atkmax=hero.atk_max,
                defense=hero.defense,
                block=False,
                potion=2,
                sword=hero.sword,
                shield=hero.shield,
                armor=hero.armor,
                fireshield=False,
                slayersword=False,
                rangervolley=False,
                venom=False,
            )

            test_enemy = Monsters(
                hero=test_hero,
                name=enemy.name,
                hp=enemy.hp,
                atk=enemy.atk,
                atkmin=enemy.atk_min_base,
                atkmax=enemy.atk_max_base,
                defense=enemy.defense,
                poisoned=False,
                special=enemy.special,
                specdmg=enemy.spec_dmg,
                specprep=enemy.spec_prep,
                specdesc=enemy.spec_desc
            )

            round_count = 0
            while test_hero.hp > 0 and test_enemy.hp > 0:
                round_count += 1
                if test_hero.hp <= 8 and test_hero.potion > 0:
                    test_hero.heal_potion()
                elif round_count % 4 == 0:
                    test_hero.block_atk()
                else:
                    test_hero.std_atk(test_enemy)

                if test_enemy.hp <= 0:
                    break

                if test_enemy.special != "none" and round_count > 2 and (round_count + 1) % 4 == 0:
                    test_enemy.m_special_prep(test_hero)
                elif test_enemy.special != "none" and round_count % 4 == 0:
                    test_enemy.m_special_atk(test_hero)
                else:
                    test_enemy.m_std_atk(test_hero)

            if test_hero.hp > 0:
                wins += 1
            else:
                losses += 1

            total_rounds += round_count
            total_potions += 2 - test_hero.potion

        win_rate = wins / runs * 100
        avg_rounds = total_rounds / runs
        avg_potions = total_potions / runs

        results.append((enemy.name, wins, losses, win_rate, avg_rounds, avg_potions))

    # After all simulations, print the table header and rows
    print(f"{'Enemy':<15}{'Wins':<6}{'Losses':<8}{'Win %':<7}{'Avg Rounds':<12}{'Avg Potions'}")
    print("-" * 60)

    for r in results:
        print(f"{r[0]:<15}{r[1]:<6}{r[2]:<8}{r[3]:<7.1f}{r[4]:<12.1f}{r[5]:.2f}")

boss = False

#simulate_combat(hero, goblin, 100)

'''
with open("combat_results.txt", "w") as f:
    sys.stdout = f
    enemies_to_test = [wolf, roadbandit, durgrin, goblin, orc, spider, forestbandit, troll, giantspider, dragon]
    balance_table(hero, enemies_to_test, runs=100)
    sys.stdout = sys.__stdout__  # Reset output back to console


#balance_table(hero, enemies_to_test, runs=100)
print("Done running balance table")
'''

simulate_final_boss(hero, dragon, runs=100)
