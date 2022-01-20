rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_choice == 0:
  print(rock)
elif player_choice == 1:
  print(paper)
elif player_choice == 2:
  print(scissors)
else:
  print("Invalid choice! Please make a selection of 0, 1 or 2.")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
  print(f"Computer chose: {rock}")
elif computer_choice == 1:
  print(f"Computer chose: {paper}")
else:
  print(f"Computer chose: {scissors}")

if player_choice == 0:
  if computer_choice == 0:
    print("It\'s a draw")
  elif computer_choice == 1:
    print("You lose")
  elif computer_choice == 2:
    print("You win")


if player_choice == 1:
  if computer_choice == 1:
    print("It\'s a draw")
  elif computer_choice == 2:
    print("You lose")
  elif computer_choice == 0:
    print("You win")


if player_choice == 2:
  if computer_choice == 2:
    print("It\'s a draw")
  elif computer_choice == 1:
    print("You win")
  elif computer_choice == 0:
    print("You lose")
