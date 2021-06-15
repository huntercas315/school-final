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
            "health",
            "maxHealth",
            "originHealth",
            "attackMin",
            "attackMax",
            "attackBuff",
            "XY"]
    def __init__(self, health: int, attackMin: int, attackMax: int):
        self.health = health
        self.maxHealth = health
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
        return target
    def died(self):
        self.XY = [randrange(10)+1, randrange(10)+1]
        self.health = self.originHealth
        self.attackBuff = 0
    def upgrade(self):
        option = input("What would you like to upgrade? (h)ealth or (d)amage: ")
        while (option != "h" and option != "H" and option != "d" and option != "D"):
            option = input("What would you like to upgrade? (h)ealth or (d)amage: ")
        if (option == "h" or option == "H"):
            buff = randrange(2,5)
            self.health += buff
            print(f"You have found an item that increased your health by {buff}!")#add \n's where needed, future me #tell player how much of an increase
        elif (option == "d" or option == "D"):
            buff = randrange(1,3)
            self.attackBuff += buff
            print(f"You have found an item that buffed your damage by {buff}!") #ditto #Make so it adds a value to the random damage func | damageMin to Max then + buff
    def statViewer(self) -> None:
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Stats:")
        print(f"    Health: {self.health}/{self.maxHealth}")
        print(f"    Attack: {self.attackMin+1}-{self.attackMax}")
        print(f"    X: {self.XY[0]}")
        print(f"    Y: {self.XY[1]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()

player = stats(10, 0, 3)
mechanic = stats(5, 0, 2)
treasure = stats(0, 0, 0)

while (player.XY is mechanic.XY):
    mechanic.XY = [randrange(10)+1, randrange(10)+1]
while (player.XY is treasure.XY):
    treasure.XY = [randrange(10)+1, randrange(10)+1]


##### Beta stuff
print(treasure.XY)
print(mechanic.XY)
#####


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
            "A potato field surounds you.", "An abandoned city looms before you, silent and empty", "You have chanced upon an incredibly beautiful field, if only graphics were implemented...",
            "You have stepped into an apple orchard.", "You have stumbled across the wonderous Screaming Goat! Say goodbye to your sanity!",
            "The entrance to a dungeon lies before you, but you are claustrophobic and cannot enter for valid reasons"]
        
        self.fightComments = ["*bonk*",
            "*Bam*", "*Smack*", "*Bop*", "*Bing Bong*", "onomatopoeia!", "*Attack Noises!*"]
        
    def commentPrint(self, target: list) -> str:
        length = len(target)
        comment = target[randrange(length)]
        return comment

comment = comments()#Make a settings menu to enable and disable maps and comments

class mapStuff:
    __slots__ = [
        "digits",
        "mechanic",
        "treasure"]
    def __init__(self):
        self.digits = []
        self.mechanic = [-1,-1]
        self.treasure = [-1,-1]
    def drawMap(self):
        self.digits = []
        self.digits.append("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for i in range(11):
            digitTemp = ["|"]
            for e in range(11):
                if (player.XY[1] == i and player.XY[0] == e):
                    digitTemp.append("[@]")
                elif (self.treasure[1] == i and self.treasure[0] == e):
                    digitTemp.append("[=]")
                elif (self.mechanic[1] == i and self.mechanic[0] == e):
                    digitTemp.append("[!]")
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

maps = mapStuff()

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
        print(f"\nHealth: {player.health}\n")
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

def encounterMechanic() -> None: #NEEDS REFACTOR
    print("\nYou have found a wild 'Game Mechanic' in it's natural habitat, a game.")
    maps.mechanic = mechanic.XY
    action = "f"
    while (action == "f"):
        action = str(input("What will you do? (f)ight or (r)un: "))
        print()
        if (action == "f"):
            print("\nYou attack the Game Mechanic...\n")
            fight()
            if (player.XY != mechanic.XY):
                break
        else:
            print("\nYou scamper, giving the Flash a run for his money...\n")
            player.XY = move(player.XY)

def encounterTreasure() -> None:
    print("You have found a treasure chest\n")
    maps.treasure = treasure.XY
    action = str(input("What will you do? (o)pen or (r)un: "))
    if (action == "o"):
        player.upgrade()
        treasure.died()
        maps.treasure = [-1,-1]
    else:
        print("\nYou skedaddle, leaving the treasure behind?\n")
        player.XY = move(player.XY)


#When starting fight, add buff to health values
def fight() -> None: #NEEDS REFACTOR
    #Player Attack
    mechanicHealth = mechanic.health
    mechanicHealth = player.attack(mechanicHealth)
    mechanic.health = mechanicHealth
    print(comment.commentPrint(comment.fightComments), "\n") #Attack Comment
    if (mechanic.health < 0):
        mechanic.health = 0
    print(f"The Game Mechanic has {mechanic.health} health left.\n")
    if (mechanic.health == 0):
        print("\n\n...The Game Mechanic has died...\n\n")
        mechanic.died()
        return
    #The waiting/timer part
    timer = 9999999
    while (timer != 0):
        timer -= 1
    #Game Mechanic Attack
    playerHealth = player.health
    playerHealth = mechanic.attack(playerHealth)
    player.health = playerHealth
    print(comment.commentPrint(comment.fightComments), "\n") #Attack Comment
    if (player.health < 0):
        player.health = 0
    print(f"You have {player.health} health left.\n")
    if (player.health == 0):
        print("\n\n\n...You Died...\n\n\n")
        player.died()

def help() -> None:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Movement Instructions:\n")
    print("Use (w),(a),(s),(d) to move North, West, South, and East,")
    print("Use (h) to view your health,")
    print("Use (c) to use the compass and find nearby objects,")
    print("Use (m) to view the map,")
    print("Use (stats) to view stats.\n")
    #add general move() instructions above
    print("Encounter Instructions:\n")
    print("Use (f) to fight an encountered Game Mechanic,")
    print("Use (r) to run and use the general movement controls,")
    print("Use (o) to open treasure chests.\n")
    #add encounter() instructions above
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
    if (player.XY == mechanic.XY):
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



#The Starting Parts

welcomePrints()
while True:
    #Checks for encounters
    encounterCheck()
    #The exit/quit part
    if quitCheck:
        break
    #The general movement part
    player.XY = move(player.XY)
