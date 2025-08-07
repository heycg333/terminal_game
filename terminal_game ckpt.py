
import random

herohp = heromaxhp = 20
heroatk = 0
herodef = 0
potion = 0
potionskip = False
herodead = False
heroblock = False
bonusquest = False
gameover = False

# === INTRODUCTION ===

print("*********************")
print("⚔️                 ⚔️")
print("    Codédex Quest    ")
print("⚔️                 ⚔️")
print("*********************")
print("")
hero = input("What is your name? ")
print("")
print("The Story Begins......")
print("----------------------")
print(f"{hero} is from a small village nestled in the shadow of the snowy peaks of a looming mountain range")
print("Recently a dragon has moved into the mountains and the village is in danger")
print(f"{hero}'s father, the village guardian, has fallen in battle and the people need a new champion...")
print("----------------------")
print("One morning you hear the Village Elder knocking on your door and calling your name")

Q1 = 0
while Q1 != "y" and Q1 != "n":
    Q1 = input("Do you answer the door? Y/N -- ").lower() #convert to lowercase so don't need to define Y/N/y/n
    if Q1 == "y":
        print("")
    elif Q1 == "n":
        print("")
        print(f"'{hero}, this is too important - I hope you're dressed, I'm coming in'")
        print("")
    else:
        print("please answer Y or N")

print("Village Elder enters and asks for your help. He describes several options to help protect the village from the dragon")
print("-------------------------------------------------------------------------------------")
print("  1- The dwarves in the nearby Copper Hills may be convinced to help defend us")
print("-------------------------------------------------------------------------------------")
print("  2- A legendary dragon slayer's tomb lies on the coast and contains his magic sword")
print("-------------------------------------------------------------------------------------")
print("  3- The rangers in the forest are masterful archers and could take down a dragon")
print("-------------------------------------------------------------------------------------")
print("")

Q2 = 0
while Q2 != "y" and Q2 != "n":
    Q2 = input(f"'What say you, young {hero}, do you feel up to the task?' Y/N -- ").lower()
    if Q2 == "y":
        print("'Ah wonderful, blessings upon your quest'")
    elif Q2 == "n":
        print(f"'Oh {hero}, and that's precisely why you are the right person'")
    else:
        print("please answer Y or N")
print("")

# === CHOOSE QUEST, GEAR UP ===

print("Where will you go for aid?")
print("  1- The Hill Dwarves")
print("-----------------------------------")

quest = 0
while quest != 1:
    try:
        quest = int(input("Which path will you take? 1 -- "))
        if quest == 1:
            print("")
            print("'A splendid choice, let's prepare you for your journey with some equipment'")
            print("(GAIN SHORTSWORD)")  
            print("(GAIN SHIELD)")  
            print("(GAIN 3 10hp HEAL POTIONS)")  
            print("-----------------------------------")
            potion = potion + 3
            heroatk = heroatk + 1
            herodef = herodef + 1
        else:
            print("please choose path 1")
    except ValueError:
        print("please enter a number 1")

