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


#####
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
        self.wallComments = ["filler"]
        self.moveComments = ["filler"]
        self.fightComments = ["filler"]
        self.compassComments = ["filler"]
        


def move(XY: list) -> int:
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
    elif (direction == "c"): #Maybe make so it points to closest object?
        compass(mechanic.XY)
        return XY
    elif (direction == "exit"):
        global quitCheck
        quitCheck = True
        return XY
    else:
        help()
        return XY

def borderMechanic(XY: int):
    if (XY > 10):
        print("\n\nYou have found a wall, it seems to be whispering something about 'Game Mechanics', how odd.\n")
        return XY - 1
    elif (XY < 0):
        print("\n\nYou have found a wall, it seems to be whispering something about 'Game Mechanics', how odd.\n")
        return XY + 1
    else:
        return XY

def encounterMechanic():
    # player.XY
    print("You have found a wild 'Game Mechanic' in it's natural habitat, a game.")
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

def encounterTreasure():
    # player.XY
    print("You have found a treasure chest\n")
    action = str(input("What will you do? (o)pen or (r)un: "))
    if (action == "o"):
        treasure.died()
        pass
    else:
        print("\nYou skedaddle, leaving the treasure behind?\n")
        player.XY = move(player.XY)

def fight():
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
        return

def compass(target: list):
    # player.XY
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

def help():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Movement Instructions:\n")
    print("Use (w),(a),(s),(d) to move North, West, South, and East,")
    print("Use (h) to view your health,")
    print("Use (c) to view the compass.\n")
    #add general move() instructions above
    print("Encounter Instructions:\n")
    print("Use (f) to fight an encountered Game Mechanic,")
    print("Use (r) to run and use the general movement controls,")
    print("Use (o) to open treasure chests.\n")
    #add encounter() instructions above
    print("Use (help) to access these tips,")
    print("Use (exit) to exit the game.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

def showCoords():
    # player.XY
    print(f"\nYou are at {player.XY[0]} X and {player.XY[1]} Y.\n")

def welcomePrints():
    print("Welcome to [insert game name]\n")
    showCoords()

def encounterCheck():
    if (player.XY == mechanic.XY):
        encounterMechanic()
    elif (player.XY == treasure.XY):
        encounterTreasure()



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
