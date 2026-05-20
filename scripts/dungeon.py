import random
import scripts.battle
import ui.dungeon, ui.general

def main(system):
  isUpdateSuccessful = False
  while True:
    isAllPlayersDefeated = True
    for x in range(len(system.playerParty)):
      if system.playerParty[x].status != "Defeated":
        isAllPlayersDefeated = False
    
    if isAllPlayersDefeated:
      return
    else:
      for x in range(len(system.playerParty)):
        currentPlayer = 0
        while currentPlayer < len(system.playerParty):
          if system.playerParty[currentPlayer].status == "Defeated":
            del system.playerParty[currentPlayer]
            continue

          system.playerParty[currentPlayer].status = "Okay"
          system.playerParty[currentPlayer].name = system.playerParty[currentPlayer].originalName
          currentPlayer += 1
    
    if system.movesLeft == 0 and system.currentFloor == 10:
      while system.enemyParty[0].status != "Defeated":
        scripts.battle.main(system)

        isAllPlayersDefeated = True
        for x in range(len(system.playerParty)):
          if system.playerParty[x].status != "Defeated":
            isAllPlayersDefeated = False
        
        if isAllPlayersDefeated:
          return
        else:
          for x in range(len(system.playerParty)):
            currentPlayer = 0
            while currentPlayer < len(system.playerParty):
              if system.playerParty[currentPlayer].status == "Defeated":
                del system.playerParty[currentPlayer]
                continue

              system.playerParty[currentPlayer].status = "Okay"
              system.playerParty[currentPlayer].name = system.playerParty[currentPlayer].originalName
              currentPlayer += 1

        if system.enemyParty[0].status == "Defeated":
          ui.general.clearScreen()
          ui.dungeon.displayGameCompleteScreen()
          ui.general.displayUserInputContinue()

          return

    ui.general.clearScreen()
    ui.general.displayHeader(system)
    ui.dungeon.displayMapScreen(system)
    ui.general.displayPlayerPartyStats(system)

    if system.currentMap[system.restAreaLocation] == "   " and system.currentMap[system.itemLocation] == "   " and system.currentMap[system.shopLocation] == "   " and system.currentMap[system.exitLocation] == "   ":
      if system.isExplorationBonusAvailable:
        ui.dungeon.displayExplorationBonus(system)
        ui.general.displayUserInputContinue()

        for x in range(len(system.playerParty)):
          system.playerParty[x].gainXP(system.currentFloor*100)
          
        system.gold += system.currentFloor*10
        if system.gold > 1000:
          system.gold = 1000

        system.isExplorationBonusAvailable = False
        continue
    
    if system.playerPartyCurrentLocation == system.exitLocation:
      ui.dungeon.displayExitScreen(system)
    elif system.playerPartyCurrentLocation == system.restAreaLocation:
      ui.dungeon.displayRestAreaScreen(system)
    elif system.playerPartyCurrentLocation == system.itemLocation:
      ui.dungeon.displayItemScreen(system)
    elif system.playerPartyCurrentLocation == system.shopLocation:
      ui.dungeon.displayShopScreen()
    else:
      if random.randint(1,100) < 11 and isUpdateSuccessful:
        system.createEnemyParty()
        scripts.battle.main(system)
        isUpdateSuccessful = False
        continue

    ui.dungeon.displayNavigation(system)
    choice = ui.general.displayUserInput()

    if choice in "wasd":
      isUpdateSuccessful = system.setPlayerPartyCurrentLocation(choice)
    elif system.playerPartyCurrentLocation == system.exitLocation:
      if choice == "1":
        if system.currentFloor != 10:
          system.createNewDungeonFloor()
        elif system.currentFloor == 10:
          system.createBoss()
          while system.enemyParty[0].status != "Defeated":
            scripts.battle.main(system)

            isAllPlayersDefeated = True
            for x in range(len(system.playerParty)):
              if system.playerParty[x].status != "Defeated":
                isAllPlayersDefeated = False
            
            if isAllPlayersDefeated:
              return
            else:
              for x in range(len(system.playerParty)):
                currentPlayer = 0
                while currentPlayer < len(system.playerParty):
                  if system.playerParty[currentPlayer].status == "Defeated":
                    del system.playerParty[currentPlayer]
                    continue

                  system.playerParty[currentPlayer].status = "Okay"
                  system.playerParty[currentPlayer].name = system.playerParty[currentPlayer].originalName
                  currentPlayer += 1

            if system.enemyParty[0].status == "Defeated":
              ui.general.clearScreen()
              ui.dungeon.displayGameCompleteScreen()
              ui.general.displayUserInputContinue()

              return
    elif system.playerPartyCurrentLocation == system.restAreaLocation:
      if choice == "1":
        if system.isRestAreaAlreadyUsed == False:
          system.healParty()
          system.isRestAreaAlreadyUsed = True
    elif system.playerPartyCurrentLocation == system.itemLocation:
      if choice in "123":
        if system.isItemAlreadyObtained == False:
          itemAssignScreen(choice, system)
    elif system.playerPartyCurrentLocation == system.shopLocation:
      if choice == "1":
        shopItemsScreen(system)
      elif choice == "2":
        shopRecruitsScreen(system)