# === loop will be exited if hero dies to end game ===
while not herodead and not gameover :

    # === QUEST 1 - DWARVES ===

    if quest == 1: #choose travel route - determines who combat will be with
        print("The Dwarves live in the Copper Hills to the south. You can either - ")
        print("  1- Take the well-traveled mining trail road, following it south then cut east to the Copper Hills")
        print("  2- Take a riskier, more direct route and head southeast across the plains")
        route1 = 0
        while route1 not in (1,2):
            try:
                route1 = int(input("Choose your route 1-2 --"))
                print("")
                if route1 == 1:
                    print("Along the road you encounter an angry wolf. Get ready to fight!")
                    monster = "Wolf"
                    monsteratk = 1
                    monsterhp = 10
                elif route1 == 2:
                    print("You come across a bandit camp and 2 charge you. Get ready to fight!")
                    monster = "Bandit"
                    monsteratk = 2
                    monsterhp = 18
                else:
                    print("please choose a route 1-2")
            except ValueError:
                print("please enter a number 1-2")
        print("")

        # === COMBAT LOOP - HERO ACTION ===

        round = 0
        while herohp > 0 and monsterhp > 0:
            round = round + 1
            print("********************************************")
            print(f"Round - {round}")
            print("BATTLE OPTIONS") #should I add options to check HP? or always print hero/monster hp at top?
            print("   1- Attack ⚔️")
            print("   2- Block 🛡️") 
            print("   3- Heal Potion 💗")
            try:
                herocombatchoice = int(input("Enter number 1-3 -- "))
                if herocombatchoice == 1: 
                    #attack rolls d20 to check for critial hit or miss.
                    d20 = random.randint(1,20)
                    if d20 == 20:
                        print("**********************")
                        print("⚔️  CRITICAL HIT!  ⚔️")
                        print("**********************")
                        if heroblock:
                            heroatkdmg = 2 + ((heroatk + random.randint(1,3)) * 2)  #heroblock adds 2 dmg and crit hit doubles dmg
                            heroblock = False
                        else:
                            heroatkdmg = (heroatk + random.randint(1,3)) * 2  #crit hit doubles dmg
                        print(f"{monster} takes {heroatkdmg} damage")
                        monsterhp = monsterhp - heroatkdmg
                        if monsterhp <= 0:
                            print("")
                        else:
                            print(f"{monster} has {monsterhp} hp left")
                            print("")
                    elif d20 == 1:
                        print("")
                        print(f"{hero} Missed!")    
                    #===if not crit hit or miss, continue with normal attack - calc atk dmg using hero atk stat and randint, subtract from monster hp
                    else:
                        if heroblock: #adds 2 dmg
                            heroatkdmg = 2 + heroatk + random.randint(1,3) 
                            heroblock = False
                        else:
                            heroatkdmg = heroatk + random.randint(1,3)
                        print("")
                        print(f"{hero} attacks! {monster} takes {heroatkdmg} damage")
                        monsterhp = monsterhp - heroatkdmg
                        if monsterhp <= 0:
                            print("")
                        else:
                            print(f"{monster} has {monsterhp} hp left")
                            print("")
                elif herocombatchoice == 2:  #===blocking reduces dmg in monster attack and adds 2 to next heroatkdmg
                    heroblock = True
                    print("")
                    print(f"{hero} conserves energy, raises shield, and braces for impact")
                    print("")
                elif herocombatchoice == 3:
                # === check to see if user has potions then heal 10hp up to maxhp ===
                    if potion != 0:
                        if herohp > (heromaxhp - 10):
                            herohp = heromaxhp
                            print("")
                            print(f"{hero} is fully healed")
                            print(f"{hero} has {herohp} hp")
                            print("")
                            potion = potion - 1
                        else:
                            herohp = herohp + 10
                            print("")
                            print(f"{hero} heals 10 hp")
                            print(f"{hero} has {herohp} hp")
                            print("")
                            potion = potion - 1
                    else:
                        print(f"Oh no! {hero} is out of potions") 
                        potionskip = True #skips monster attack to loop back to battle options
                else:
                    print ("select an action 1-3")
            except ValueError:
                print("please enter a number 1-3")

        # === COMBAT LOOP - MONSTER ACTION ===

            if potionskip:
                potionskip = False
                continue
            elif monsterhp > 0: #if monster was killed in hero action, skip monster action
                print(f"{monster} attacks!")
                if heroblock: #checks for block, halves dmg (rounded down)
                    monsteratkdmg = int(monsteratk - herodef + (random.randint(1,3)) / 2)
                else:
                    monsteratkdmg = monsteratk - herodef + random.randint(1,3)
                print(f"{hero} takes {monsteratkdmg} dmg")
                herohp = herohp - monsteratkdmg
                if herohp <= 0:
                    print("💀💀💀💀💀💀💀💀")
                    print(f"{hero} has perished")
                    print("💀💀💀💀💀💀💀💀")
                    herodead = True
                    break
                else:
                    print(f"{hero} has {herohp} hp left")
                    print("")
            else:
                print("")
        if not herodead:
            print("🎉🎉🎉*******************🎉🎉🎉")
            print(f"{hero} defeated the {monster}")
            print("🎉🎉🎉*******************🎉🎉🎉")
            print("")
            print("----------------------------------------------")
            if route1 == 2: #harder route gains rewards
                print("(GAIN LONGSWORD)")
                print("(GAIN 1 10hp HEAL POTION)")
                potion = potion + 1
                heroatk = heroatk + 2
                herohp = heromaxhp
            else:
                herohp = heromaxhp
        else:
            break

        # === ARRIVE QUEST LOCATION ===

        print("You arrive at the gates of the dwarven stronghold built into the rock face of the Copper Hills")
        print("A guard shouts down 'State your business here!'")
        print("You shout back - ")
        print("  1- I need to speak to your chief. My village needs help defending from the dragon")
        print("  2- I've heard the hill dwarves make the best ale - I have my doubts so I'm here to put that to the test")
        print("")
        dwarfQ1 = 0
        while dwarfQ1 not in (1,2):
            try:
                dwarfQ1 = int(input("Choose your response 1-2 --"))
                print("")
                if dwarfQ1 == 1:
                    print("The guard laughs. 'You are not fit to address the Thane. Durgrin, go teach this whelp a lesson.'")
                    print("The gate opens and a burly dwarf approaches cracking his knuckles. Get ready to fight!")
                    monster = "Durgrin"
                    monsteratk = 2
                    monsterhp = 15
                elif dwarfQ1 == 2:
                    print("The guard scowls. 'There is NONE better! Durgrin! Open the gates and show this fool to the tavern.'")
                else:
                    print("please choose a response 1-2")
            except ValueError:
                print("please enter a number 1-2")

        if dwarfQ1 == 1:
        # === COMBAT LOOP - HERO ACTION ===

            round = 0
            while herohp > 0 and monsterhp > 0:
                round = round + 1
                print("********************************************")
                print(f"Round - {round}")
                print("BATTLE OPTIONS") #should I add options to check HP? or always print hero/monster hp at top?
                print("   1- Attack ⚔️")
                print("   2- Block 🛡️") 
                print("   3- Heal Potion 💗")
                try:
                    herocombatchoice = int(input("Enter number 1-3 -- "))
                    if herocombatchoice == 1: 
                        #attack rolls d20 to check for critial hit or miss.
                        d20 = random.randint(1,20)
                        if d20 == 20:
                            print("**********************")
                            print("⚔️  CRITICAL HIT!  ⚔️")
                            print("**********************")
                            if heroblock:
                                heroatkdmg = 2 + ((heroatk + random.randint(1,3)) * 2)  #heroblock adds 2 dmg and crit hit doubles dmg
                                heroblock = False
                            else:
                                heroatkdmg = (heroatk + random.randint(1,3)) * 2  #crit hit doubles random dmg
                            print(f"{monster} takes {heroatkdmg} damage")
                            monsterhp = monsterhp - heroatkdmg
                            if monsterhp <= 0:
                                print("")
                            else:
                                print(f"{monster} has {monsterhp} hp left")
                                print("")
                        elif d20 == 1:
                            print("")
                            print(f"{hero} Missed!")    
                        #===if not crit hit or miss, continue with normal attack - calc atk dmg using hero atk stat and randint, subtract from monster hp
                        else:
                            if heroblock: #adds 2 dmg
                                heroatkdmg = 2 + heroatk + random.randint(1,3) 
                                heroblock = False
                            else:
                                heroatkdmg = heroatk + random.randint(1,3)
                            print("")
                            print(f"{hero} attacks! {monster} takes {heroatkdmg} damage")
                            monsterhp = monsterhp - heroatkdmg
                            if monsterhp <= 0:
                                print("")
                            else:
                                print(f"{monster} has {monsterhp} hp left")
                                print("")
                    elif herocombatchoice == 2:  #===blocking reduces dmg in monster attack and adds 2 to next heroatkdmg
                        heroblock = True
                        print("")
                        print(f"{hero} conserves energy, raises shield, and braces for impact")
                        print("")
                    elif herocombatchoice == 3:
                    # === check to see if user has potions then heal 10hp up to maxhp ===
                        if potion != 0:
                            if herohp > (heromaxhp - 10):
                                herohp = heromaxhp
                                print("")
                                print(f"{hero} is fully healed")
                                print(f"{hero} has {herohp} hp")
                                print("")
                                potion = potion - 1
                            else:
                                herohp = herohp + 10
                                print("")
                                print(f"{hero} heals 10 hp")
                                print(f"{hero} has {herohp} hp")
                                print("")
                                potion = potion - 1
                        else:
                            print(f"Oh no! {hero} is out of potions") 
                            potionskip = True #skips monster attack to loop back to battle options
                    else:
                        print ("select an action 1-3")
                except ValueError:
                    print("please enter a number 1-3")

            # === COMBAT LOOP - MONSTER ACTION ===

                if potionskip:
                    potionskip = False
                    continue
                elif monsterhp > 0: #if monster was killed in hero action, skip monster action
                    print(f"{monster} attacks!")
                    if heroblock: #checks for block, halves dmg (rounded down)
                        monsteratkdmg = int(monsteratk - herodef + (random.randint(1,3)) / 2)
                    else:
                        monsteratkdmg = monsteratk - herodef + random.randint(1,3)
                    print(f"{hero} takes {monsteratkdmg} dmg")
                    herohp = herohp - monsteratkdmg
                    if herohp <= 0:
                        print("💀💀💀💀💀💀💀💀")
                        print(f"{hero} has perished")
                        print("💀💀💀💀💀💀💀💀")
                        herodead = True
                        break
                    else:
                        print(f"{hero} has {herohp} hp left")
                        print("")
                else:
                    print("")
            if not herodead:
                print("🎉🎉🎉*******************🎉🎉🎉")
                print(f"{hero} defeated {monster}")
                print("🎉🎉🎉*******************🎉🎉🎉")
                print("")
                print("----------------------------------------------")
                herohp = heromaxhp
                print(f"{monster} dusts himself off, laughing as you help him up")
                print("'I underestimated you, follow me friend, I could use a drink'")
            else:
                break
        else: #dwarfQ1 == 2
            print("")        

        # === ENTER DWARVEN STRONGHOLD ===
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
        print("")
        dwarfQ2 = 0
        while dwarfQ2 not in (1,2,3):
            try:
                dwarfQ2 = int(input("Choose your response 1-3 --"))
                print("")
                if dwarfQ2 == 1:
                    print("Durgrin nods, 'Wise choice'. You follow the guards past the marketplace to a towering set of bronze doors.")
                    print("Inside, the throne room stretches upward into a dome with intricate ornamental etchings spiraling up the stone")
                elif dwarfQ2 in (2,3):
                    print("'Insolent whelp! We'll teach you manners!' You're struck in the head and knocked unconscious")
                    herohp = herohp - 5
                    print(f"{hero} loses 5 hp. Current hp = {herohp}")
                    print("---------------------------------------------------------------------------------------------")
                    print("")
                    print("You awaken on the floor of a large room stretching upward into a dome. Rubbing your head you look around and realize you're in the throne room")
                    print("----------------------------------------------------------------------------------------------------------------------------------------------")

                else:
                    print("please choose a response 1-2")
            except ValueError:
                print("please enter a number 1-2")

        # === DWARVEN THRONEROOM ===
        print("Thane Brogdin's throne sits on a raised dais, carved from a single slab of granite with copper runes twisting up the armrests")
        print("The Thane watches you with deep-set eyes, his face expressionless and unreadable.")
        print("You feel a chill - his stare is every bit as cold as the polished stone surrounding him")
        print("His advisor Ori, an older dwarf with a beard like braided chainmail, breaks the silence first -")
        print("")
        print("'It was only a matter of time before the humans came seeking shelter. Those who choose to live under the sky will always be at the mercy of what falls from it'")
        print("")
        print("You respond - ")
        print("  1 - Better the open sky than a hole in the ground")
        print("  2 - It's true, we seek protection and aid from the brave and mighty dwarves of the Copper Hills")
        print("  3 - Say nothing. Let the Thane speak first")
        print("")

        dwarfQ3 = 0
        while dwarfQ3 not in (1,2,3):
            try:
                dwarfQ3 = int(input("Choose your response 1-3 --"))
                print("")
                if dwarfQ3 == 1:
                    print("The advisor's nostrils flare and his eyes shoot daggers. He raises an arm, taking a deep breath and readying a verbal lashing")
                    print("Thane Brogdin's booming laughter interrupts. 'This one has some courage, settle yourself Ori, we shall hear out our visitor'")
                elif dwarfQ3 == 2:
                    print("'Sniveling worm, do not insult us with your attempts to barter with flattery' Ori snarls")
                    print("The Thane eyes you with thinly-veiled disdain")
                elif dwarfQ3 == 3:
                    print("You hold your tongue and look to the Thane")
                else:
                    print("please choose a response 1-3")
            except ValueError:
                print("please enter a number 1-3")
        
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("Thane Brogdin raises a gauntleted fist, instantly silencing the room")
        print("")
        print("'You come here seeking dwarven steel to protect your people, bringing great risk to mine'")
        print("'Why should we face your dragon? Why should dwarven blood pay for your salvation?'")
        print("")
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print("How will you convince the Thane - ")
        print("  1 - It is the right thing to do")
        print("  2 - If we fall, the dragon will come for your great halls next")
        print("  3 - We will share whatever treasure the dragon has hoarded")
        print("  4 - You'll earn glory that will echo through stone forever'")
        print("")

        dwarfQ4 = 0
        while dwarfQ4 not in (1,2,3,4):
            try:
                dwarfQ4 = int(input("Choose your response 1-4 --"))
                print("")
                if dwarfQ4 == 1:
                    print("'Noble, yet naive. The only right thing to do is what's best for my people'")
                elif dwarfQ4 == 2:
                    print("'A fair warning, mayhap a true one")
                elif dwarfQ4 in (3,4):
                    print("You see a flash in the Thane's eyes - you have clearly piqued his interest")
                else:
                    print("please choose a response 1-4")
            except ValueError:
                print("please enter a number 1-4")
        if dwarfQ4 == 1 and dwarfQ3 == 2:
            print("'We'll not bleed for humans who run to us only when their roof catches fire. You'll find no allies here'")
            questsuccess = False
        elif dwarfQ4 in (2,4) and dwarfQ3 == 2:
            print("'You come seeking aid with naught but words for compensation. I grow tired'")
            print("Thane Brogdin stands and turns to leave. Do you -")
            print("  1 - Plead for aid, at the risk of angering the Thane")
            print("  2 - Quietly leave")
            dwarfQ5 = 0
            while dwarfQ5 not in (1,2):
                try:
                    dwarfQ5 = int(input("Choose your response 1-2 --"))
                    print("")
                    if dwarfQ5 == 1:
                        print("You push the matter, pleading for your village one last time")
                        print("The Thane pauses. With his back turned, you cannot read his face, but nods his head, seemingly in consideration")
                        bonusquest = True
                    elif dwarfQ5 == 2:
                        questsuccess = False
                        gameover = True
                    else:
                        print("please choose a response 1-2")
                except ValueError:
                    print("please enter a number 1-2")
        elif dwarfQ4 in (3,4) and dwarfQ3 != 2:
            print("")
            questsuccess = True
        else:
            bonusquest = True
        print("----------------------------------------------------------------------------------------------------------------------------------------------")

        # === QUEST RESOLUTION === 
        if bonusquest: #combat miniboss 
            print("'I remain unconvinced, but I shall give you opportunity to prove your worth'")
            print("'A troll has attacked our miners and must be dealt with. Do so, and you may yet deserve dwarven steel'")
            print("'Ori, send an escort to take our guest into the mines. We shall see how strong they are'")
            print("")
            print("-------------------------------------------------------------------------------------------------------")
            print("")
            print("As you descend deeper into the mines, a foul, rotting musk assaults your nostrils")
            print("Something shuffles ahead. A growl echoes from the shadows, low, guttural, and hungry")
            print("A hulking figure lurches into view, dragging a massive club that could crush a clydesdale")
            print("Gray skin slick with cave slime parts to reveal jagged teeth bared in a twisted grin.")
            print("You've found the troll, and it looks hungry")
            monster = "Troll"
            monsterhp = 30
            monsteratk = 2
            monsterspecial = 0

            # === COMBAT LOOP - HERO ACTION ===

            round = 0
            monstercharge = False
            while herohp > 0 and monsterhp > 0:
                round = round + 1
                print("********************************************")
                print(f"Round - {round}")
                print("BATTLE OPTIONS") #should I add options to check HP? or always print hero/monster hp at top?
                print("   1- Attack ⚔️")
                print("   2- Block 🛡️") #block needs more function, add 2 to atk maybe gather your strength
                print("   3- Heal Potion 💗")
                try:
                    herocombatchoice = int(input("Enter number 1-3 -- "))
                    if herocombatchoice == 1: 
                        #attack rolls d20 to check for critial hit or miss.
                        d20 = random.randint(1,20)
                        if d20 == 20:
                            print("**********************")
                            print("⚔️  CRITICAL HIT!  ⚔️")
                            print("**********************")
                            if heroblock:
                                heroatkdmg = 2 + ((heroatk + random.randint(1,3)) * 2)  #heroblock adds 2 dmg and crit hit doubles random dmg
                                heroblock = False
                            else:
                                heroatkdmg = (heroatk + random.randint(1,3)) * 2  #crit hit doubles random dmg
                            print(f"{monster} takes {heroatkdmg} damage")
                            monsterhp = monsterhp - heroatkdmg
                            if monsterhp <= 0:
                                print("")
                            else:
                                print(f"{monster} has {monsterhp} hp left")
                                print("")
                        elif d20 == 1:
                            print("")
                            print(f"{hero} Missed!")    
                        #===if not crit hit or miss, continue with normal attack - calc atk dmg using hero atk stat and randint, subtract from monster hp
                        else:
                            if heroblock: #adds 2 dmg
                                heroatkdmg = 2 + heroatk + random.randint(1,3) 
                                heroblock = False
                            else:
                                heroatkdmg = heroatk + random.randint(1,3)
                            print("")
                            print(f"{hero} attacks! {monster} takes {heroatkdmg} damage")
                            monsterhp = monsterhp - heroatkdmg
                            if monsterhp <= 0:
                                print("")
                            else:
                                print(f"{monster} has {monsterhp} hp left")
                                print("")
                    elif herocombatchoice == 2:  #===blocking reduces dmg in monster attack and adds 2 to next heroatkdmg
                        heroblock = True
                        print("")
                        print(f"{hero} conserves energy, raises shield, and braces for impact")
                        print("")
                    elif herocombatchoice == 3:
                    # === check to see if user has potions then heal 10hp up to maxhp ===
                        if potion != 0:
                            if herohp > (heromaxhp - 10):
                                herohp = heromaxhp
                                print("")
                                print(f"{hero} is fully healed")
                                print(f"{hero} has {herohp} hp")
                                print("")
                                potion = potion - 1
                            else:
                                herohp = herohp + 10
                                print("")
                                print(f"{hero} heals 10 hp")
                                print(f"{hero} has {herohp} hp")
                                print("")
                                potion = potion - 1
                        else:
                            print(f"Oh no! {hero} is out of potions") 
                            potionskip = True #skips monster attack to loop back to battle options
                    else:
                        print ("select an action 1-3")
                except ValueError:
                    print("please enter a number 1-3")

            # === COMBAT LOOP - MONSTER ACTION ===

                if potionskip:
                    potionskip = False
                    continue
                elif monsterhp > 0 and round % 3 == 0: #every 3rd round skip attack to prep special attack
                    print("⚠️---------------------------------------------------------⚠️")
                    print(f"Watch out {hero}, the {monster} is winding up for a devastating strike!")
                    print("⚠️---------------------------------------------------------⚠️")
                    monstercharge = True
                    continue
                elif monsterhp > 0: #if monster was killed in hero action, skip monster action
                    if monstercharge: #special attack every 4th round
                        print("************************")
                        print("💀------------------⚔️")
                        print("        RAMPAGE        ")
                        print("⚔️-------------------💀")
                        print("************************")
                        print(f"The {monster} roars and thrashes around wildly with his giant club")
                        monsterspecial = 5
                        monstercharge = False
                    else:
                        print(f"{monster} attacks!")

                    if heroblock: #checks for block, halves dmg (rounded down)
                        monsteratkdmg = int(monsterspecial + monsteratk - herodef + (random.randint(1,3)) / 2)
                    else:
                        monsteratkdmg = monsterspecial + monsteratk - herodef + random.randint(1,3)
                    print(f"{hero} takes {monsteratkdmg} dmg")
                    herohp = herohp - monsteratkdmg
                    monsterspecial = 0

                    if herohp <= 0:
                        print("💀💀💀💀💀💀💀💀")
                        print(f"{hero} has perished")
                        print("💀💀💀💀💀💀💀💀")
                        herodead = True
                        break
                    else:
                        print(f"{hero} has {herohp} hp left")
                        print("")
                else:
                    continue
            if not herodead:
                print("🎉🎉🎉*******************🎉🎉🎉")
                print(f"{hero} defeated the {monster}")
                print("🎉🎉🎉*******************🎉🎉🎉")
                print("")
                print("----------------------------------------------")
                herohp = heromaxhp
            else:
                break

            print("You return to the throne room covered in troll blood")
            questsuccess = True
        else:
            print("")

        if questsuccess: #gain armor and fire shield
            print("Thane Brogdin nods approvingly. 'I can see now there is strength in you, mayhap enough to face the challenge ahead'")
            print("'You may have the courage to face dragon fire, but you lack the equipment. Easily remedied.'")
            print(f"'Ori, prepare a room for our guest. Go and rest {hero}, we shall speak more tomorrow'")
            print("---------------------------------------------------------------------------------------------------------------------")
            print("In the morning, you are summoned back to the throne room")
            print("Thane Brogdin welcomes you and presents you with the finest dwarven mail you have ever seen")
            print("'My smiths worked through the night. This armor is light enough for your kind, strong enough to turn a dragon's fang'")
            print("Another smith steps forward and presents you with a dark shield, its surface shimmers in the firelight")
            print("'And this, the Emberguard. Quenched in molten obsidian, cooled in troll-blooded oil. No fire will blister your skin while this guard is raised'")
            print("(GAIN DWARVEN MAIL ARMOR)")  
            print("(GAIN EMBERGUARD SHIELD)")  
            print("(GAIN 2 10hp HEAL POTIONS)")  
            print("-----------------------------------")
            potion = potion + 2
            herodef = herodef + 4
            fireshield = True
            print("'Take these gifts, may they serve you well in the battle ahead. I send with you a regiment to help defend your village.'")
            print(f"'May the Stonefather guide your sword and shield your back. Farewell {hero}'")
        else:
            print("")

    else:
        print("⚠️ under construction ⚠️")

    # === FINAL BOSS ===
    print("---------------------------------------------------------------------------------------------------------------------")
    print("To be continued..............")
    gameover = True

# === GAME OVER - end herodead loop ===
gameover = True

