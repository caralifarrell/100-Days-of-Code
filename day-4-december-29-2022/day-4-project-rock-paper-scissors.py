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

#Write your code below this line 👇

import random

user_choice = int(
    input(
        'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'
    ))

if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

if computer_choice >= 3:
  print("")
elif computer_choice == 0:
    print(f"Computer chose:\n{rock}")
elif computer_choice == 1:
    print(f"Computer chose:\n{paper}")
elif computer_choice == 2:
    print(f"Computer chose:\n{scissors}")

if user_choice == computer_choice:
  print("It's a tie. Nobody wins.")
elif user_choice == 0:
  if computer_choice == 1:
    print("Rock gets covered by paper. You lose.")
  elif computer_choice == 2:
    print("Rock crushes scissors. You win.")
elif user_choice == 1:
  if computer_choice == 0:
    print("Paper covers rock. You win.")
  elif computer_choice == 2:
    print("Paper gets cut by scissors. You lose.")
elif user_choice == 2:
  if computer_choice == 0:
    print("Scissors, gets crushed by rock. You lose.")
  elif computer_choice == 1:
    print("Scissors cuts paper. You win.")
