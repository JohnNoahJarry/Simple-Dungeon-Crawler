import random
import ui.battle, ui.general

def main(system):
  system.allUnitsInBattle = []
  for x in range(len(system.playerParty)):
    system.allUnitsInBattle.append(system.playerParty[x])
  
  for x in range(len(system.enemyParty)):
    system.allUnitsInBattle.append(system.enemyParty[x])
  
  system.allUnitsInBattle = sorted(system.allUnitsInBattle, key=lambda y:y.spdStat, reverse=True)

  isFirstRound = True
  while True:
    isAllPlayersDefeated = True
    for x in range(len(system.playerParty)):
      if system.playerParty[x].status != "Defeated":
        isAllPlayersDefeated = False
    
    if isAllPlayersDefeated:
      ui.general.clearScreen()
      ui.general.displayHeader(system)
      ui.battle.displayEnemyStats(system)
      ui.general.displayPlayerPartyStats(system)
      ui.battle.displayGameOverScreen()
      ui.general.displayUserInputContinue()
      return
    
    isAllPlayersFled = True
    for x in range(len(system.playerParty)):
      if system.playerParty[x].status not in ["Fled", "Defeated"]:
        isAllPlayersFled = False
    
    if isAllPlayersFled:
      ui.general.clearScreen()
      ui.general.displayHeader(system)
      ui.battle.displayEnemyStats(system)
      ui.general.displayPlayerPartyStats(system)
      ui.battle.displayFleeScreen()
      ui.general.displayUserInputContinue()

      return
    
    isAllEnemiesDefeated = True
    for x in range(len(system.enemyParty)):
      if system.enemyParty[x].status != "Defeated":
        isAllEnemiesDefeated = False
    
    if isAllEnemiesDefeated:
      ui.general.clearScreen()
      ui.general.displayHeader(system)
      ui.battle.displayEnemyStats(system)
      ui.general.displayPlayerPartyStats(system)
      ui.battle.displayWinScreen(system)
      ui.general.displayUserInputContinue()

      system.gold += system.currentFloor*len(system.enemyParty)
      if system.gold > 1000:
        system.gold = 1000

      for x in range(len(system.playerParty)):
        if system.playerParty[x].status != "Fled":
          system.playerParty[x].gainXP(system.currentFloor*10*len(system.enemyParty))
      
      return

    currentPlayer = 0
    while currentPlayer < len(system.playerParty):
      if system.playerParty[currentPlayer].status in ["Defeated", "Fled"]:
        currentPlayer += 1
        continue

      ui.general.clearScreen()
      ui.general.displayHeader(system)
      ui.battle.displayEnemyStats(system)
      ui.general.displayPlayerPartyStats(system)
      
      if isFirstRound:
        ui.battle.displayIntro(system)
        ui.general.displayUserInputContinue()
        isFirstRound = False
        continue
      else:
        ui.battle.displayActions(system, currentPlayer)
        ui.general.displayBackButton()
        actionChoice = ui.general.displayUserInput()

        if actionChoice == "1":
          while True:
            ui.general.clearScreen()
            ui.general.displayHeader(system)
            ui.battle.displayEnemyStats(system)
            ui.general.displayPlayerPartyStats(system)
            ui.battle.displayTargets(system, currentPlayer)
            ui.general.displayBackButton()
            targetChoice = ui.general.displayUserInput()

            if targetChoice in ["1", "2", "3"]:
              if int(targetChoice) <= len(system.enemyParty) and system.enemyParty[int(targetChoice)-1].status != "Defeated":
                system.playerParty[currentPlayer].status = "Attacking"
                system.playerParty[currentPlayer].target = system.enemyParty[int(targetChoice)-1]
                currentPlayer += 1
                break
            elif targetChoice == "b":
              currentPlayer = 0
              break
        elif actionChoice == "2":
          system.playerParty[currentPlayer].status = "Fleeing"
          while True:
            system.playerParty[currentPlayer].target = random.choice(system.enemyParty)

            if system.playerParty[currentPlayer].target.status not in ["Defeated", "Fled"]:
              break
          currentPlayer += 1
        elif actionChoice == "b":
          currentPlayer = 0
          continue
    
    for x in range(len(system.enemyParty)):
      while True:
        system.enemyParty[x].target = random.choice(system.playerParty)

        if system.enemyParty[x].target.status not in ["Defeated", "Fled"]:
          break
    
    for x in range(len(system.allUnitsInBattle)):
      if system.allUnitsInBattle[x].status == "Defeated" or system.allUnitsInBattle[x].target.status == "Defeated" or system.allUnitsInBattle[x].status == "Fled" or system.allUnitsInBattle[x].target.status == "Fled":
        if system.allUnitsInBattle[x].target.status == "Defeated" and system.allUnitsInBattle[x].status not in ["Defeated", "Fled"]:
          ui.general.clearScreen()
          ui.general.displayHeader(system)
          ui.battle.displayEnemyStats(system)
          ui.general.displayPlayerPartyStats(system)      
          ui.battle.displayDefeatedAlready(system, x)
          ui.general.displayUserInputContinue()
        elif system.allUnitsInBattle[x].target.status == "Fled" and system.allUnitsInBattle[x].status not in ["Defeated", "Fled"]:
          ui.general.clearScreen()
          ui.general.displayHeader(system)
          ui.battle.displayEnemyStats(system)
          ui.general.displayPlayerPartyStats(system)      
          ui.battle.displayFledAlready(system, x)
          ui.general.displayUserInputContinue()
        continue

      if system.allUnitsInBattle[x].unitType == "Enemy":
        system.allUnitsInBattle[x].status = "Attacking"
      
      evasionStatus = "Fled"
      critStatus = 0
      totalDamage = 0
      if system.allUnitsInBattle[x].status == "Attacking":
        evasionStatus, critStatus, totalDamage = system.allUnitsInBattle[x].performAttack()
      elif system.allUnitsInBattle[x].status == "Fleeing":
        evasionStatus = system.allUnitsInBattle[x].performFlee(system)
      
      ui.general.clearScreen()
      ui.general.displayHeader(system)
      ui.battle.displayEnemyStats(system)
      ui.general.displayPlayerPartyStats(system)      
      ui.battle.displayAttackStatus(system, x, evasionStatus, critStatus, totalDamage)
      ui.general.displayUserInputContinue()

      if system.allUnitsInBattle[x].target.status == "Defeated":
        system.allUnitsInBattle[x].target.name = "[DEFEATED]"
      elif system.allUnitsInBattle[x].status == "Fled":
        system.allUnitsInBattle[x].name = "[FLED]"