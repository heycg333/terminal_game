
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
        if self.hp <= 0:
            print("💀💀💀💀💀💀💀💀")
            print(f"{self.name} has perished")
            print("💀💀💀💀💀💀💀💀")
            gameover(hero)
        else:
            print(f"{self.name} has {self.hp} hp left\n")

    def ranged_atk(self, monster): #used in final battle
        d20 = random.randint(1, 20)
        if d20 == 20:
            print("\n**********************")
            print("⚔️  \033[1;33mCRITICAL HIT!\033[0m  ⚔️")
            print("**********************")
            dmg = monster.hp - 25
        else:
            dmg = 1
            print(f"\n{self.name}'s arrow hits. It will take much more to bring the beast down!")
            
        monster.take_dmg(dmg)


    def special_atk_ranged(self, monster, round): #used in final battle air phase, special atk depends on which quest completed
        d20 = random.randint(1, 20)
        print()
        if hero.ranger_volley:
            print("You signal the rangers!")
            if round > 5 or d20 == 20:
                print("\n**********************")
                print("⚔️  \033[1;33mCRITICAL HIT!\033[0m  ⚔️")
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
                print("⚔️  \033[1;33mCRITICAL HIT!\033[0m  ⚔️")
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
                print("⚔️  \033[1;33mCRITICAL HIT!\033[0m  ⚔️")
                print("**********************")
                dmg = monster.hp - 25
            elif d20 > 16:
                dmg = random.randint(8, 11)
                print("\nSevaral traps hit their mark, but the dragon shakes free and takes to the sky again")
            else: 
                print("The dragon spins to avoid the worst of the attack and mighty wings take it out of reach")
                dmg = random.randint(2, 4)
        print()
        monster.take_dmg(dmg)           

    def special_atk_melee(self, monster): #final battle - ground phase
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
        print()
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
        print("⚠️-------------------------------------------------------------------------⚠️")
        print(f"Watch out {hero.name}, the {self.name} {self.spec_prep}")
        print("⚠️----------------------------------------------------================-----⚠️\n")

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
            print("🎉🎉🎉*******************🎉🎉🎉")
            print(color_text(f"{hero.name} defeated the {self.name}", "1;33"))
            print("🎉🎉🎉*******************🎉🎉🎉\n")
            print("\n-------------------------------------")
            hero.hp = hero.max_hp
        else:
            print(f"{self.name} has {self.hp} hp left\n")

    def take_poison_dmg(self):
        dmg = random.randint(1, 3)
        print(f"\n☠️ {self.name} takes {dmg} poison damage ☠️\n")
        self.hp -= dmg
        

    def dragon_air(self, hero): #final battle 
        d20 = random.randint(1, 20)
        dodge = random.randint(1, 10)
        rng = (random.randint(self.atk_min,self.atk_max))

        if d20 <= 10:
            print("The dragon unleashes a torrent of fire from its gaping maw")
            if hero.fire_shield:
                dmg = 0
                print("\n🛡️ You raise the Emberguard and the flames pass harmlessly around you 🛡️")
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

        

hero = Hero("Hero", 20, 20, 1, 1, 3, 1, False, 3, "Shortsword", "Wood Shield", "No Armor", False, False, False, False)

wolf = Monsters(hero, "Wolf", 12, 2, 2, 4, 0, False, "none", 0, "", "")
roadbandit = Monsters(hero, "Bandit", 14, 3, 1, 3, 0, False, "none", 0, "", "")
durgrin = Monsters(hero, "Durgrin", 14, 2, 2, 4, 0, False, "none", 0, "", "")
troll = Monsters(hero, "Troll", 30, 2, 2, 5, 0, False, "RAMPAGE", 5, "is winding up for a devastating strike!", "roars and thrashes around wildly with his giant club")
goblin = Monsters(hero, "Goblin", 12, 3, 1, 4, 0, False, "none", 0, "", "")
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
    print(f"\nIt looks like {hero.name} won't be saving the village")
    print("GAME OVER")
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
            print("   1- ⚔️  Attack")
            print("   2- 🛡️  Block") 
            print("   3- 💗 Heal Potion")
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
            print("   1- 🏹 Attack ")
            print("   2- 🛡️ Block") 
            print("   3- 💗 Heal Potion")
            if hero.ranger_volley:
                print("   4- ⭐ Ranger Volley")
            elif hero.slayer_sword:
                print("   4- ⭐ Slayer Sword Blast")
            elif hero.fire_shield:
                print("   4- ⭐ Call For Dwarven Traps")          

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
    
    pause("press Enter to get out of the way!")
    dragon_drops()

    print("The earth quakes with its rage\n")
    print("Now it's time to end this!")
    pause("press Enter to charge forward\n")


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
            print("   1- ⚔️ Attack")
            print("   2- 🛡️ Block") 
            print("   3- 💗 Heal Potion")
            if hero.ranger_volley:
                print("   4- ⭐ Ranger Volley")
            elif hero.slayer_sword:
                print("   4- ⭐ Slayer Sword Blast")

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


def dragon_drops():
    frames = [
        "          🐉   ", 
        "         🐉    ", 
        "        🐉     ", 
        "     🐉🔥      ", 
        "   🐉🔥🔥       ",
        " 💥🔥🔥🔥🔥💥     ",
    ]

    for i in frames:
        print(i)
        time.sleep(0.3)


