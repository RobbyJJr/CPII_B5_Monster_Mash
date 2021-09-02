from creature import *
import re

print("Welcome to Monster Mash!")
# Game Settings
battlefield = []
numPlayers = ''

while re.search(r'^\d+$',numPlayers) == None:
  numPlayers = input('How many players are playing? (integers) ')
numPlayers = int(numPlayers)
 

# This is my line (Jeven)

                                    








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