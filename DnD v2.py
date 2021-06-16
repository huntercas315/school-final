import math
from random import randrange


quitCheck = False


class options:
    __slots__ = [
            "showMap",
            "showComments"]
    def __init__(self, maps: bool, comments: bool):
        self.showMap = maps
        self.showComments = comments
    def optionsViewer(self) -> None:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Options:")
        print("    Enter (map) to toggle displaying the map during movement,")
        print("    Enter (comments) to toggle displaying the comments during movement,")
        print("    Enter (done) to leave this menu.")
        while True:
            option = str(input("Option: "))
            if (option == "map" or option == "MAP"):
                self.showMap = self.toggle(self.showMap)
            elif (option == "comments" or option == "COMMENTS"):
                self.showComments = self.toggle(self.showComments)
            elif (option == "done" or option == "DONE"):
                break
            else:
                break
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
    def toggle(self, option: bool) -> bool:
        if option:
            print("The option is now off.")
            return False
        else:
            print("The option is now on.")
            return True

options = options(False, True)

class stats:
    __slots__ = [
            "icon",
            "health",
            "maxHealth",
            "originHealth",
            "attackMin",
            "attackMax",
            "attackBuff",
            "heals",
            "coins",
            "XY"]
    def __init__(self, icon: str, health: int, attackMin: int, attackMax: int, heals: int, coins: int):
        self.icon = icon
        self.health = health
        self.maxHealth = health
        self.originHealth = health
        self.attackMin = attackMin
        self.attackMax = attackMax
        self.attackBuff = 0
        self.heals = heals
        self.coins = coins
        self.XY = [randrange(10)+1, randrange(10)+1]
        #XY[0] is X, XY[1] is Y
    def attack(self, target) -> int:
        damage = randrange(self.attackMin, self.attackMax)+1
        damage += self.attackBuff
        target -= damage
        if (target < 0):
            target = 0
        return target
    def died(self):
        self.XY = [randrange(10)+1, randrange(10)+1]
        self.health = self.originHealth
        self.maxHealth = self.originHealth
        self.attackBuff = 0
        self.heals = 0
        self.coins = 0
    def upgrade(self):
        option = input("\nWhat would you like to upgrade? (h)ealth or (d)amage: ")
        while (option != "h" and option != "H" and option != "d" and option != "D"):
            option = input("\nWhat would you like to upgrade? (h)ealth or (d)amage: ")
        if (option == "h" or option == "H"):
            buff = randrange(2,5)
            self.maxHealth += buff
            print(f"\nYou have found an item that increased your max health by {buff}!\n")
        elif (option == "d" or option == "D"):
            buff = randrange(1,2)
            self.attackBuff += buff
            print(f"\nYou have found an item that buffed your damage by {buff}!\n") 
    def heal(self):
        if (self.heals > 0):
            self.heals -= 1
            self.health += 3
            if (self.health > self.maxHealth):
                self.health = self.maxHealth
            print(f"\nYou have used a healing item, your health is now {self.health} and you have {self.heals} healing items left.\n")
        else:
            print("\nYou have no healing items left.\n")
    def statViewer(self) -> None:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Stats:")
        print(f"    Health: {self.health}/{self.maxHealth}")
        print(f"    Attack: {self.attackMin+1}-{self.attackMax}")
        print(f"    Attack Buffed by +{self.attackBuff}")
        print()
        print(f"    Coins: {self.coins}")
        print(f"    Healing Items: {self.heals}")
        print()
        print(f"    X: {self.XY[0]}")
        print(f"    Y: {self.XY[1]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

player = stats("@", 10, 0, 3, 2, 50)
treasure = stats("=", 0, 0, 0, 0, 0)


class mechanicStats:
    __slots__ = [
            "icon",
            "health",
            "originHealth",
            "attackMin",
            "attackMax",
            "attackBuff",
            "XY"]
    def __init__(self, icon: str, health: int, attackMin: int, attackMax: int):
        self.icon = icon
        self.health = health
        self.originHealth = health
        self.attackMin = attackMin
        self.attackMax = attackMax
        self.attackBuff = 0
        self.XY = [randrange(10)+1, randrange(10)+1]
        #XY[0] is X, XY[1] is Y
    def attack(self, target) -> int:
        damage = randrange(self.attackMin, self.attackMax)+1
        damage += self.attackBuff
        target -= damage
        if (target < 0):
            target = 0
        return target
    def died(self):
        self.XY = [randrange(10)+1, randrange(10)+1]
        self.health = self.originHealth + 3
        self.originHealth = self.health
        self.attackBuff += 1
        maps.mechanic = [-1,-1]
        
mechanic = mechanicStats("!", 5, 0, 2)



class comments:
    __slots__ = [
        "wallComments",
        "moveComments",
        "fightComments"]
    def __init__(self):
        self.wallComments = ["You have found a wall, it seems to be whispering something about 'Game Mechanics', how odd.",
            "A large wall blocks your path...",
            "You seem to have encountered some lazy world design. You cannot continue in this direction, because of totally valid reasons.",
            "A tiny ledge is in your path. You could jump over it, but this world is 2d. Turn back 2d person...",
            "A low wall is blocking you from continuing, but you skipped leg day, and as such cannot jump the wall..."]

        self.moveComments = ["You have wandered into a desert.",
            "A potato field surounds you.",
            "An abandoned city looms before you, silent and empty.",
            "You have chanced upon an incredibly beautiful field, if only graphics were implemented...",
            "You have stepped into an apple orchard.",
            "You have stumbled across the wonderous Screaming Goat! Say goodbye to your sanity!",
            "The entrance to a dungeon lies before you, but you are claustrophobic and cannot enter for valid reasons.",
            "An abandoned tower blocks out the sky above you.",
            "A coconut lies in the middle of the path, not a swallow in sight. It would be best to move on...",
            "You come across some peasants in a field, they seem to be arguing about the constitution.",
            "A cave is within sight, but it is guarded by a rabbit and you have no holy handgrenades on hand...",
            "A swallow flies on the horizon, carrying coconuts to distant non-tropical lands."]
        
        self.fightComments = ["*bonk*",
            "*Bam*", "*Smack*", "*Bop*", "*Bing Bong*", "Onomatopoeia!", "*Attack Noises!*",
            "*Procedural Noise Generation!*"]
        
    def commentPrint(self, target: list) -> str:
        length = len(target)
        comment = target[randrange(length)]
        return comment

comment = comments()#Make a settings menu to enable and disable maps and comments



class compass:
    def compassAllFunc(self) -> None:
        closest = self.closestObject()
        if (self.distFinder(closest) > 5):
            print("\nThe compass cannot find anything nearby.\n")
            return
        self.compass(closest)

    def closestObject(self) -> list:
        distance = 99999
        point = []
        #Finding distances
        distMechanic = self.distFinder(mechanic.XY)
        if (distMechanic < distance):
            point = mechanic.XY
            distance = distMechanic
        distTreasure = self.distFinder(treasure.XY)
        if (distTreasure < distance):
            point = treasure.XY
            distance = distTreasure
        #Returning closest
        return point

    def distFinder(self, target: list) -> float:
        global distanceList
        sideDist = lambda point, player: abs((player - point))
        a = sideDist(target[0], player.XY[0])
        b = sideDist(target[1], player.XY[1])
        a = pow(a, 2)
        b = pow(b, 2)
        c = a + b
        c = math.sqrt(c)
        return c

    def compass(self, target: list) -> None:
        if (player.XY == target):
            print("\nThe Compass is spinning, you have arrived. The destination is on your right...\n")
            return
        #North/South
        if (player.XY[1] < target[1]):
            yCompass = "North"
        elif (player.XY[1] > target[1]):
            yCompass = "South"
        else:
            yCompass = ""
        #East/West
        if (player.XY[0] < target[0]):
            xCompass = "East"
        elif (player.XY[0] > target[0]):
            xCompass = "West"
        else:
            xCompass = ""
        #Direction Creation
        compass = yCompass+xCompass
        print(f"\nThe Compass is pointing {compass}.\n")

compass = compass()

class shop:
    __slots__ = [
        "location",
        "heals",
        "healsPrice",
        "upgrades",
        "upgradesPrice",
        "selections"]
    def __init__(self, heals: int, upgrades: int):
        self.location = [3,3]
        self.heals = heals
        self.healsPrice = 50
        self.upgrades = upgrades
        self.upgradesPrice = 125
        self.selections = ["done","DONE","h","H","u","U"]
    def startStore(self) -> None:
        enter = input("\n\nYou have found the shop, enter? (y)/(n): ")
        if (enter == "y" or enter == "Y"):
            self.openStore()
        else:
            return
    def openStore(self) -> None:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Shop:")
        print(f"    (h)ealing items | {self.healsPrice} COINS  | Stock: {self.heals}")
        print(f"    (u)pgrades      | {self.upgradesPrice} COINS | Stock: {self.upgrades}")
        print()
        print("    (done)")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        
        while True:
            print(f"You have {player.coins} COINS")
            choice = input("What are you buying: ")
            if choice not in self.selections:
                break
            elif (choice == "done" or choice == "DONE"):
                print()
                break
            else:
                self.buy(choice)
    def buy(self, item: str) -> None:
        if (item == "h" or item == "H"):
            quantity = int(input("How many? "))
            while (quantity > self.heals or quantity < 0):
                print("The shop does not have that much in stock.")
                quantity = input("How many? ")
            if (quantity == 0):
                return
            cost = self.healsPrice * quantity
            if (cost > player.coins):
                print(f"\nYou can't afford this, you have {player.coins} coins, the cost is {cost}\n")
                return
            player.coins -= cost
            player.heals += quantity
            print(f"\nYou now have {player.heals} healing items and {player.coins} coins left.\n")
        elif (item == "u" or item == "U"):
            cost = self.upgradesPrice
            if (cost > player.coins):
                print(f"\nYou can't afford this, you have {player.coins} coins, the cost is {cost}\n")
                return
            player.coins -= cost
            option = input("\nWhat would you like to upgrade? (h)ealth or (d)amage: ")
            while (option != "h" and option != "H" and option != "d" and option != "D"):
                option = input("\nWhat would you like to upgrade? (h)ealth or (d)amage: ")
            if (option == "h" or option == "H"):
                buff = randrange(2,5)
                player.maxHealth += buff
                print(f"\nYou have increased your max health by {buff}!\n")
            elif (option == "d" or option == "D"):
                buff = randrange(1,2)
                player.attackBuff += buff
                print(f"\nYou have buffed your damage by {buff}!\n")

shop = shop(4, 2)


class mapStuff:
    __slots__ = [
        "digits",
        "shop",
        "mechanic",
        "treasure"]
    def __init__(self):
        self.digits = []
        self.shop = [-1,-1]
        self.mechanic = [-1,-1]
        self.treasure = [-1,-1]
    def drawMap(self) -> None:
        self.digits = []
        self.digits.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for i in range(11):
            digitTemp = ["|"]
            for e in range(11):
                if (player.XY[1] == i and player.XY[0] == e):
                    digitTemp.append(f"[{player.icon}]")
                elif (self.shop[1] == i and self.shop[0] == e):
                    digitTemp.append("[$]")
                elif (self.treasure[1] == i and self.treasure[0] == e):
                    digitTemp.append(f"[{treasure.icon}]")
                elif (self.mechanic[1] == i and self.mechanic[0] == e):
                    digitTemp.append(f"[{mechanic.icon}]")
                else:
                    digitTemp.append("[_]")
            digitTemp.append("|")
            self.digits.append(digitTemp)
        self.digits.append("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.digits.reverse()
        for z in self.digits:
            lineString = ""
            for u in z:
                lineString += u
            print(lineString)
    def addLocation(self, location: str) -> None:
        if (location == "shop"):
            if (self.shop == [-1,-1]):
                print("\nYour map has been updated\n")
                self.shop = shop.location
        elif (location == "mechanic"):
            if (self.mechanic == [-1,-1]):
                print("\nYour map has been updated\n")
                self.mechanic = mechanic.XY
        elif ( location == "treasure"):
            if (self.treasure == [-1,-1]):
                print("\nYour map has been updated\n")
                self.treasure = treasure.XY
        else:
            return

maps = mapStuff()

class combat:
    __slots__ = [
        "encounter"]
    def __init__(self):
        self.encounter = "none" #MAY NOT BE NEEDED
    def fightAll(self, objTarget: str):
        if (objTarget == "player"):
            ##player.health = #NEEDS OWN FUNC
        if (objTarget == "mechanic"):
            mechanic.health = fightMechanic(mechanic.health)
    def fightMechanic(self, targetHealth: int) -> int: #The game mechanic's fighting function #NEEDS REFACTOR - MAYBE
        #Player Attack
        targetHealth = player.attack(targetHealth)
        print(comment.commentPrint(comment.fightComments), "\n") #Attack Comment
        print(f"The Game Mechanic has {targetHealth} health left.\n")
        return targetHealth
    def dieCheck(self, targetHealth: int, target: str) -> int:
        if (targetHealth == 0):
            if (target == "mechanic"):
                mechanic.died()
            elif (target == "player"):
                player.died()
combat = combat()




def move(XY: list) -> list:
    global showMap
    direction = str(input("What Action? Use (help) to view tips: "))
    if (direction == "w" or direction == "W"):
        temp = XY[1]+1
        temp = borderMechanic(temp)
        XY.pop(1)
        XY.insert(1, temp)
        showCoords()
        return XY
    elif (direction == "a" or direction == "A"):
        temp = XY[0]-1
        temp = borderMechanic(temp)
        XY.pop(0)
        XY.insert(0, temp)
        showCoords()
        return XY
    elif (direction == "s" or direction == "S"):
        temp = XY[1]-1
        temp = borderMechanic(temp)
        XY.pop(1)
        XY.insert(1, temp)
        showCoords()
        return XY
    elif (direction == "d" or direction == "D"):
        temp = XY[0]+1
        temp = borderMechanic(temp)
        XY.pop(0)
        XY.insert(0, temp)
        showCoords()
        return XY
    elif (direction == "h" or direction == "H"):
        print(f"\nHealth: {player.health}/{player.maxHealth}\n")
        return XY
    elif (direction == "help" or direction == "HELP"):
        help()
        return XY
    elif (direction == "c" or direction == "C"):
        compass.compassAllFunc()
        return XY
    elif (direction == "m" or direction == "M"):
        maps.drawMap()
        return XY
    elif (direction == "heal" or direction == "HEAL"):
        player.heal()
        return XY
    elif (direction == "stats" or direction == "STATS"):
        player.statViewer()
        return XY
    elif (direction == "options" or direction == "OPTIONS"):
        options.optionsViewer()
        return XY
    elif (direction == "exit" or direction == "EXIT"):
        global quitCheck
        quitCheck = True
        return XY
    ###########
    elif (direction == "beta"): #BETA STUFF - REMOVE LATER
        ##### Beta stuff
        print(treasure.XY)
        print(mechanic.XY)
        #####
        return XY
    elif (direction == "beta2"):
        player.coins += 250
        return XY
    elif (direction == "beta3"):
        player.upgrade()
        return XY
    elif (direction == "beta4"):
        maps.addLocation("mechanic")
        maps.addLocation("treasure")
        maps.addLocation("shop")
        return XY
    ##########
    else:
        help()
        return XY

def borderMechanic(XY: int) -> int:
    if (XY > 10):
        print("\n",comment.commentPrint(comment.wallComments),"\n")
        return XY - 1
    elif (XY < 0):
        print("\n",comment.commentPrint(comment.wallComments),"\n")
        return XY + 1
    else:
        return XY

def encounterTreasure() -> None:
    maps.addLocation("treasure")
    print("You have found a treasure chest\n")
    action = str(input("What will you do? (o)pen or (r)un: "))
    if (action == "o" or action == "O"):
        coinToss = randrange(1,100)
        if (coinToss in range(80,100)):
            player.upgrade()
        else:
            coinTemp = randrange(50,200)
            player.coins += coinTemp
            print(f"\nYou have found {coinTemp} coins!\n")
        treasure.died()
        maps.treasure = [-1,-1]
    else:
        print("\nYou skedaddle, leaving the treasure behind?\n")
        player.XY = move(player.XY)

def encounterMechanic() -> None: #NEEDS REFACTOR - or does?
    maps.addLocation("mechanic")
    print("\nYou have found a wild 'Game Mechanic' in it's natural habitat, a game.")
    action = "f"
    while True:
        action = str(input("What will you do? (f)ight, (heal) or (r)un: "))
        print()
        if (action == "f" or action == "F"):
            print("\nYou attack the Game Mechanic...\n")
            combat.fightAll("mechanic")
            if (player.XY != mechanic.XY):
                break
        elif (action == "heal" or action == "HEAL"):
            player.heal()
        else:
            print("\nYou scamper, giving the Flash a run for his money...\n")
            player.XY = move(player.XY)
            break

def fightMechanic(targetHealth) -> None: #The game mechanic's fighting function #NEEDS REFACTOR - MAYBE
    #Player Attack
    targetHealth = player.attack(targetHealth)
    print(comment.commentPrint(comment.fightComments), "\n") #Attack Comment
    print(f"The Game Mechanic has {targetHealth} health left.\n")
##    if (targetHealth == 0): 
##        print("\n\n...The Game Mechanic has died...\n\n")#NEED TO CHANGE - Maybe global encounter var and use to decide which die() func to use?
##        mechanic.died()
##        coinLoot = randrange(25,75)
##        print(f"You have gained {coinLoot} coins!\n")
##        player.coins += coinLoot
##        return
    return targetHealth
    #The waiting/timer part
    ################################
##    timer = 9999999
##    while (timer != 0):
##        timer -= 1
##    #Game Mechanic Attack
##    playerHealth = player.health
##    playerHealth = mechanic.attack(playerHealth) #MAKE A SEPERATE PART. Player object stuff can stay
##    player.health = playerHealth
##    print(comment.commentPrint(comment.fightComments), "\n") #Attack Comment
##    if (player.health < 0):
##        player.health = 0
##    print(f"You have {player.health} health left.\n")
##    if (player.health == 0):
##        print("\n\n\n...You Died...\n\n\n")
##        player.died()

def coordCheck(XY: list) -> list:
    while (XY == player.XY or XY == shop.location):
        XY = [randrange(10)+1, randrange(10)+1]
    return XY

def help() -> None:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Movement Instructions:\n")
    print("Use (w),(a),(s),(d) to move North, West, South, and East,")
    print("Use (h) to view your health,")
    print("Use (heal) to use a healing item to gain health,")
    print("Use (c) to use the compass and find nearby objects,")
    print("Use (m) to view the map,")
    print("Use (stats) to view stats.\n")
    #add general move() instructions above
    print("Encounter Instructions:\n")
    print("Use (f) to fight an encountered Game Mechanic,")
    print("Use (heal) to use a healing item to gain health,")
    print("Use (r) to run and use the general movement controls,")
    print("Use (o) to open treasure chests.\n")
    #add encounter() instructions above
    print("Shop Instructions:")
    print("When at a shop, enter the item you would like to purchase,")
    print("If you have enough gold, you will be able to buy items for healing or upgrading yourself,")
    print("Enter (done) to finish your shopping,")
    print("Get more coins from treasure chests and Game Mechanics.\n")
    print("Use (options) to open the options menu,")
    print("Use (help) to access these tips,")
    print("Use (exit) to exit the game.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def showCoords() -> None: #Informs the player of their location after movement
    if encounterCheckBool(): #Check is player is at an encounter and whether to continue the function
        return
    if options.showMap: #shows the map if enabled
        maps.drawMap()
    else:
        print()

    print(f"You are at X: {player.XY[0]} and Y: {player.XY[1]}.")
    
    if options.showComments: #shows a wee message if enabled
        print(comment.commentPrint(comment.moveComments))
    print()

def welcomePrints() -> None: 
    print("Welcome to [insert generic game name]\n")
    showCoords()

def encounterCheck() -> None: #Triggers events
    if (player.XY == shop.location):
        maps.addLocation("shop")
        shop.startStore()
    elif (player.XY == mechanic.XY):
        encounterMechanic()
    elif (player.XY == treasure.XY):
        encounterTreasure()

def encounterCheckBool() -> bool: #This is for disabling displaying coords and the map
    if (player.XY == mechanic.XY):
        return True
    elif (player.XY == treasure.XY):
        return True
    else:
        return False

mechanic.XY = coordCheck(mechanic.XY)
treasure.XY = coordCheck(treasure.XY)

#The Starting Parts

welcomePrints()
while True:
    #The exit/quit part
    if quitCheck:
        break
    #Checks for encounters
    encounterCheck()
    #The exit/quit part
    if quitCheck:
        break
    #The general movement part
    player.XY = move(player.XY)
