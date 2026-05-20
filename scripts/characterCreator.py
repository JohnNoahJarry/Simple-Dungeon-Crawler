import random
from pathlib import Path
import objects.unit, objects.system
import ui.characterCreator, ui.general

def main():
  name = ""
  hpGrowth = 5
  atkGrowth = 5
  defGrowth = 5
  spdGrowth = 5

  while True:
    while True:
      ui.general.clearScreen()
      ui.characterCreator.displayNameScreen()
      name = ui.general.displayRawUserInput()
      
      isNameOkay = False
      if len(name) < 19:
        if name == "":
          filepath = Path(__file__).parent / "../assets/Names"
          f = open(filepath, "r")

          names = []
          for line in f:
            names.append(line.strip())
            
          name = random.choice(names)
        
        while isNameOkay == False:
          ui.general.clearScreen()
          ui.characterCreator.displayNameFollowUpScreen(name)
          yorn = ui.general.displayUserInput()
          
          if yorn == "1":
            isNameOkay = True
          elif yorn == "2":
            break
      
      if isNameOkay:
        break
    
    while True:
      pointsRemaining = 4
      hpGrowth = 5
      atkGrowth = 5
      defGrowth = 5
      spdGrowth = 5
      
      while pointsRemaining != 0:
        ui.general.clearScreen()
        ui.characterCreator.displayStatGrowthScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth, pointsRemaining)
        choice = ui.general.displayUserInput()

        if choice == "1":
          hpGrowth += 1
          pointsRemaining -= 1
        elif choice == "2":
          atkGrowth += 1
          pointsRemaining -= 1
        elif choice == "3":
          defGrowth += 1
          pointsRemaining -= 1
        elif choice == "4":
          spdGrowth += 1
          pointsRemaining -= 1
      
      isStatGrowthOkay = False
      while isStatGrowthOkay == False:
        ui.general.clearScreen()
        ui.characterCreator.displayStatGrowthFollowUpScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth)
        yorn = ui.general.displayUserInput()

        if yorn == "1":
          isStatGrowthOkay = True
        elif yorn == "2":
          break
      
      if isStatGrowthOkay:
        break

    isEverythingOkay = False
    while isEverythingOkay == False:
      ui.general.clearScreen()
      ui.characterCreator.displayConfirmationScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth)
      yorn = ui.general.displayUserInput()

      if yorn == "1":
        isEverythingOkay = True
      elif yorn == "2":
        break
    
    if isEverythingOkay:
      break
  
  player = objects.unit.Unit("Player", name, 10, hpGrowth, atkGrowth, defGrowth, spdGrowth)
  system = objects.system.System(player)

  return system