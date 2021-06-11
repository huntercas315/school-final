import math
from random import randrange


class stats:
    __slots__ = [
            "health",
            "originHealth",
            "attackMin",
            "attackMax",
            "XY",
            "upgrades"]
    def __init__(self, health: int, attackMin: int, attackMax: int):
        self.health = health
        self.originHealth = health
        self.attackMin = attackMin
        self.attackMax = attackMax
        self.XY = [randrange(10)+1, randrange(10)+1]
        #XY[0] is X, XY[1] is Y
        self.upgrades = ["health", "attack"]
    def attack(self, target) -> int:
        target -= randrange(self.attackMin, self.attackMax)+1
        return target
    def died(self):
        self.XY = [randrange(10)+1, randrange(10)+1]
        self.health = self.originHealth
    def upgrade(self):
        option = self.upgrades[randrange(1)]
        if (option == "health"):
            pass #may use to add weapons or armor?
        elif (option == "attack"):
            pass

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
        "fightComments",
        "compassComments"]
    def __init__(self):
        self.wallComments = ["You have found a wall, it seems to be whispering something about 'Game Mechanics', how odd.",
            "A large wall blocks your path...",
            "You seem to have encountered some lazy world design. You cannot continue in this direction, because of totally valid reasons.",
            "A tiny ledge is in your path. You could jump over it, but this world is 2d. Turn back 2d person...",
            "A low wall is blocking you from continuing, but you skipped leg day, and as such cannot jump the wall..."]
        self.moveComments = ["filler"]
        self.fightComments = ["filler"]
    def commentPrint(self, target: list) -> str:
        length = len(target)
        comment = target[randrange(length)]
        return comment

comment = comments()

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
#add maps to movement coord message, create func to check if on an encounter coord using a bool to prevent using map during an encounter



showMap = False     

def move(XY: list) -> int:
    global showMap
    direction = str(input("What Action? Use (help) to view tips: "))
    if (direction == "w"):
        temp = XY[1]+1
        temp = borderMechanic(temp)
        XY.pop(1)
        XY.insert(1, temp)
        showCoords()
        return XY
    elif (direction == "a"):
        temp = XY[0]-1
        temp = borderMechanic(temp)
        XY.pop(0)
        XY.insert(0, temp)
        showCoords()
        return XY
    elif (direction == "s"):
        temp = XY[1]-1
        temp = borderMechanic(temp)
        XY.pop(1)
        XY.insert(1, temp)
        showCoords()
        return XY
    elif (direction == "d"):
        temp = XY[0]+1
        temp = borderMechanic(temp)
        XY.pop(0)
        XY.insert(0, temp)
        showCoords()
        return XY
    elif (direction == "h"):
        print(f"\nHealth: {player.health}\n")
        return XY
    elif (direction == "help"):
        help()
        return XY
    elif (direction == "c"):
        compassAllFunc()
        return XY
    elif (direction == "m"):
        maps.drawMap()
        return XY
    elif (direction == "map"):
        if showMap:
            showMap = False
            print("\nThe map has been turned off.\n")
        else:
            showMap = True
            print("\nThe map has been turned on.\n")
        return XY
    elif (direction == "exit"):
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

def encounterMechanic() -> None:
    print("You have found a wild 'Game Mechanic' in it's natural habitat, a game.")
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
        ####
        print("Incomplete mechanic, come back later...")
        #####
        treasure.died()
        maps.treasure = [-1,-1]
        pass #NEEDS A TREASURE MECHANIC
    else:
        print("\nYou skedaddle, leaving the treasure behind?\n")
        player.XY = move(player.XY)

def fight() -> None:
    #Player Attack
    mechanicHealth = mechanic.health
    print("*BONK*\n")
    mechanicHealth = player.attack(mechanicHealth)
    mechanic.health = mechanicHealth
    if (mechanic.health < 0):
        mechanic.health = 0
    print(f"The Game Mechanic has {mechanic.health} health left.\n")
    if (mechanic.health == 0):
        print("\n\nThe Game Mechanic has died...\n\n")
        mechanic.died()
        return
    #The waiting/timer part
    timer = 9999999
    while (timer != 0):
        timer -= 1
    #Game Mechanic Attack
    playerHealth = player.health
    print("\"Attack Noises\"\n")
    playerHealth = mechanic.attack(playerHealth)
    player.health = playerHealth
    if (player.health < 0):
        player.health = 0
    print(f"You have {player.health} health left.\n")
    if (player.health == 0):
        print("\n\n\n...You Died...\n\n\n")
        player.died()

def compassAllFunc() -> None:
    closest = closestObject()
    if (distFinder(closest) > 5):
        print("\nThe compass cannot find anything nearby.\n")
        return
    compass(closest)

def closestObject() -> list:
    distance = 99999
    point = []
    #Finding distances
    distMechanic = distFinder(mechanic.XY)
    if (distMechanic < distance):
        point = mechanic.XY
        distance = distMechanic
    distTreasure = distFinder(treasure.XY)
    if (distTreasure < distance):
        point = treasure.XY
        distance = distTreasure
    #Returning closest
    return point

def distFinder(target: list) -> float:
    global distanceList
    sideDist = lambda point, player: abs((player - point))
    a = sideDist(target[0], player.XY[0])
    b = sideDist(target[1], player.XY[1])
    a = pow(a, 2)
    b = pow(b, 2)
    c = a + b
    c = math.sqrt(c)
    return c

def compass(target: list) -> None:
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

def help() -> None:
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Movement Instructions:\n")
    print("Use (w),(a),(s),(d) to move North, West, South, and East,")
    print("Use (h) to view your health,")
    print("Use (c) to use the compass and find nearby objects,")
    print("Use (m) to view the map,")
    print("Use (map) to toggle viewing the map when moving.\n")
    #add general move() instructions above
    print("Encounter Instructions:\n")
    print("Use (f) to fight an encountered Game Mechanic,")
    print("Use (r) to run and use the general movement controls,")
    print("Use (o) to open treasure chests.\n")
    #add encounter() instructions above
    print("Use (help) to access these tips,")
    print("Use (exit) to exit the game.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def showCoords() -> None: #Informs the player of their location after movement
    if showMap:
        maps.drawMap()
        print(f"You are at {player.XY[0]} X and {player.XY[1]} Y.\n")
    else:
        print(f"\nYou are at {player.XY[0]} X and {player.XY[1]} Y.\n")
    #PUT A COMMENT FUNC HERE

def welcomePrints() -> None: 
    print("Welcome to [insert game name]\n")
    showCoords()

def encounterCheck() -> None: #Triggers events
    if (player.XY == mechanic.XY):
        encounterMechanic()
    elif (player.XY == treasure.XY):
        encounterTreasure()

def encounterCheck() -> bool: #This is for disabling displaying coords and the map
    if (player.XY == mechanic.XY):
        return True
    elif (player.XY == treasure.XY):
        return True
    else:
        return False



#The Starting Parts
quitCheck = False

welcomePrints()
while True:
    #The encounter part
    encounterCheck()
    #The exit/quit part
    if quitCheck:
        break
    #The general movement part
    player.XY = move(player.XY)
