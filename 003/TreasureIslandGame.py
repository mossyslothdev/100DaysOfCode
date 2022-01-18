print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# The player is choosing which path to take on the crossroad
crossroad_choice = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

# If the left path is choosen then they eventually come across a lake
if crossroad_choice == "left":
  
  # Now the player is choosing whether they want to wait for a boat or attempt to swim across
  lake_choice = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  
  # If the player chooses to wait for a boat, they reach the island in the middle of the lake with a house on it
  if lake_choice == "wait":
    
    # Now the player has to choose which door to enter to complete the game
    door_choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
    
    # If the red door is choosen then the game is over
    if door_choice == "red":
      print("You are unable to resist the voices on the other side. Game Over.")
    
    # If the blue door is choosen the game is over
    elif door_choice == "blue":
      print("You are unable to resist the pull of the void. Game Over.")
    
    # Finally, if the yellow door is choosen then the player wins
    elif door_choice == "yellow":
      print("You found the artifact! You win!")
    
    # This is a catch all for the player choosing a door that doesn't exist and results in a game over
    else:
      print("You choose a door a door that doesn't exist and are met with the gaze of The Architects. Game Over.")
  
  # If the player chooses to swim across the lake then the game is over
  elif lake_choice == "swim":
    print("You are unable to resist the siren's call. Game Over.")
  
  # Another catch all if the player chooses an invalid option, resulting in a game over
  else:
    print("You are unable to resist the siren's call. Game Over.")

# If the player chooses the right crossroad path then the game is over
elif crossroad_choice == "right":
  print("You fall into a swirling abyss, becoming lost to time and are never seen again. Game Over.")

# One last catch all if the player chooses an invalid option during the crossroads section of the game and this also results in a game over
else:
  print("You fall into a swirling abyss, becoming lost to time and are never seen again. Game Over.")
