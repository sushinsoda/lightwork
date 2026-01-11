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
#print(rock)

import random
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice == 0:
    print(rock)
elif your_choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if your_choice >=3 or your_choice <0:
    print("You typed an invalid number. Try again")
elif your_choice == computer_choice:
    print("Draw!")
elif your_choice == 0 and computer_choice ==2:
    print("You win!")
elif computer_choice==0 and your_choice==2:
    print("You lose")
elif computer_choice > your_choice:
    print("You Lose!")
else:
    print("You win!")
