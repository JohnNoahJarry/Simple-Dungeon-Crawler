def displayEnemyStats(system):
  output = ""
  for x in range(len(system.enemyParty)):
    output += "[==============================] "
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " | {0:<18} LVL {1:<3} |  ".format(system.enemyParty[x].name, system.enemyParty[x].level if system.enemyParty[x].level < 100 else "MAX")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " | HP: {0:<3}/{1:<3}    XP: {2:<3}/{3:<3} |  ".format(system.enemyParty[x].currentHP if system.enemyParty[x].currentHP < 1000 else "MAX", system.enemyParty[x].maximumHP if system.enemyParty[x].maximumHP < 1000 else "MAX", system.enemyParty[x].currentXP, system.enemyParty[x].level)
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " | ATK: {0:<3} DEF: {1:<3} SPD: {2:<3} |  ".format(system.enemyParty[x].atkStat if system.enemyParty[x].atkStat < 1000 else "MAX", system.enemyParty[x].defStat if system.enemyParty[x].defStat < 1000 else "MAX", system.enemyParty[x].spdStat if system.enemyParty[x].spdStat < 1000 else "MAX")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " |     Head: {0:<12}     |  ".format(system.enemyParty[x].head if system.enemyParty[x].head != "Helmet LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " |     Hand: {0:<11}      |  ".format(system.enemyParty[x].hand if system.enemyParty[x].hand != "Sword LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " |     Body: {0:<11}      |  ".format(system.enemyParty[x].body if system.enemyParty[x].body != "Armor LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += " |     Feet: {0:<11}      |  ".format(system.enemyParty[x].feet if system.enemyParty[x].feet != "Boots LVL 0" else "None")
  print(output)

  output = ""
  for x in range(len(system.enemyParty)):
    output += "[==============================] "
  print(output)
  print()

def displayIntro(system):
  if system.enemyParty[0].name == "The Dungeon Lord":
    print('''>> This is it. The final boss.
''')
  else:
    print('''>> A random encounter. It's time to fight.
''')

def displayActions(system, currentPlayer):
  print('''>> You are now selecting an action for {0}.
>> What will {0} do?

[1] = Attack
[2] = Flee ({1:.2f}%)
'''.format(system.playerParty[currentPlayer].name, system.playerParty[currentPlayer].getFleeChance(system.enemyParty)))
  
def displayTargets(system, currentPlayer):
  print('''>> You are now selecting a target for {0}.
>> Who will {0} target?
'''.format(system.playerParty[currentPlayer].name))
  
  for x in range(len(system.enemyParty)):
    if system.enemyParty[x].status != "Defeated":
      print("[{0}] {1}".format(x+1, system.enemyParty[x].name))
  
  print()

def displayAttackStatus(system, currentUnit, evasionStatus, critStatus, totalDamage):
  if evasionStatus == "Evaded":
    print(">> {0} attacks {1}, but {1} evaded the attack.".format(system.allUnitsInBattle[currentUnit].name, system.allUnitsInBattle[currentUnit].target.name))
  elif evasionStatus == "Fled":
    print(">> {0} has successfully fled the battle.".format(system.allUnitsInBattle[currentUnit].name))
  elif evasionStatus ==  "Failed to Flee":
    print(">> {0} attempted to flee, but failed.".format(system.allUnitsInBattle[currentUnit].name))
  else:
    if critStatus == "Crit":
      print(">> {0} CRITICALLY attacks {1} for {2} damage.".format(system.allUnitsInBattle[currentUnit].name, system.allUnitsInBattle[currentUnit].target.name, totalDamage))
    elif critStatus == "No Crit":
      print(">> {0} attacks {1} for {2} damage.".format(system.allUnitsInBattle[currentUnit].name, system.allUnitsInBattle[currentUnit].target.name, totalDamage))
  
  print()

def displayGameOverScreen():
  print('''>> Your party has been wiped out. Game Over.
''')
  
def displayWinScreen(system):
  print('''>> You have won the battle.
>> You've earned {0} Gold and {1} XP.
'''.format(system.currentFloor*len(system.enemyParty), system.currentFloor*10*len(system.enemyParty)))

def displayFleeScreen():
  print('''>> Your party has fled the battle.
''')
  
def displayDefeatedAlready(system, currentUnit):
  print('''>> {0} was looking to attack {1}, but {1} has already been defeated.
'''.format(system.allUnitsInBattle[currentUnit].name, system.allUnitsInBattle[currentUnit].target.originalName))

def displayFledAlready(system, currentUnit):
  print('''>> {0} was looking to attack {1}, but {1} has already fled the battle.
'''.format(system.allUnitsInBattle[currentUnit].name, system.allUnitsInBattle[currentUnit].target.originalName))