# === DWARVES QUEST ===
def quest1():
    #choose travel route - determines who combat will be with
    print("The Dwarves live in the Copper Hills to the south. You can either - ")
    print("  1- Take the well-traveled mining trail road, following it south then cut east to the Copper Hills")
    print("  2- Take a riskier, more direct route and head southeast across the plains")
    route1 = 0
    while route1 not in (1,2):
        try:
            route1 = int(input("Choose your route 1-2 -- \n"))
            if route1 == 1:
                print("Along the road you encounter an angry wolf. Get ready to fight!")
                combat(hero, wolf)
            elif route1 == 2: #harder route gains rewards
                print("You come across a bandit camp and 2 charge you. Get ready to fight!")
                combat(hero, roadbandit)
                print("(GAIN LONGSWORD)")
                print("(GAIN 1 10hp HEAL POTION)")
                hero.sword = "Longsword"
                hero.potion += 1
                hero.atk += 2
                hero.equipment_check()
            else:
                print("please choose a route 1-2")
        except ValueError:
            print("please enter a number 1-2")

    # === ARRIVE QUEST LOCATION ===

    print("\n\nYou arrive at the gates of the dwarven stronghold built into the rock face of the Copper Hills")
    print("A guard shouts down 'State your business here!'")
    print("You shout back - ")
    print("  1- I need to speak to your chief. My village needs help defending from the dragon")
    print("  2- I've heard the hill dwarves make the best ale - I have my doubts so I'm here to put that to the test")
    dwarfQ1 = 0
    while dwarfQ1 not in (1,2):
        try:
            dwarfQ1 = int(input("\nChoose your response 1-2 --\n"))
            if dwarfQ1 == 1:
                print("\nThe guard laughs. 'You are not fit to address the Thane. Durgrin, go teach this whelp a lesson.'")
                print("The gate opens and a burly dwarf approaches cracking his knuckles. Get ready to fight!")
                combat(hero, durgrin)
                print("Durgrin dusts himself off, laughing as you help him up")
                print("'I underestimated you, follow me friend, I could use a drink'")
            elif dwarfQ1 == 2:
                print("\nThe guard scowls. 'There is NONE better! Durgrin! Open the gates and show this fool to the tavern.'")
                pause()
            else:
                print("please choose a response 1-2")
        except ValueError:
            print("please enter a number 1-2")


    # === ENTER DWARVEN STRONGHOLD ===
    time.sleep(2)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Durgrin leads you through the gate into a long stone corridor sloping downwards. Glowing lanterns flicker above, casting shadows along the carved stone")
    print("You pass through an archway and emerge into a large open marketplace. The clinking of hammer on anvil echoes all around, a backdrop to gruff voices haggling at each vendor cart")
    print("Suddenly a group of heavily armored dwarves marches up and orders you to halt. 'Thaneguard - on your best behavior now' Durgrin whispers")
    print("'By order of Thane Brogdin, you are to come with us, outsider'")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("You respond - ")
    print("  1 - Ok, lead the way")
    print("  2 - I demand to know where you're taking me")
    print("  3 - Sure, but after I get some ale")
    dwarfQ2 = 0
    while dwarfQ2 not in (1,2,3):
        try:
            dwarfQ2 = int(input("\nChoose your response 1-3 --\n"))
            if dwarfQ2 == 1:
                print("\nDurgrin nods, 'Wise choice'. You follow the guards past the marketplace to a towering set of bronze doors.")
                print("Inside, the throne room stretches upward into a dome with intricate ornamental etchings spiraling up the stone")
            elif dwarfQ2 in (2,3):
                print("\n'Insolent whelp! We'll teach you manners!' You're struck in the head and knocked unconscious")
                hero.take_dmg(5)
                print("---------------------------------------------------------------------------------------------")
                time.sleep(2)
                print("\nYou awaken on the floor of a large room stretching upward into a dome. Rubbing your head you look around and realize you're in the throne room")
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
                pause()

            else:
                print("please choose a response 1-3")
        except ValueError:
            print("please enter a number 1-3")

    # === DWARVEN THRONEROOM ===
    time.sleep(1)
    print("Thane Brogdin's throne sits on a raised dais, carved from a single slab of granite with copper runes twisting up the armrests")
    print("The Thane watches you with deep-set eyes, his face expressionless and unreadable.")
    print("You feel a chill - his stare is every bit as cold as the polished stone surrounding him")
    pause()
    print("His advisor Ori, an older dwarf with a beard like braided chainmail, breaks the silence first -\n")
    print("'It was only a matter of time before the humans came seeking shelter. Those who choose to live under the sky will always be at the mercy of what falls from it'")
    time.sleep(1)
    print("\nYou respond - ")
    print("  1 - Better the open sky than a hole in the ground")
    print("  2 - It's true, we seek protection and aid from the brave and mighty dwarves of the Copper Hills")
    print("  3 - Say nothing. Let the Thane speak first")

    dwarfQ3 = 0
    while dwarfQ3 not in (1,2,3):
        try:
            dwarfQ3 = int(input("\nChoose your response 1-3 --\n"))
            if dwarfQ3 == 1:
                print("\nThe advisor's nostrils flare and his eyes shoot daggers. He raises an arm, taking a deep breath and readying a verbal lashing")
                print("Thane Brogdin's booming laughter interrupts. 'This one has some courage, settle yourself Ori, we shall hear out our visitor'")
            elif dwarfQ3 == 2:
                print("\n'Sniveling worm, do not insult us with your attempts to barter with flattery' Ori snarls")
                print("The Thane eyes you with thinly-veiled disdain")
            elif dwarfQ3 == 3:
                print("\nYou hold your tongue and look to the Thane")
            else:
                print("please choose a response 1-3")
        except ValueError:
            print("please enter a number 1-3")
    
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Thane Brogdin raises a gauntleted fist, instantly silencing the room\n")
    time.sleep(1)
    print("'You come here seeking dwarven steel to protect your people, bringing great risk to mine'")
    print("'Why should we face your dragon? Why should dwarven blood pay for your salvation?'\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("How will you convince the Thane - ")
    print("  1 - It is the right thing to do")
    print("  2 - If we fall, the dragon will come for your great halls next")
    print("  3 - We will share whatever treasure the dragon has hoarded")
    print("  4 - You'll earn glory that will echo through stone forever'")

    dwarfQ4 = 0
    bonusquest = False
    while dwarfQ4 not in (1,2,3,4):
        try:
            dwarfQ4 = int(input("\nChoose your response 1-4 --\n"))
            if dwarfQ4 == 1:
                print("\n'Noble, yet naive. The only right thing to do is what's best for my people'")
            elif dwarfQ4 == 2:
                print("\n'A fair warning, mayhap a true one")
            elif dwarfQ4 in (3,4):
                print("\nYou see a flash in the Thane's eyes - you have clearly piqued his interest")
            else:
                print("please choose a response 1-4")
        except ValueError:
            print("please enter a number 1-4")
    if dwarfQ4 == 1 and dwarfQ3 == 2:
        print("\n'We'll not bleed for humans who run to us only when their roof catches fire. You'll find no allies here'\n")
        time.sleep(2)
        questsuccess = False
    elif dwarfQ4 in (2,4) and dwarfQ3 == 2:
        print("\n'You come seeking aid with naught but words for compensation. I grow tired'")
        print("Thane Brogdin stands and turns to leave. Do you -")
        print("  1 - Plead for aid, at the risk of angering the Thane")
        print("  2 - Quietly leave")
        dwarfQ5 = 0
        while dwarfQ5 not in (1,2):
            try:
                dwarfQ5 = int(input("\nChoose your response 1-2 --\n"))
                if dwarfQ5 == 1:
                    print("\nYou push the matter, pleading for your village one last time")
                    print("The Thane pauses. With his back turned, you cannot read his face, but nods his head, seemingly in consideration")
                    bonusquest = True
                elif dwarfQ5 == 2:
                    questsuccess = False
                    time.sleep (1)
                else:
                    print("please choose a response 1-2")
            except ValueError:
                print("please enter a number 1-2")
    elif dwarfQ4 in (3,4) and dwarfQ3 != 2:
        questsuccess = True
    else:
        bonusquest = True
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

    # === QUEST RESOLUTION === 
    if bonusquest: #combat miniboss 
        time.sleep(2)
        print("'I remain unconvinced, but I shall give you opportunity to prove your worth'")
        print("'A troll has attacked our miners and must be dealt with. Do so, and you may yet deserve dwarven steel'")
        print("'Ori, send an escort to take our guest into the mines. We shall see how strong they are'\n")
        pause("press Enter to venture into the mine")
        print("-" * 30)
        print("\nAs you descend deeper into the mines, a foul, rotting musk assaults your nostrils")
        print("Something shuffles ahead. A growl echoes from the shadows, low, guttural, and hungry")
        time.sleep(2)
        print("A hulking figure lurches into view, dragging a massive club that could crush a clydesdale")
        print("Gray skin slick with cave slime parts to reveal jagged teeth bared in a twisted grin")
        time.sleep(1)
        print("You've found the troll........")
        time.sleep(1)
        print("and it looks hungry\n\n")
        combat(hero, troll)
        time.sleep(1)
        print("\nYou return to the throne room covered in troll blood")
        questsuccess = True
    else:
        pass

    if questsuccess: #gain armor and fire shield
        time.sleep(1)
        print("\nThane Brogdin nods approvingly. 'I can see now there is strength in you, mayhap enough to face the challenge ahead'")
        print("'You may have the courage to face dragon fire, but you lack the equipment. Easily remedied.'")
        print(f"'Ori, prepare a room for our guest. Go and rest {hero.name}, we shall speak more tomorrow'")
        pause("press Enter to retire to your room")
        hero.sleep()
        print("---------------------------------------------------------------------------------------------------------------------")
        print("In the morning, you are summoned back to the throne room")
        time.sleep(0.5)
        print("\nThane Brogdin welcomes you and presents you with the finest dwarven mail you have ever seen")
        print("'My smiths worked through the night. This armor is light enough for your kind, strong enough to turn a dragon's fang'")
        time.sleep(2)
        print("\nAnother smith steps forward and presents you with a dark shield, its surface shimmers in the firelight")
        print("'And this, the Emberguard. Quenched in molten obsidian, cooled in troll-blooded oil. No fire will blister your skin while this guard is raised'")
        time.sleep(2)
        print("\n(GAIN DWARVEN MAIL ARMOR)")  
        print("(GAIN EMBERGUARD SHIELD)")  
        print("(GAIN 2 10hp HEAL POTIONS)")  
        hero.armor = "Dwarven Mail"
        hero.shield = "Emberguard Shield"
        hero.potion += 2
        hero.defense += 4
        hero.fire_shield = True
        hero.equipment_check()
        time.sleep(2)
        print("-----------------------------------")
        print("'Take these gifts, may they serve you well in the battle ahead. I send with you a regiment to help defend your village.'")
        print(f"'May the Stonefather guide your sword and shield your back. Farewell {hero.name}'")
        hero.hp = hero.max_hp
        pause()

# === DRAGON SLAYER TOMB QUEST ===
def quest2():
    door_puzzle = ["🛡️", "🛡️", "🛡️", "🛡️"]

    def tomb_door(door_puzzle):  
        print("The shield symbols glow faintly with pale blue runes. You try to rotate the discs but they won't budge")
        print("Around the outer ring of each disc, you notice faint carvings: not just shields... but swords as well")
        print("Seems as if they’re meant to turn and reveal a second form")
        print("Below the door, a short inscription reads:")
        print("'When swords replace shields, the slayer shall rise again'")
        print(door_puzzle)
        pause()

    #choose travel route - determines who combat will be with
    print("\nThe tomb lies on the coast to the west. You can either - ")
    print("  1- Take the well-traveled merchant road, following it north from the village and west to the coast")
    print("  2- Take a riskier, more direct route and travel an old pilgrim trail west through the hills")
    route1 = 0
    while route1 not in (1,2):
        try:
            route1 = int(input("\nChoose your route 1-2 --\n"))
        except ValueError:
            print("please enter a number 1-2")
    if route1 == 1:
        print("\nAlong the road you encounter an angry wolf. Get ready to fight!")
        combat(hero, wolf)
    else:
        print("\nAs you ascend the winding trail goblins leap out of hiding, weapons raised. Get ready to fight!")
        combat(hero, goblin)
        print("\nAmong the hoard of goblin trash you notice a shield with solid metal plating circling the rim")
        time.sleep(1)
        print("GAIN REINFORCED SHIELD")
        hero.shield = "Reinforced Shield"
        hero.defense += 1
        hero.equipment_check()

    pause()
    print("\nCarved into a cliff overlooking the sea, the tomb's entrance yawns like the mouth of a forgotten god")
    print("Weathered statues of armored warriors flank the stairs, their swords pointed downward in eternal vigil")
    time.sleep(2)
    print("Inside, the air is dry and cold. The stone walls bear faded murals")
    print("The scenes depict a lone warrior slaying beasts, rallying soldiers, and, at last, falling beneath a dragon’s shadow.")
    pause()
    print("\nYou step into a wide, circular chamber. The air here is still and cold, untouched by time")
    print("Directly ahead stands a massive stone door etched with patterns that gleam faintly under your torchlight")
    time.sleep(2)
    print("\nEmbedded into the face of the door are four round, bronze-like discs displaying shield symbols")
    print("Flanking the door on both sides are 4 short hallways leading to other rooms, each labeled with some kind of trial")
    
    room_options = {
        1: tomb_door,
        2: tomb_w_room,
        3: tomb_nw_room,
        4: tomb_ne_room,
        5: tomb_e_room
    }

    while door_puzzle != ["⚔️", "⚔️", "⚔️", "⚔️"]:
        time.sleep(1)
        room_explore = 0
        print("-" * 30)
        print("1 - Examine door")
        print("2 - Trial of Names - west passage")
        print("3 - Trial of Light - northwest passage")
        print("4 - Trial of Balance - northeast passage")
        print("5 - Trial of Sound - east passage")
        print("-" * 30)
        while room_explore not in (1,2,3,4,5):
            try:
                room_explore = int(input("Explore 1-5 --"))
            except ValueError:
                print("please enter a number 1-5")
        
        room_options[room_explore](door_puzzle)

    print("The stone doors grind open and your skin begins to tingle")
    time.sleep(1)
    print("Inside lies a massive stone sarcophagus, draped in faded crimson cloth and topped with floral wreaths")
    time.sleep(1)
    print("At its base, a sword rests — blade gleaming with a faint inner light that grows as you approach")
    print("A faint voice whispers - 'It senses your need and has awakened.'\n")
    pause("press Enter to pick up the sword")
    print("\nThe blade thrums in your hands, seeming eager to be put to use")
    time.sleep(1)
    print("'Quench its thirst for dragon's blood, and then return it here to its slumber'")
    time.sleep(1)
    print("You nod your head in silent agreement and exit the tomb, eager to feed your new companion")
    time.sleep(2)

    hero.slayer_sword = True
    print("GAIN SLAYER SWORD")
    hero.sword = "Slayer Sword"
    hero.atk += 4
    hero.atk_min += 1
    hero.atk_max += 2
    hero.equipment_check()
    hero.hp = hero.max_hp

    pause()

# === ROOM PUZZLE SOLVED ===
def puzzle_trigger(door_puzzle):
    print("In the distance, you hear stone grinding — deep and resonant. You rush back to the burial chamber entrace")
    time.sleep(2)
    print("One of the shield symbols turns with a heavy click, and a sword now gleams where a shield once stood")
    time.sleep(1)
    print(door_puzzle)
    pause()


# === TRIAL OF NAMES ===
def tomb_w_room(door_puzzle): 
    exit = False
    def inspect_plates():
        nonlocal exit
        print("\nIn the center of the plates an inscription reads 'Honor the Dragon Slayer'")
        print("1 - step on Kellumn Ironhand")
        print("2 - step on Ser Bryn of the Vale")
        print("3 - step on Kael the Nameless")
        print("4 - step on Durek Flameborn")
        print("5 - back away")
        plates = 0
        while plates not in (1,2,3,4,5):
            try:
                plates = int(input("\nChoose 1-5 -- incorrect selections have consequence"))
            except ValueError:
                print("please enter a number 1-5")
        if plates == 5:
            return
        elif plates == 3:
            print("\nThe plate makes a satisfying click as it falls into place and the name begins to glow")
            door_puzzle[0] = "⚔️"
            time.sleep(1)
            puzzle_trigger(door_puzzle)
            exit = True
        else:
            print("🩸" * 15)
            print("A flash of pain rushes up your leg as small spikes drive into your foot")
            print("A voice whispers - 'You chose poorly'")
            time.sleep(1)
            hero.take_dmg(5)

    def inspect_statue():
        print("The inscription reads - ")
        print("He walked alone where fire fell,")
        print("No crown, no kin, no tale to tell.")
        print("No banners waved, no crowds adored —")
        print("Yet still, the beast fell to his sword.")

    def inspect_table():
        print("A stone scale, perfectly level. Etched on the base it reads - ")
        print("Blade and bone, equal in death. Wood tips the balance")        
    explore_options = {
        1: inspect_plates,
        2: inspect_statue,
        3: lambda: print("Depicts three knights, all bearing house sigils. One figure stands apart — weapon drawn, no sigil on his cloak"),
        4: inspect_table
    }

    # === ROOM DESCRIPTION ===
    time.sleep(1)
    print("\nAs you enter the room you are confronted with an imposing mural of a warrior standing atop a fallen dragon")
    print("He lifts his glowing sword to the sky in celebration of this great victory")
    print("\nBelow the mural on the floor are 4 pressure plates, each with a name written on them")
    print("On another wall there is a faded banner next to a cracked statue of a knight")
    print("A small table has what looks like a balanced stone scale")
    while not exit:
        pause()
        print()        
        print("-" * 30)
        print("1 - Inspect the named plates")
        print("2 - Inspect statue")
        print("3 - Inspect faded banner")
        print("4 - Inspect small table")
        print("5 - Leave room")
        print("-" * 30)

        explore = 0
        while explore not in (1,2,3,4,5):
            try:
                explore = int(input("\nChoose 1-5 --\n"))
            except ValueError:
                print("please enter a number 1-5")
        print("")
        if explore == 5:
            exit = True
        else:
            time.sleep(0.5)
            explore_options[explore]()


# === TRIAL OF LIGHT ===
def tomb_nw_room(door_puzzle):  
    exit = False

    def inspect_pillars():
        nonlocal exit
        correct_order = [2, 3, 1, 4]
        light_order = []
        print("\nAbove each sconce is a symbol")
        print("1 - A rising sun")
        print("2 - A setting sun")
        print("3 - A crescent moon")
        print("4 - A bright, full sun")
        start_lighting = 0
        while start_lighting != "y" and start_lighting != "n":
            print("\nFailure will have consequence")
            start_lighting = input("Are you ready to begin lighting sequence? y/n -- \n").lower()
            if start_lighting == "y":
                continue
            elif start_lighting == "n":
                return
            else:
                print("please answer Y or N")

        for i in range(4):
            light = 0
            while light not in (1,2,3,4):
                try:
                    light = int(input(f"\nLight sconce {i+1}: (1-4) \n"))
                    if light in (1,2,3,4):
                        light_order.append(light)
                    else:
                        print("Try again 1-4")
                except ValueError:
                    print("please enter a number 1-4")

        time.sleep(0.5)

        if light_order == correct_order:
            print("\nThe lit sconces suddenly blaze bright blue flame, activating runes on the pillars")
            door_puzzle[1] = "⚔️"
            puzzle_trigger(door_puzzle)
            exit = True
        else:
            print("🔥" * 15)
            print("The last sconce belches flame back at you, searing your arm. All flames extinguish")
            print("A voice whispers - 'You chose poorly'\n")
            time.sleep(2)
            hero.take_dmg(5)

    def inspect_torchstand():
        print("Runes etched along its base glow faintly when touched")
        print("A faint voice whispers: 'From shadow we watch, through fire we strike'")

    def inspect_mural():
        print("The battle scene shows four warriors, three of which are named:")
        print("In the foreground, a bloodied Durek Flameborn holds a fallen Kellum Ironhand in his arms")
        print("To the left Ser Bryn lies in the grass, body blackened from dragon fire")
        print("The unnamed figure strikes the dragon alone")

    explore_options = {
        1: inspect_pillars,
        2: inspect_mural,
        3: inspect_torchstand
    }
    # === ROOM DESCRIPTION ===
    time.sleep(1)
    print("This chamber has 4 pillars, each with a stone sconce facing the center of the room")
    print("In the center a pedestal instructs - 'Light returns in rhythm'")
    print("The back wall displays a mural of warriors battling a dragon")
    print("A ceremonial torchstand sits in front")
    while not exit:
        pause()
        print("-" * 30)
        print("\n1 - Inspect the pillars")
        print("2 - Inspect mural")
        print("3 - Inspect torchstand")
        print("4 - Leave room")
        print("-" * 30)

        explore = 0
        while explore not in (1,2,3,4):
            try:
                explore = int(input("\nChoose 1-4 --\n"))
            except ValueError:
                print("please enter a number 1-4")
        if explore == 4:
            exit = True
        else:
            time.sleep(0.5)
            explore_options[explore]()



# === TRIAL OF BALANCE ===
def tomb_ne_room(door_puzzle):
    exit = False

    def inspect_scale():
        nonlocal exit
        block_order = []

        time.sleep(1)
        print("Carvings along the beam depict warriors being weighed. The scale has one square indent on each side")
        print("The stone blocks on the table seem perfectly sized to fit the indents on the scale")
        print("\nEach block has a symbol")
        print("1 - Arrow")
        print("2 - Sword")
        print("3 - Shield")
        print("4 - Bone")
        start_blocks = 0
        while start_blocks != "y" and start_blocks != "n":
            print("\nFailure will have consequence")
            start_blocks = input("Are you ready to begin balancing blocks? y/n -- \n").lower()
            if start_blocks == "y":
                continue
            elif start_blocks == "n":
                return
            else:
                print("please answer Y or N")

        for i in range(2):
            block = 0
            while block not in (1,2,3,4):
                try:
                    block = int(input(f"\nPlace block {i+1} of 2: (1-4) \n"))
                    if block in (1,2,3,4):
                        block_order.append(block)
                    else:
                        print("Try again 1-4")
                except ValueError:
                    print("please enter a number 1-4")

        if block_order == [2, 4] or block_order == [4, 2]:
            time.sleep(2)
            print("\nThe blocks click into place, their symbols glow as the scales become perfectly balanced")
            door_puzzle[2] = "⚔️"
            time.sleep(1)
            puzzle_trigger(door_puzzle)
            exit = True
        else:
            time.sleep(1)
            print("⚡" * 15)
            print("A vicious shock of electricity hits you like a lightning bolt. The scale remains unbalanced")
            print("A voice whispers - 'You chose poorly'\n")
            time.sleep(1)
            hero.take_dmg(5)

    def inspect_urn():
        print("\nDecorated with the symbol of the dragon slayer’s order — but faded")
        print("Smells faintly of charred wood and herbs.")
        print("All that remains of a worn away name scratched on the bottom: ‘K’")

    def inspect_remains():
        print("\nA leather breastplate lies beside old bones")
        print("Someone died attempting this puzzle")
        time.sleep(1)
        print("Well, the leather is in fair shape - no sense it going to waste")
        time.sleep(1)
        print("\nGAIN LEATHER ARMOR")
        hero.armor = "Leather Armor"
        hero.defense += 2
        hero.equipment_check()


    def inspect_walls():     
        print("\nCarving of a song with symbols above it, suggesting tone/musical order")
        print("Four symbols above verses I-IV: silence, fire, stone, blade")
        print("Below is scratched - 'The song of blade and beast'")

    explore_options = {
        1: inspect_scale,
        2: inspect_urn, 
        3: inspect_remains,
        4: inspect_walls
    }

    # === ROOM DESCRIPTION ===
    time.sleep(1)
    print("\nA huge ancient scale sits in the center of the room, one side hanging lower than the other")
    print("In front sits a table with four stone blocks, each with symbols on their face")
    print("On the ground nearby are scattered remains")
    print("A pedestal on the far wall displays an urn")
    print("The walls are adorned with various carvings")

    while not exit:
        pause()
        print("-" * 30)
        print("1 - Inspect the scale")
        print("2 - Inspect urn")
        print("3 - Inspect remains")
        print("4 - Inspect walls")
        print("5 - Leave room")
        print("-" * 30)

        explore = 0
        while explore not in (1,2,3,4,5):
            try:
                explore = int(input("\nChoose 1-5 --\n"))
            except ValueError:
                print("please enter a number 1-5")
        if explore == 5:
            exit = True
        else:
            time.sleep(0.5)
            explore_options[explore]()


# === TRIAL OF SOUND ===
def tomb_e_room(door_puzzle): 
    exit = False

    def inspect_chimes():
        nonlocal exit
        correct_order = [3, 1, 4, 2]
        chime_order = []
        print("A plaque on the floor states: 'Recount the battle in song'")
        print("1 - Chime I")
        print("2 - Chime II")
        print("3 - Chime III")
        print("4 - Chime IV")
        start_ringing = 0
        while start_ringing != "y" and start_ringing != "n":
            print("\nFailure will have consequence")
            start_ringing = input("Are you ready to begin ringing chimes? y/n -- \n").lower()
            if start_ringing == "y":
                continue
            elif start_ringing == "n":
                return
            else:
                print("please answer Y or N")

        for i in range(4):
            ring = 0
            while ring not in (1,2,3,4):
                try:
                    ring = int(input(f"Ring chime {i+1}: (1-4) \n"))
                    if ring in (1,2,3,4):
                        chime_order.append(ring)
                    else:
                        print("Try again 1-4")
                except ValueError:
                    print("please enter a number 1-4")

        if chime_order == correct_order:
            time.sleep(2)
            print("\nThe echoes of the chimes fill the chamber with harmony and the murals begin to glow")
            door_puzzle[3] = "⚔️"
            time.sleep(1)
            puzzle_trigger(door_puzzle)
            exit = True
        else:
            time.sleep(1)
            print("⚠️ " * 10)
            print("A discordant sound assaults your ears, the cacophony nearly unbearable before finally subsiding")
            print("A voice whispers - 'You chose poorly'")
            hero.take_dmg(5)


    def inspect_arrow():
        print("\nThe half-rotted arrow has black fletching — a ranger's mark")
        print("Carved beside it: 'Missed my note. Won’t again.'")

    def inspect_murals():  # 3-1-4-2
        print("\nI - The slayer dodges flame as he lunges forward, sword drawn")
        print("II - The dragon roars, the slayer mid-swing, sword glowing")
        print("III - The slayer stands alone, head bowed")
        print("IV  - The slayer crouched behind a huge shield, the dragon clawing at it")

    def inspect_painting():
        print("\nA painting of a torch being passed from hand to hand in different phases of light (dusk, night, dawn, morning)")
        print("The caption reads - 'Light returns in rhythm'")

    explore_options = {
        1: inspect_chimes,
        2: inspect_arrow,
        3: inspect_murals, 
        4: inspect_painting
    }

    # === ROOM DESCRIPTION ===
    time.sleep(1)
    print("\nFour stone chimes hang at the far end of the chamber, in order labeled I, II, III, IV")
    print("Around the room are mural panels matching the numbers on the chimes I-IV")
    print("You notice an arrow stuck in the wall between two chimes")
    print("A painting hangs alone on the south wall")

    while not exit:
        pause()
        print("-" * 30)
        print("1 - Inspect the chimes")
        print("2 - Inspect arrow")
        print("3 - Inspect murals")
        print("4 - Inspect painting")
        print("5 - Leave room")
        print("-" * 30)

        explore = 0
        while explore not in (1,2,3,4,5):
            try:
                explore = int(input("\nChoose 1-5 --\n"))
            except ValueError:
                print("please enter a number 1-5")
        if explore == 5:
            exit = True
        else:
            time.sleep(0.5)
            explore_options[explore]()



# ===  RANGERS QUEST  ===
def quest3():
    time.sleep(1)
    print("\nThe rangers live secluded in the forest to the north, self-imposed guardians of the green")
    print("It's a straight shot north to the forest border, but navigating through the trees will be a challenge")
    pause()
    print("🌲" * 50)
    print("You arrive at the forest edge. The trees rise like silent sentinels, thick and ancient, their bark gnarled with age.")
    print("Shafts of pale sunlight pierce the canopy in narrow beams, casting shifting patterns on the mossy ground.")
    time.sleep(1)
    print("A hush blankets the woods — not peace, but the stillness of something watching")
    pause()
    print("You step inside and head down the path")

    # === FOREST MAZE ===
    lost = True
    lost_turn = 0
    right_path = 0
    got_sword = got_shield = got_armor = False
    encounter1 = encounter2 = encounter3 = encounter4 = encounter5 = encounter6 = encounter7 = encounter8 = encounter9 = False
    while lost and lost_turn <= 8:  #caps maze at 8 turns max
        lost_turn += 1
        right_choice = random.randint(1,2)  #determines which path (nav_choice) is correct choice to advance right_path count
        time.sleep(1)
        print("🌲" * 50)
        nav_option_list = [
            "\nYou come to a fork in the path - which way do you go?  1 - Left   2 - Right", 
            "\nThe path diverges ahead - which way do you go?  1 - Uphill   2 - Downhill", 
            "\nA path splits off to the right - it seems darker in that direction  1 - Take path   2 - Continue on", 
            "\nThat tree looks really familiar - were you here already?  1 - Backtrack   2 - Continue on"
        ]
        print(nav_option_list[random.randint(0,3)]) 
        # user select path    
        nav_choice = 0
        while nav_choice not in (1,2):
            try:
                nav_choice = int(input("\nChoose your route 1-2 -- \n"))
                if nav_choice == right_choice:
                    right_path += 1
                elif nav_choice != right_choice:
                    continue
                else:
                    print("please choose a route 1-2")
            except ValueError:
                print("please enter a number 1-2")

        if right_path >=4: #if 4 correct path choices skip to end
            lost = False
            break
        else: #determine what random encounter spawns
            time.sleep(1)
            random_encounter = random.randint(1,20)
            if random_encounter == 1: 
                if encounter1: #can only get this once
                    continue
                else:
                    print("\nYou find a skeleton in tattered clothing on the ground leaning against a tree")
                    print("Vines wrap around in a chilling embrace, claiming it. The tree may own the body, but you claim the contents of his satchel")
                    pause()
                    print("GAIN 3 10hp health potions")
                    hero.potion += 3
                    encounter1 = True 
                    hero.equipment_check()
            elif random_encounter == 2:
                if encounter2: 
                    continue
                else:
                    print("\nYou stumble upon a crumbling altar covered in vines and old runes. As you touch it, a warm light courses through your body.")
                    hero.max_hp += 5
                    hero.hp = hero.max_hp
                    pause()
                    print(f"MAX HP increased by 5 --- {hero.name} hp now {hero.hp}")
                    encounter2 = True 
            elif random_encounter in (3,4):
                print("\nA guttural voice breaks the silence. Two orcs in leather armor step out from the trees, blades drawn, eyes full of malice.")
                time.sleep(1)
                combat(hero, orc)
                if not got_sword:
                    print("\nOne of the orcs has a steel sword strapped to his back. This is not orc-forged. They must have claimed it from a past victim")
                    pause()
                    print("(GAIN LONGSWORD)")
                    hero.sword = "Longsword"
                    hero.atk += 2
                    got_sword = True
                    hero.equipment_check()
                    time.sleep(1)
            elif random_encounter in (5,6):
                print("\nYou step into a web-strewn clearing — the air thick with silk and the promise of fangs. Two spiders the size of dogs rush towards you")
                combat(hero, spider)
                if not got_shield:
                    print("\nBelow a dessicated body wrapped in webbing you notice a shield with solid metal plating circling the rim. No sense it going to waste")
                    pause()
                    print("GAIN REINFORCED SHIELD")
                    hero.shield = "Reinforced Shield"
                    hero.defense += 1
                    got_shield = True
                    hero.equipment_check()
                    time.sleep(1)
            elif random_encounter in (7,8):
                print("\nA whistling arrow lands at your feet. Have you found the rangers?")
                print("No such luck. Bandits melt out from the foliage, grinning.")
                combat(hero, forestbandit)
                if not got_armor:
                    print("\nOne of the bandits wears an impressive hardended leather breatplate (blood stains are easy to get out, right?)")
                    pause()
                    print("GAIN LEATHER ARMOR")
                    hero.armor = "Leather Armor"
                    hero.defense += 2
                    got_armor = True
                    hero.equipment_check()
                    time.sleep(1)
            elif random_encounter in (9,10):
                if encounter6:
                    continue
                else:
                    print("\nThe path crumbles beneath your feet! You manage to cling to a root, but your gear shifts and a pouch falls into a ravine")
                    print("Lose 1 10hp health potion")
                    hero.potion -= 1
                    encounter6 = True
                    hero.equipment_check()
                    time.sleep(1)
            elif random_encounter in (11,12,13):
                print("\nA low growl rises from the underbrush. Yellow eyes gleam between the ferns — not one, but several. They're circling")
                combat(hero, wolf)
            elif random_encounter in (14,15,16):
                encounter8 = random.randint(1, 3)
                right_path -= 1 
                if encounter8 == 1:
                    print("\nYou stumble into a patch of strange flowers — their scent is dizzying. You feel disoriented… was this path here before?")
                elif encounter8 == 2:
                    print("\nThe path ahead of you comes to an abrupt end - nature has reclaimed it. No choice but to turn around")
                else:
                    print("\nExcitement builds as you see footprints on the trail ahead. Wait, these match your shoes. You've been this way already")
            else:
                encounter9 = random.randint(0, 4)
                encounter9_list = [
                    "\nYou hear movement nearby. Just a rabbit... or was it?",
                    "\nA figure darts through the trees then melts into the shadows",
                    "\nYou hear a roar to the east. Too close for comfort", 
                    "\nThe air smells of rotten flesh and you have no desire to find the source",
                    "\nMaybe it's time for a break. You feel eyes watching you... maybe find another spot"
                    ]
                print(encounter9_list[encounter9])
                print("You stay alert and press on")

    # === MAZE BOSS BATTLE ===
    time.sleep(2)
    print("\nA twig snaps to your right")
    time.sleep(1)
    print("\nSquinting in the gloom beyond the thick brush, you can't make anything out")
    time.sleep(2)
    print("\nSuddenly a large deer bursts out and runs past you. You stumble backwards and find yourself suspended between two trees") 
    time.sleep(2)
    pause("press Enter to pull yourself free")
    print("\nYou lurch forward and find you can't move. A web, nearly invisible, clings to your limbs like molasses.")
    time.sleep(2)
    print("Above you, something clicks its mandibles in the dark. It sounds massive. You’ve got seconds.")
    time.sleep(2)
    print(" 🕸️ 🕸️" * 15)

    web_free = False
    poisoned = False
    escape_odds = {
        1: (8, 6),  # arms
        2: (9, 7),  # legs
        3: (10, 10),  # thrash
    }

    for web_turn in range(4):
        time.sleep(1)
        if web_turn == 0:
            pass
        elif web_turn == 1:
            print("\nYou hear legs scraping bark nearby...")
        elif web_turn == 2:
            print("\nThe web trembles slightly — it's close...")
        else:
            print("\nA shadow looms above you...")

        time.sleep(1)
        print(" 🕸️ 🕸️" * 15)
        print("ACTION -")
        print("  1- Try to pull your arms free")
        print("  2- Try to kick your legs free")
        print("  3- Thrash wildly with your entire body")
        struggle_action = 0
        while struggle_action not in (1,2,3):
            try:
                struggle_action = int(input("\nWhat do you do? 1-3 -- \n"))
            except ValueError:
                print("please enter a number 1-3")

        struggle_roll = random.randint(1,10)
        early_odds, late_odds = escape_odds[struggle_action] #hero choice and turn number affect difficulty of success
        escape = early_odds if web_turn < 2 else late_odds  # becomes easier as turns pass

        if struggle_roll >= escape:
            web_free = True
            break
        else:
            time.sleep(1)
            print("\nYou struggle, but the webs hold tight...")

    if web_free and web_turn < 2:
        time.sleep(1)
        print("\nThe silky strands give way and you tumble to the ground. Wasting no time, you take off running before the spider arrives")
        fought_spider = False
    elif web_free:
        time.sleep(1)
        print("\nYou tear yourself free just as the spider draws near")
        time.sleep(1)
        print("In one fluid motion you draw your sword and slash at dripping fangs.")
        pause("press Enter to attack")
        print("SURPRISE ATTACK! The giant spider loses 5 hp")
        time.sleep(1)
        print("Enraged, the spider shrieks and knocks you aside with powerful legs. You roll into attack position preparing for battle")
        time.sleep(3)
        giantspider.hp -= 5
        fought_spider = True
        combat(hero, giantspider)
    else:
        time.sleep(1)
        print("\nUnable to free yourself in time, the spider lunges from the rear as you struggle helplessly!")
        print(f"{hero.name} loses 5 hp")
        time.sleep(2)
        print("\nAs fangs sink into flesh, the weight of the spider gives you the last push needed to free yourself from the trap")
        time.sleep(1)
        print("Back throbbing from the bite, you draw your sword and prepare to defend yourself")
        time.sleep(2)
        hero.hp -= 5
        fought_spider = True
        poisoned = True
        combat(hero, giantspider)

    print("🕷️ 🕷️ 🕷️ 🕷️")
    time.sleep(1)
    print("\nHaving no desire to see if the creature has friends, you bolt away from the carcass down the path")
    if poisoned:
        print("\nBack constricting, you feel the venom seizing up your muscles. You need help, and fast")

    time.sleep(2)

    # === MEET THE RANGERS ===
    print("\nIn your haste, your foot snags something. A whisper of rope, a snap — and the world flips")
    time.sleep(1)
    print("You’re yanked upside down, blood rushing to your head as the forest spins")
    time.sleep(1)
    print("Then silence. No footsteps, no breathing — until a half-dozen cloaked figures melt from the trees like ghosts")
    time.sleep(2)
    print("\nFaces hidden beneath hoods, bows aimed, unmoving. One steps forward and, without a word, slices the rope")
    time.sleep(2)

    pause()

    black_out = ["The world...", "crashes down...", "to", "black"]
    for i in black_out:
        print(i)
        time.sleep(1)

    time.sleep(1)
    print("😴 😴 😴")
    time.sleep(2)

    print("\nWhen you wake, your hands are unbound but you're surrounded by lean, silent figures with watchful eyes and forest-worn cloaks")
    time.sleep(2)
    if poisoned:
        print("\nYou notice the pain from the spider venom is gone and there are fresh dressings under your shirt")
    print("\nWooden platforms span the trees above, connected by rope bridges. Cooking fires crackle low, their smoke rising like spirits")
    time.sleep(2)
    print("This is not a simple ranger camp — it’s a village among the branches")
    time.sleep(1)
    print("\n'Hello little cub'")
    pause("press Enter to look up")
    print("\nYou see the leader drop from a platform above, landing lightly beside you with a cat’s grace")
    time.sleep(1)
    print("Her cloak rustles like leaves in a breeze. Her sharp eyes study you with amusement as though she’s already decided your story.")
    pause()
    print("\n'Most who find us are never seen again. But you... you’ve caused quite a stir.' She circles you slowly")
    time.sleep(1)
    print("'So tell me, brave wanderer — are you here to beg, bargain, or blunder?'")
    pause()

    print("-" * 30)
    print("\n  1- 'I came to beg help of the rangers to face a dragon threatening my village'")
    print("  2- 'Simple - help kill a dragon, share the hoard. You’ll have silver-tipped arrows for centuries'")
    print("  3- 'Well, there's a dragon to slay, but blunder has ALWAYS been my favorite pastime'")
    
    rangerQ1 = 0
    while rangerQ1 not in (1,2,3):
        try:
            rangerQ1 = int(input("\nHow do you respond? 1-3 -- \n"))
        except ValueError:
            print("please enter a number 1-3")

    rangerQ1_responses = [
        "'Begging? Poor look on someone who walked through my forest and lived'", 
        "'Treasure buys nothing in the forest, but shiny things are nice...'", 
        "'Then you're in luck, cub - our traps love repeat offenders'"
    ]    
    time.sleep(1)
    print(rangerQ1_responses[rangerQ1 - 1])
    pause()
    print("\n'A dragon, hmm? Well, we don’t care much for torching trees.' She cocks her head, considering")
    print("She circles you, arms behind her back, expression unreadable")
    pause()
    print("\n'The world is full of would-be heroes. Some are fools, some are corpses. What makes you different?'")
    time.sleep(1)
    print("-" * 30)
    print("  1- 'I’ve got a sharp blade, steady hands, and a village that believes in me'")
    print("  2- 'Probably nothing. But I’ve made it this far without dying — and that’s more than most'")
    print("  3- 'I’m smart enough to know your scouts could’ve dropped me three times already, and charming enough to still be standing'")
    print("  4- 'I don’t seek glory. I only ask to die for something larger than myself — if I must die at all'")
    time.sleep(2)

    rangerQ2 = 0
    while rangerQ2 not in (1,2,3,4):
        try:
            rangerQ2 = int(input("\nHow do you respond? 1-4 -- \n"))
        except ValueError:
            print("please enter a number 1-4")

    rangerQ2_responses = [
        "'Shall we wager how well belief guards against dragon fire?'", 
        "'Ha, a dragon slayer not weighed down by ego, perhaps there's hope for you, cub'", 
        "She bursts out laughing. 'Thank you for the laugh, cub. Charming indeed covered in grime, guts, and spiderweb'", 
        "'An idealist, perhaps you've read too many stories'"
    ]    
    time.sleep(1)
    print(rangerQ2_responses[rangerQ2 - 1])

    pause()
    print("-" * 30)
    print("Eyeing you carefully, finally she shrugs and nods her head")
    time.sleep(1)
    print("\n'You fought your way here, cub. That says enough'")
    print("'You now have ranged support, friend. Our bows will find the beast when you call'")
    print("'Now rest up, be our guest tonight and tomorrow we can escort you home'")
    hero.ranger_volley = True

    if fought_spider:
        pause()
        print("\nLater on, a young ranger seeks you out and makes a big show of pulling a small green vial from his sleeve")
        print("He pops it open, wrinkling his nose as he sniffs the air")
        print("'Smell that? Venom. Straight from the eight-legged nasty you tangled with'")
        print("'We refined it for you. Coat your blade - it'll sting more than dragonhide likes'")
        print("Taking a bow, he scampers away. Strange lad")
        hero.venom = True

    pause("press Enter to go to sleep")
    hero.sleep()

    print("-" * 30)
    print("\nThe next morning you're called to the edge of the settlement where the ranger leader waits with a small regiment of archers")
    print("'For you, cub, an escort of some of the finest bowmen the woods have to offer'")
    print("'May their arrows fly true and drop that scaly beast where your sword can greet it'")
    pause()
    print("\nShe tosses you a pouch. 'I wish you luck - I've a feeling you'll need it'")
    print("GAIN 3 10hp health potions")
    hero.potion += 3
    hero.equipment_check()
    time.sleep(2)

    if rangerQ2 in (2,3):
        if not got_armor or not got_sword:
            print("\n'Been a pleasure, cub, you're more fun than I expected. Take this as well - a gift from the forest'")

            if not got_armor:
                time.sleep(1)
                print("\nGAIN LEATHER ARMOR")
                hero.armor = "Leather Armor"
                hero.defense += 2
                got_armor = True
            
            if not got_sword:
                time.sleep(1)
                print("\nGAIN LONGSWORD)")
                hero.sword = "Longsword"
                hero.atk += 2
                got_sword = True

            hero.equipment_check()
            
    time.sleep(1)
    print("🌲" * 50)
    pause()

   

# === DRAGON ENDGAME ===
def final_boss():
    quest_text = {
        "dwarves": [
            "'And a very warm welcome to the Hill Dwarves, your aid shall not be forgotten'",
            "Defer to the dwarves for expertise",
            "You turn and find the dwarves are already busy barking orders, apparently planning to do both",
            "Dwarves hammer iron stakes into carts and weld makeshift barricades. Others prepare elaborate mechanical traps", 
            "The dwarves clang weapons against shields, providing comfort to the villagers they defend",
            ""
        ],
        "slayer": [
            "'That sword certainly looks the part, let us hope it lives up to its legend'",
            "Let the Elder decide",
            "'Hmmm, the pit trap seems best'",
            "",
            "When you draw the slayer's sword, it's glow cuts through dusk like fire through fog. It pulses eagerly",
            "The sword flares up in a blue blaze. In the glow you can almost hear satisfied whispers"
        ],
        "rangers": [
            "'And a very warm welcome to the Forest Rangers, your aid shall not be forgotten'", 
            "Defer to the rangers for expertise",
            "The rangers agree the pit trap is best",
            "The rangers sharpen arrows while they supervise the villagers",
            "The rangers slink into their hiding spots and blend into the fields like shadows",
            ""
        ],
        "none": [
            "", "Let the Elder decide", "'Hmmm, the pit trap seems best'", "", "", ""
        ]
    }
    # quest completed determines key to pull text values from
    if hero.fire_shield:
        quest_completed = "dwarves"
    elif hero.slayer_sword:
        quest_completed = "slayer"
    elif hero.ranger_volley:
        quest_completed = "rangers"
    else:
        quest_completed = "none"
        
    
    print("")
    print("-" * 30)
    print("The wind carries the scent of ash as you return home. The village seems far too quiet and your heart races")
    print("Beginning to fear the worst, a window pops open behind you and an old woman hisses 'off the streets you fool, it's not safe'")
    pause("press Enter to turn and face her")
    print(f"\nHer face softens a bit as she recognizes you. 'Oh, apologies {hero.name}, we fear open skies these days'") 
    print("'As meager a snack as I'd be, best not tempt the flying beast. Speaking of, shouldn't you be up at the farm with everyone else?'")
    print("She explains the Elder has brought everyone to the northeast plains to help prepare the old abandoned farm for the dragon")
    print("Wasting no time, you bid her farewell and head northeast")
    pause()
    print("-" * 15)
    print("The Elder greets you with open arms when you arrive at the farm")
    print(f"'Welcome back {hero.name}!!!'")
    print(quest_text[quest_completed][0])

    print("'All able-bodied villagers have gathered, donating farm animals as bait in preparation for your confrontation'")
    print("'There has been some debate on exactly HOW to prepare. Perhaps you can offer input?'")
    pause()
    print("\nHow should you prepare?")
    print("  1- Build a pit trap to injure the dragon")
    print("  2- Build barricades to offer protection in the battle")
    print(f"  3- {quest_text[quest_completed][1]}")
    print("-----------------------------------")
    Q1 = 0
    while Q1 not in (1,2,3):
        try:
            Q1 = int(input("\nDecision 1-3 -- \n"))
            if Q1 in (1,2,3):
                print()
                print(quest_text[quest_completed][2])
            else:
                print("please choose 1-3")
        except ValueError:
            print("please enter a number 1-3")

    print("\n'Well it seems settled, let's get to work!'")
    pause("press Enter to ready for battle")

    print("\nThe plains erupt in a bustle of activity as everyone jumps on their assigned tasks")
    print(quest_text[quest_completed][3])

    if Q1 == 2:
        "Carts are converted into barricades, flanking the intended battleground"
    else:
        "A shallow pit is dug next to the bait area, lined with sharpened stakes and covered in netting and hay"

    print("\nThe field is now a battlefield-in-waiting. A makeshift corral holds terrified livestock in a circle of bait")

    if hero.venom:
        print("You coat your weapon in the green venom, careful not to let it touch your skin")

    print(quest_text[quest_completed][4])

    print("\nThe sun hangs low when the first scream splits the sky")
    print("The clouds ripple as a shadow breaks through. With a sound like mountains cracking, the dragon dives")
    print("Wings stretched like sails, the creature descends toward the bait")

    if Q1 == 2:
        print("\nApproaching, the dragon ignores the livestock and unleashes a torrent of flame")
        print("As the charred makeshift barricades crumble, you're fully exposed on the open plain")
        print("Launching back skyward, the dragon circles around to continue its assault!")
    else:
        print("\nAs the dragon lands the ground gives way as it falls into the pit!")
        print("A roar of surprise echoes as the trap bites into scale")
        Monsters.take_dmg(dragon, 5)
        print("\nTearing free, it launches skyward in a fury and circles around, preparing to make you pay")

    print("\nSomeone throws you a bow and a quiver")
    print("'You need to bring the dragon to ground, you can't fight it in the air!")

    final_battle_air(hero, dragon)

    final_battle_ground(hero, dragon)
    
    print("\nThe dragon's breath comes in ragged bursts, blood tracing patterns down its scales")
    print("Time to finish this. Exhausted, hands shaking, you drive your sword in for the killing blow")
    print(quest_text[quest_completed][5])
    print("Wings sag, one last breath hissing between its fangs. Finally, silence")
    pause()

    print("-" * 30)
    print("The last traces of black smoke dissipate in the sky")
    print("Villagers emerge one by one, cautiously eyeing the massive carcass")
    print(f"Someone shouts '{hero.name} has done it!' and thunderous cheers follow")
    print("The Elder clasps your arm, eyes shining")
    pause()
    
    print("\nThe dragon is dead")
    time.sleep(1.5)
    print("The village is safe")
    time.sleep(1.5)
    print("Finally, there is peace")

    the_end()


def the_end():
    ascii_text = r"""
  _______ _            _______          ___ 
 |__   __| |           |  ____|         | |
    | |  | |__   ___   | |__   _ __   __| |
    | |  | '_ \ / _ \  |  __| | '_ \ / _` |
    | |  | | | |  __/  | |____| | | | (_| |
    |_|  |_| |_|\___|  |______|_| |_|\__,_|
                                          
    """

    for char in ascii_text:
        print(char, end="", flush=True)
        time.sleep(0.02)  

    print("\n\n")  



# === GAME INTRODUCTION ===
print("*********************")
print("⚔️                 ⚔️")
print(color_text("    Codédex Quest    ", "1;32"))
print("⚔️                 ⚔️")
print("*********************")
hero.name = input("\nWhat is your name? \n")
print("\nThe Story Begins......")
print("----------------------")
print(f"{hero.name} is from a small village nestled in the shadow of the snowy peaks of a looming mountain range")
print("Recently a dragon has moved into the mountains and the village is in danger")
print(f"{hero.name}'s father, the village guardian, has fallen in battle and the people need a new champion...")
print("----------------------")
pause()
print("\nOne morning you hear the Village Elder knocking on your door and calling your name")

Q1 = 0
while Q1 != "y" and Q1 != "n":
    Q1 = input("Do you answer the door? Y/N -- \n").lower() #convert to lowercase so don't need to define Y/N/y/n
    if Q1 == "y":
        pass
    elif Q1 == "n":
        print(f"\n'{hero.name}, this is too important - I hope you're dressed, I'm coming in'")
    else:
        print("please answer Y or N")


print("\nVillage Elder enters and asks for your help. He describes several options to help protect the village from the dragon")
print("-------------------------------------------------------------------------------------")
print("  1- The dwarves in the nearby Copper Hills may be convinced to help defend us")
print("-------------------------------------------------------------------------------------")
print("  2- A legendary dragon slayer's tomb lies on the coast and contains his magic sword")
print("-------------------------------------------------------------------------------------")
print("  3- The rangers in the forest are masterful archers and could take down a dragon")
print("-------------------------------------------------------------------------------------")
pause()

Q2 = 0
while Q2 != "y" and Q2 != "n":
    Q2 = input(f"\n'What say you, young {hero.name}, do you feel up to the task?' Y/N -- \n").lower()
    if Q2 == "y":
        print("'Ah wonderful, blessings upon your quest'")
    elif Q2 == "n":
        print(f"'Oh {hero.name}, and that's precisely why you are the right person'")
        time.sleep(1)
    else:
        print("please answer Y or N")

# === CHOOSE QUEST, GEAR UP ===

print("\nWhere will you go for aid?")
print("  1- The Hill Dwarves")
print("  2- The tomb of the dragon slayer")
print("  3- The Forest Rangers")
print("-----------------------------------")

quest = 0
while quest not in (1,2,3):
    try:
        quest = int(input("\nWhich path will you take? 1-3 -- \n"))
        if quest in (1,2,3):
            print("\n'A splendid choice, let's prepare you for your journey with some equipment'")
            time.sleep(1)
            print("(GAIN SHORTSWORD)")
            time.sleep(1)
            print("(GAIN SHIELD)")
            time.sleep(1)
            print("(GAIN 3 10hp HEAL POTIONS)")
            time.sleep(1)
            print("-----------------------------------")
            hero.equipment_check()
        else:
            print("please choose a path 1-3")
    except ValueError:
        print("please enter a number 1-3")
pause("press Enter to begin your quest")

if quest == 1:
    quest1()
elif quest == 2:
    quest2()
else:
    quest3()
time.sleep(2)
final_boss()