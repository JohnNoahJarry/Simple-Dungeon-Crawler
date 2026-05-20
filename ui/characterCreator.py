def displayNameScreen():
  print('''[=====================]
 | Character Creator |
[=====================]

>> Before we dive into the dungeon, let's give a name to your first party member.
>> Please Enter a name thats not longer than 18 characters.
>> You can also enter nothing for a randomized name.
''')
  
def displayNameFollowUpScreen(name):
  print('''[=====================]
 | Character Creator |
[=====================]

>> The name "{0}" has been chosen.
>> Is this name okay?

[1] = Yes
[2] = No
'''.format(name))

def displayStatGrowthScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth, pointsRemaining):
  print('''[=====================]
 | Character Creator |
[=====================]
        
>> Next, let's assign bonus points to {0}'s stat growth.

>> +{1} HP per level
>> +{2} ATK per level
>> +{3} DEF per level
>> +{4} SPD per level

>> You have {5} points remaining.
>> Choose where to assign them.

[1] = HP
[2] = ATK
[3] = DEF
[4] = SPD
'''.format(name, hpGrowth, atkGrowth, defGrowth, spdGrowth, pointsRemaining))

def displayStatGrowthFollowUpScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth):
  print('''[=====================]
 | Character Creator |
[=====================]

>> So, {0}'s stat growth is as follows:

>> +{1} HP per level
>> +{2} ATK per level
>> +{3} DEF per level
>> +{4} SPD per level

>> Is this stat growth okay?

[1] = Yes
[2] = No
'''.format(name, hpGrowth, atkGrowth, defGrowth, spdGrowth))
  
def displayConfirmationScreen(name, hpGrowth, atkGrowth, defGrowth, spdGrowth):
  print('''[=====================]
 | Character Creator |
[=====================]

>> So, your first party member's name is {0}.
>> And has a stat growth of:

>> +{1} HP per level
>> +{2} ATK per level
>> +{3} DEF per level
>> +{4} SPD per level

>> Is this party member okay?
>> If you say "No", the character creator process will start over from the beginning.

[1] = Yes
[2] = No        
'''.format(name, hpGrowth, atkGrowth, defGrowth, spdGrowth))