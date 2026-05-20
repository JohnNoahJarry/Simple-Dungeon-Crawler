import os

def clearScreen():
  os.system("cls||clear")

def displayUserInput():
  return input("<< ").replace(" ","").lower()

def displayUserInputContinue():
  return input("<< Press ENTER to continue!").replace(" ","").lower()

def displayRawUserInput():
  return input("<< ")

def displayHeader(system):
  print('''[==========================================]
 | Floor {0:<2} | Moves Left: {1:<3} | Gold: {2:<3} |
[==========================================]
'''.format(system.currentFloor, system.movesLeft, system.gold if system.gold < 1000 else "MAX"))
  
def displayPlayerPartyStats(system):
  output = ""
  for x in range(len(system.playerParty)):
    output += "[==============================] "
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " | {0:<18} LVL {1:<3} |  ".format(system.playerParty[x].name, system.playerParty[x].level if system.playerParty[x].level < 100 else "MAX")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " | HP: {0:<3}/{1:<3}    XP: {2:<3}/{3:<3} |  ".format(system.playerParty[x].currentHP if system.playerParty[x].currentHP < 1000 else "MAX", system.playerParty[x].maximumHP if system.playerParty[x].maximumHP < 1000 else "MAX", system.playerParty[x].currentXP, system.playerParty[x].level)
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " | ATK: {0:<3} DEF: {1:<3} SPD: {2:<3} |  ".format(system.playerParty[x].atkStat if system.playerParty[x].atkStat < 1000 else "MAX", system.playerParty[x].defStat if system.playerParty[x].defStat < 1000 else "MAX", system.playerParty[x].spdStat if system.playerParty[x].spdStat < 1000 else "MAX")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " |     Head: {0:<12}     |  ".format(system.playerParty[x].head if system.playerParty[x].head != "Helmet LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " |     Hand: {0:<11}      |  ".format(system.playerParty[x].hand if system.playerParty[x].hand != "Sword LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " |     Body: {0:<11}      |  ".format(system.playerParty[x].body if system.playerParty[x].body != "Armor LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += " |     Feet: {0:<11}      |  ".format(system.playerParty[x].feet if system.playerParty[x].feet != "Boots LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.playerParty)):
    output += "[==============================] "
  print(output)
  print()

def displayBackButton():
  print('''[B] = Back
''')