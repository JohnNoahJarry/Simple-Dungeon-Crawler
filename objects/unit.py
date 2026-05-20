import random

class Unit:
  def __init__(self, unitType, name, level, hpGrowth, atkGrowth, defGrowth, spdGrowth):
    self.unitType = unitType
    self.status = "Okay"
    
    self.name = name
    self.originalName = name
    self.level = level

    self.hpGrowth = hpGrowth
    self.atkGrowth = atkGrowth
    self.defGrowth = defGrowth
    self.spdGrowth = spdGrowth

    self.currentHP = self.hpGrowth*self.level
    self.maximumHP = self.hpGrowth*self.level
    self.currentXP = 0
    self.atkStat = self.atkGrowth*self.level
    self.defStat = self.defGrowth*self.level
    self.spdStat = self.spdGrowth*self.level

    self.head = "Helmet LVL 0"
    self.hand = "Sword LVL 0"
    self.body = "Armor LVL 0"
    self.feet = "Boots LVL 0"

    self.target = None

  def equipItem(self, item):
    if item[0:6] == "Helmet":
      self.maximumHP -= 20*int(self.head[-1])
      self.maximumHP += 20*int(item[-1])
      self.head = item

      if self.currentHP > self.maximumHP:
        self.currentHP = self.maximumHP
    elif item[0:5] == "Sword":
      self.atkStat -= 20*int(self.hand[-1])
      self.atkStat += 20*int(item[-1])
      self.hand = item
    elif item[0:5] == "Armor":
      self.defStat -= 20*int(self.body[-1])
      self.defStat += 20*int(item[-1])
      self.body = item
    elif item[0:5] == "Boots":
      self.spdStat -= 20*int(self.feet[-1])
      self.spdStat += 20*int(item[-1])
      self.feet = item
  
  def gainXP(self, xp):
    if self.level < 100:
      for x in range(xp):
        if self.level == 100:
          return

        self.currentXP += 1
        if self.currentXP == self.level:
          self.levelUp()
  
  def levelUp(self):
    self.level += 1
    self.maximumHP += self.hpGrowth
    self.currentHP = self.maximumHP
    self.atkStat += self.atkGrowth
    self.defStat += self.defGrowth
    self.spdStat += self.spdGrowth

    self.currentXP = 0

  def getFleeChance(self, enemyParty):
    sumOfEnemySPDStats = 0
    for x in range(len(enemyParty)):
      sumOfEnemySPDStats += enemyParty[x].spdStat
    
    averageOfEnemySPDStats = sumOfEnemySPDStats / len(enemyParty)
    
    fleeChance = self.spdStat / averageOfEnemySPDStats

    return fleeChance*100
  
  def performAttack(self):
    evasionRNG = random.randint(1,100)
    if evasionRNG <= 5:
      return "Evaded", "No Crit", 0
    else:
      critBonus = 1
      critBonusRNG = random.randint(1,100)
      if critBonusRNG <= 5:
        critBonus = 2
      
      totalDamage = self.atkStat*critBonus - random.randint(0, self.target.defStat)
      if totalDamage < 1:
        totalDamage = 1
      
      self.target.currentHP -= totalDamage
      if self.target.currentHP < 1:
        self.target.currentHP = 0
        self.target.status = "Defeated"
      
      if critBonus == 2:
        return "Not Evaded", "Crit", totalDamage
      else:
        return "Not Evaded", "No Crit", totalDamage
  
  def performFlee(self, system):
    if random.randint(1,100) <= self.getFleeChance(system.enemyParty):
      self.status = "Fled"
      return "Fled"
    else:
      self.status = "Failed to Flee"
      return "Failed to Flee"