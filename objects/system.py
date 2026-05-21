from pathlib import Path
import random
import objects.unit

class System:
  def __init__(self, player):
    self.currentFloor = 1
    self.movesLeft = 100
    self.gold = 0

    self.playerParty = [player]
    self.enemyParty = []

    self.currentMap = ["###" for _ in range(100)]
    self.playerPartyCurrentLocation = random.randint(0,99)
    self.restAreaLocation = random.randint(0,99)
    self.isRestAreaAlreadyUsed = False
    self.shopLocation = random.randint(0,99)

    self.shopItems = []
    for x in range(5):
      self.shopItems.append("{0} LVL {1}".format(random.choice(["Helmet", "Sword", "Armor", "Boots"]), random.randint(1,5)))

    self.shopRecruits = []
    for x in range(3):
      name = ""
      filepath = Path(__file__).parent / "../assets/Names"
      f = open(filepath, "r")

      names = []
      for line in f:
        names.append(line.strip())
            
      name = random.choice(names)
      
      level = random.randint(self.currentFloor*10-9,self.currentFloor*10)

      hpGrowth = 5
      atkGrowth = 5
      defGrowth = 5
      spdGrowth = 5
      for x in range(4):
        rng = random.randint(1,4)
        if rng == 1:
          hpGrowth += 1
        elif rng == 2:
          atkGrowth += 1
        elif rng == 3:
          defGrowth += 1
        elif rng == 4:
          spdGrowth += 1
      
      recruit = objects.unit.Unit("Player", name, level, hpGrowth, atkGrowth, defGrowth, spdGrowth)

      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Helmet LVL {0}".format(random.randint(1,5)))
        recruit.currentHP = recruit.maximumHP
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Sword LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Armor LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Boots LVL {0}".format(random.randint(1,5)))
      
      self.shopRecruits.append(recruit)


    self.itemLocation = random.randint(0,99)
    self.isItemAlreadyObtained = False

    self.itemsInItemRoom = []
    for x in range(3):
      self.itemsInItemRoom.append("{0} LVL {1}".format(random.choice(["Helmet", "Sword", "Armor", "Boots"]), random.randint(1,5)))

    self.exitLocation = random.randint(0,99)
    self.bossLocation = self.exitLocation

    while self.restAreaLocation == self.shopLocation or self.restAreaLocation == self.itemLocation or self.restAreaLocation == self.exitLocation or self.shopLocation == self.itemLocation or self.shopLocation == self.exitLocation or self.itemLocation == self.exitLocation:
      self.restAreaLocation = random.randint(0,99)
      self.shopLocation = random.randint(0,99)
      self.itemLocation = random.randint(0,99)
      self.exitLocation = random.randint(0,99)
      self.bossLocation = self.exitLocation
    
    self.isExplorationBonusAvailable = True

    self.allUnitsInBattle = []
      
    self.setCurrentMap()

  def setPlayerPartyCurrentLocation(self, choice):
    isUpdateSuccessful = False
    if choice == "w" and self.playerPartyCurrentLocation > 9:
      self.playerPartyCurrentLocation -= 10
      self.setCurrentMap()
      self.movesLeft -= 1
      isUpdateSuccessful = True
    elif choice == "s" and self.playerPartyCurrentLocation < 90:
      self.playerPartyCurrentLocation += 10
      self.setCurrentMap()
      self.movesLeft -= 1
      isUpdateSuccessful = True
    elif choice == "a" and self.playerPartyCurrentLocation%10 != 0:
      self.playerPartyCurrentLocation -= 1
      self.setCurrentMap()
      self.movesLeft -= 1
      isUpdateSuccessful = True
    elif choice == "d" and self.playerPartyCurrentLocation%10 != 9:
      self.playerPartyCurrentLocation += 1
      self.setCurrentMap()
      self.movesLeft -= 1
      isUpdateSuccessful = True
    
    if self.movesLeft == 0 and self.currentFloor != 10:
      self.createNewDungeonFloor()
    elif self.movesLeft == 0 and self.currentFloor == 10:
      self.createBoss()
    
    return isUpdateSuccessful
  
  def setCurrentMap(self):
    self.currentMap[self.playerPartyCurrentLocation] = "   "

  def createNewDungeonFloor(self):
    self.currentFloor += 1
    self.movesLeft = 100
    self.currentMap = ["###" for _ in range(100)]
    self.playerPartyCurrentLocation = random.randint(0,99)
    self.restAreaLocation = random.randint(0,99)
    self.isRestAreaAlreadyUsed = False
    self.shopLocation = random.randint(0,99)

    self.shopItems = []
    for x in range(5):
      self.shopItems.append("{0} LVL {1}".format(random.choice(["Helmet", "Sword", "Armor", "Boots"]), random.randint(1,5)))

    self.shopRecruits = []
    for x in range(3):
      name = ""
      filepath = Path(__file__).parent / "../assets/Names"
      f = open(filepath, "r")

      names = []
      for line in f:
        names.append(line.strip())
            
      name = random.choice(names)
      
      level = random.randint(self.currentFloor*10-9,self.currentFloor*10)

      hpGrowth = 5
      atkGrowth = 5
      defGrowth = 5
      spdGrowth = 5
      for x in range(4):
        rng = random.randint(1,4)
        if rng == 1:
          hpGrowth += 1
        elif rng == 2:
          atkGrowth += 1
        elif rng == 3:
          defGrowth += 1
        elif rng == 4:
          spdGrowth += 1
      
      recruit = objects.unit.Unit("Player", name, level, hpGrowth, atkGrowth, defGrowth, spdGrowth)

      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Helmet LVL {0}".format(random.randint(1,5)))
        recruit.currentHP = recruit.maximumHP
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Sword LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Armor LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        recruit.equipItem("Boots LVL {0}".format(random.randint(1,5)))
      self.shopRecruits.append(recruit)


    self.itemLocation = random.randint(0,99)
    self.isItemAlreadyObtained = False
    
    self.itemsInItemRoom = []
    for x in range(3):
      self.itemsInItemRoom.append("{0} LVL {1}".format(random.choice(["Helmet", "Sword", "Armor", "Boots"]), random.randint(1,5)))

    self.exitLocation = random.randint(0,99)
    while self.restAreaLocation == self.shopLocation or self.restAreaLocation == self.itemLocation or self.restAreaLocation == self.exitLocation or self.shopLocation == self.itemLocation or self.shopLocation == self.exitLocation or self.itemLocation == self.exitLocation:
      self.restAreaLocation = random.randint(0,99)
      self.shopLocation = random.randint(0,99)
      self.itemLocation = random.randint(0,99)
      self.exitLocation = random.randint(0,99)
    
    self.isExplorationBonusAvailable = True
    
    self.setCurrentMap()
  
  def healParty(self):
    for x in range(len(self.playerParty)):
      self.playerParty[x].currentHP = self.playerParty[x].maximumHP
  
  def createEnemyParty(self):
    self.enemyParty = []

    for x in range(random.randint(1,3)):
      name = "{0} {1}".format(random.choice(["Wood", "Fire", "Earth", "Metal", "Water", "Sun", "Moon", "Star"]), random.choice(["Apparition", "Construct", "Elemental", "Ghost", "Golem", "Guardian", "Phantom", "Specter"]))

      level = random.randint(self.currentFloor*10-9,self.currentFloor*10)

      hpGrowth = 5
      atkGrowth = 5
      defGrowth = 5
      spdGrowth = 5
      for x in range(4):
        rng = random.randint(1,4)
        if rng == 1:
          hpGrowth += 1
        elif rng == 2:
          atkGrowth += 1
        elif rng == 3:
          defGrowth += 1
        elif rng == 4:
          spdGrowth += 1
      
      enemy = objects.unit.Unit("Enemy", name, level, hpGrowth, atkGrowth, defGrowth, spdGrowth)

      if random.randint(1,100) <= self.currentFloor*10:
        enemy.equipItem("Helmet LVL {0}".format(random.randint(1,5)))
        enemy.currentHP = enemy.maximumHP
      
      if random.randint(1,100) <= self.currentFloor*10:
        enemy.equipItem("Sword LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        enemy.equipItem("Armor LVL {0}".format(random.randint(1,5)))
      
      if random.randint(1,100) <= self.currentFloor*10:
        enemy.equipItem("Boots LVL {0}".format(random.randint(1,5)))

      self.enemyParty.append(enemy)
  
  def createBoss(self):
    self.enemyParty = []
    boss = objects.unit.Unit("Enemy", "The Dungeon Lord", 100, 9, 9, 9, 9)

    boss.equipItem("Helmet LVL 5")
    boss.currentHP = boss.maximumHP
    boss.equipItem("Sword LVL 5")
    boss.equipItem("Armor LVL 5")
    boss.equipItem("Boots LVL 5")

    self.enemyParty.append(boss)