def itemAssignScreen(itemChoice, system):
  while True:
    ui.general.clearScreen()
    ui.general.displayHeader(system)
    ui.dungeon.displayMapScreen(system)
    ui.general.displayPlayerPartyStats(system)
    ui.dungeon.displayItemAssignScreen(int(itemChoice)-1, system)
    ui.general.displayBackButton()
    ui.dungeon.displayNavigation(system)
    choice = ui.general.displayUserInput()

    if choice in "wasd":
      isUpdateSuccessful = system.setPlayerPartyCurrentLocation(choice)
      if isUpdateSuccessful:
        return
    elif choice in "123":
      if int(choice) <= len(system.playerParty):
        system.playerParty[int(choice)-1].equipItem(system.itemsInItemRoom[int(itemChoice)-1])
        system.isItemAlreadyObtained = True
        return
    elif choice == "b":
      return

def shopItemsScreen(system):
  while True:
    ui.general.clearScreen()
    ui.general.displayHeader(system)
    ui.dungeon.displayMapScreen(system)
    ui.general.displayPlayerPartyStats(system)
    ui.dungeon.displayShopItemsScreen(system)
    ui.general.displayBackButton()
    ui.dungeon.displayNavigation(system)
    itemChoice = ui.general.displayUserInput()

    if itemChoice in "wasd":
      isUpdateSuccessful = system.setPlayerPartyCurrentLocation(itemChoice)
      if isUpdateSuccessful:
        return
    elif itemChoice in "12345":
      if int(itemChoice) <= len(system.shopItems) and system.gold >= system.currentFloor*10:
        while True:
          ui.general.clearScreen()
          ui.general.displayHeader(system)
          ui.dungeon.displayMapScreen(system)
          ui.general.displayPlayerPartyStats(system)
          ui.dungeon.displayShopItemAssignScreen(int(itemChoice)-1, system)
          ui.general.displayBackButton()
          ui.dungeon.displayNavigation(system)
          playerChoice = ui.general.displayUserInput()

          if playerChoice in "wasd":
            isUpdateSuccessful = system.setPlayerPartyCurrentLocation(playerChoice)
            if isUpdateSuccessful:
              return
          elif playerChoice in "123":
            if int(playerChoice) <= len(system.playerParty):
              system.playerParty[int(playerChoice)-1].equipItem(system.shopItems[int(itemChoice)-1])
              del system.shopItems[int(itemChoice)-1]
              system.gold -= system.currentFloor*10
              return
          elif playerChoice == "b":
            return
    elif itemChoice == "b":
      return

def shopRecruitsScreen(system):
  while True:
    ui.general.clearScreen()
    ui.general.displayHeader(system)
    ui.dungeon.displayMapScreen(system)
    ui.general.displayPlayerPartyStats(system)
    ui.dungeon.displayShopRecruitsScreen(system)
    ui.general.displayBackButton()
    ui.dungeon.displayNavigation(system)
    recruitChoice = ui.general.displayUserInput()

    if recruitChoice in "wasd":
      isUpdateSuccessful = system.setPlayerPartyCurrentLocation(recruitChoice)
      if isUpdateSuccessful:
        return
    elif recruitChoice in "123":
      if int(recruitChoice) <= len(system.shopRecruits) and system.gold >= system.currentFloor*10 and len(system.playerParty) != 3:
        system.playerParty.append(system.shopRecruits[int(recruitChoice)-1])
        del system.shopRecruits[int(recruitChoice)-1]
        system.gold -= system.currentFloor*10
        return
    elif recruitChoice == "b":
      return