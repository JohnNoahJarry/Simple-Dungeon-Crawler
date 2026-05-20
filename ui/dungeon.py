def displayMapScreen(system):
  print('''[================================]''')
  
  output = ""
  for x in range(len(system.currentMap)):
    
    if x == system.playerPartyCurrentLocation:
      if x%10 == 0:
        output += " | P "
      elif x%10 == 9:
        output += " P |"
        print(output)
        output = ""
      else:
        output += " P "
    elif system.currentMap[x] != "###" and x == system.restAreaLocation:
      if x%10 == 0:
        output += " | R "
      elif x%10 == 9:
        output += " R |"
        print(output)
        output = ""
      else:
        output += " R "
    elif system.currentMap[x] != "###" and x == system.shopLocation:
      if x%10 == 0:
        output += " | S "
      elif x%10 == 9:
        output += " S |"
        print(output)
        output = ""
      else:
        output += " S "
    elif system.currentMap[x] != "###" and x == system.itemLocation:
      if x%10 == 0:
        output += " | I "
      elif x%10 == 9:
        output += " I |"
        print(output)
        output = ""
      else:
        output += " I "
    elif system.currentMap[x] != "###" and x == system.exitLocation and system.currentFloor != 10:
      if x%10 == 0:
        output += " | E "
      elif x%10 == 9:
        output += " E |"
        print(output)
        output = ""
      else:
        output += " E "
    elif system.currentMap[x] != "###" and x == system.bossLocation and system.currentFloor == 10:
      if x%10 == 0:
        output += " | B "
      elif x%10 == 9:
        output += " B |"
        print(output)
        output = ""
      else:
        output += " B "
    elif x%10 == 0:
      output += " |"
      output += system.currentMap[x]
    elif x%10 == 9:
      output += system.currentMap[x]
      output += "|"
      print(output)
      output = ""
    else:
      output += system.currentMap[x]
  
  print('''[================================]
''')
  
def displayNavigation(system):
  if system.playerPartyCurrentLocation > 9:
    print("[W] = Move Up")
  if system.playerPartyCurrentLocation < 90:
    print("[S] = Move Down")
  if system.playerPartyCurrentLocation%10 != 0:
    print("[A] = Move Left")
  if system.playerPartyCurrentLocation%10 != 9:
    print("[D] = Move Right")
  
  print()

def displayExitScreen(system):
  if system.currentFloor != 10:
    print('''[========]
 | Exit |
[========]

>> Do you wish to proceed to the next floor?
        
[1] = Yes
''')
  elif system.currentFloor == 10:
    print('''[========]
 | Boss |
[========]

>> Do you wish to fight the Boss?
        
[1] = Yes
''')
  
def displayRestAreaScreen(system):
  print('''[=============]
 | Rest Area |
[=============]

>> Welcome to the Rest Area.
>> Here, you may heal your wounds, but only once per floor.

{0}
'''.format("[1] = Rest" if system.isRestAreaAlreadyUsed == False else ">> You have already used this Rest Area."))
  
def displayItemScreen(system):
  print('''[========]
 | Item |
[========]
        
>> Welcome to the Item room.
>> Choose which item to obtain.
''')
  
  if system.isItemAlreadyObtained == False:
    for x in range(len(system.itemsInItemRoom)):
      print("[{0}] = {1}".format(x+1, system.itemsInItemRoom[x]))
  elif system.isItemAlreadyObtained == True:
    print(">> You have already obtained an item here.")

  print()

def displayItemAssignScreen(choice, system):
  print('''[========]
 | Item |
[========]

>> To whom do you want to equip the {0}?
'''.format(system.itemsInItemRoom[choice]))
  
  for x in range(len(system.playerParty)):
    print("[{0}] = {1}".format(x+1, system.playerParty[x].name))
  
  print()

def displayShopScreen():
  print('''[========]
 | Shop |
[========]

>> Welcome to the Shop.
>> What would you like to do?

[1] = Buy Items
[2] = Recruit Allies
''')
  
def displayShopItemsScreen(system):
  print('''[========]
 | Shop |
[========]

>> What item do you want to buy?
>> All items cost {0} Gold.
'''.format(system.currentFloor*10))

  if system.gold < system.currentFloor*10:
    print(">> You do not have enough Gold!")
    print()

  for x in range(len(system.shopItems)):
      print("[{0}] = {1}".format(x+1, system.shopItems[x]))
  
  if len(system.shopItems) == 0:
    print(">> You have sold out the shop.")
  
  print()

def displayShopItemAssignScreen(choice, system):
  print('''[========]
 | Shop |
[========]

>> To whom do you want to equip the {0} you just bought?
'''.format(system.shopItems[choice]))
  
  for x in range(len(system.playerParty)):
    print("[{0}] = {1}".format(x+1, system.playerParty[x].name))
  
  print()

def displayShopRecruitsScreen(system):
  print('''[========]
 | Shop |
[========]

>> Who do you wish to recruit?
>> All recruits cost {0} Gold.
'''.format(system.currentFloor*10))
  
  if system.gold < system.currentFloor*10:
    print(">> You do not have enough Gold!")
    print()
  
  if len(system.playerParty) == 3:
    print(">> Your party is full.")
    print()
  
  if len(system.shopRecruits) == 0:
    print(">> There are no more recruits left.")
    print()
  
  for x in range(len(system.shopRecruits)):
    print("[{0}] {1:<18} LVL {2:<3} HP: {3:<3} ATK: {4:<3} DEF: {5:<3} SPD: {6:<3} Head: {7:<12} Hand: {8:<11} Body: {9:<11} Feet: {10:<11}".format(x+1, 
                                                                                                                                        system.shopRecruits[x].name, 
                                                                                                                                        system.shopRecruits[x].level, 
                                                                                                                                        system.shopRecruits[x].maximumHP,
                                                                                                                                        system.shopRecruits[x].atkStat, 
                                                                                                                                        system.shopRecruits[x].defStat, 
                                                                                                                                        system.shopRecruits[x].spdStat, 
                                                                                                                                        system.shopRecruits[x].head if system.shopRecruits[x].head != "Helmet LVL 0" else "None", 
                                                                                                                                        system.shopRecruits[x].hand if system.shopRecruits[x].hand != "Sword LVL 0" else "None", 
                                                                                                                                        system.shopRecruits[x].body if system.shopRecruits[x].body != "Armor LVL 0" else "None",
                                                                                                                                        system.shopRecruits[x].feet if system.shopRecruits[x].feet != "Boots LVL 0" else "None"))
  
  print()

def displayExplorationBonus(system):
  print('''>> You have received a bonus of {0} Gold and {1} XP for revealing all important rooms.
'''.format(system.currentFloor*10, system.currentFloor*100))

def displayGameCompleteScreen():
  print('''[====================]
 | Congratulations! | 
[====================]
        
>> You have defeated The Dungeon Lord and lived to tell the tale!
>> Countless adventurers have been motivated by your success!
>> Your party has been ranked up to an S-Class adventure party!
>> Stories of your success will be known for generations to come!
''')