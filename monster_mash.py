from creature import *
import re
import random

print("Welcome to Monster Mash!")
# Game Settings
battlefield = []
numPlayers = ''
charClass = ['Elf','Fairy','Orc']

# Validation Loop for number of players
while re.search(r'^\d+$',numPlayers) == None:
  numPlayers = input('How many players are playing? (integers) ')
numPlayers = int(numPlayers)

# Set up the players
# Loop to set up the characters
for i in range(numPlayers):
  # What character type?
  choice = ''
  while choice not in list(enumerate(charClass)):
    choice = ''
    for i,cClass in enumerate(charClass):
      print(f'{i}: {cClass}')
    while not choice.isnumeric():
      choice = input('Choose a character from the list above: ')
    choice = int(choice)
    break 
  # Ask for the name?
  name = input(f'What is your {charClass[choice]}\'s name? ')
  # Random stats for simplicity ToDo
  # Create the character
  temp_char = eval(charClass[choice])(name)
  battlefield.append(temp_char)

battlefield[0].attack(battlefield[1])
# get push
  

"""                                    
# Max W
# Change the obj in the 'target' variable depending on what the objects are called obj1 = Orc(...) or char1 = Orc(...).

obj1 = Orc(1,1,1)

obj2 = Fairy(2,2,2,2)

obj3 = Elf(3,3,3,3)

all_characters = []
for i in range(3):  # change 3 to numPlayers
    m = str(i + 1)
    target = f"obj{m}.damage" # what should be the identifying factor?
    target_name = eval(target)
    all_characters.append(target_name)

print(all_characters)
"""
