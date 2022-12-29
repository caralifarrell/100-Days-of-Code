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

computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(rock)
    if computer_choice == 0:
      print(f"Computer chose:\n{rock}")
      print("It's a tie. Nobody wins.")
    elif computer_choice == 1:
      print(f"Computer chose:\n{paper}")
      print("Rock gets covered by paper. You lose.")
    elif computer_choice == 2:
      print(f"Computer chose:\n{scissors}")
      print("Rock crushes scissors. You win.")
elif user_choice == 1:
    print(paper)
    if computer_choice == 0:
      print(f"Computer chose:\n{rock}")
      print("Paper covers rock. You win.")
    elif computer_choice == 1:
      print(f"Computer chose:\n{paper}")
      print("It's a tie. Nobody wins.")
    elif computer_choice == 2:
      print(f"Computer chose:\n{scissors}")
      print("Paper gets cut by scissors. You lose.")
elif user_choice == 2:
    print(scissors)
    if computer_choice == 0:
      print(f"Computer chose:\n{rock}")
      print("Scissors gets crushed by rock. You lose.")
    elif computer_choice == 1:
      print(f"Computer chose:\n{paper}")
      print("Scissors cuts paper. You win.")
    elif computer_choice == 2:
      print(f"Computer chose:\n{scissors}")
      print("It's a tie. Nobody wins.")
else: 
  print("That is not a valid play. You lose.")
