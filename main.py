import random

# diagrams
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

# add those to a list
game_images = [rock, paper, scissors]

# ask user for a choice of rock, paper and scissor
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print that diagram from list
print(game_images[user_choice])

# randomly allot computer a choice
computer_choice = random.randint(0, 2)
print("Computer chose:")
# print that diagram from list
print(game_images[computer_choice])

# if any number outside of 0, 1, 2 is chosen
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 

# if user chooses rock and computer chooses scissors
elif user_choice == 0 and computer_choice == 2:
  print("You win!")

# or if computer chooses rock and user chooses scissors
elif computer_choice == 0 and user_choice == 2:
  print("You lose")

# In the list, if you see paper beats rock, scissor beats paper , hence if the one's choice is greater than the other's they win
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
# if both players chose same component 
elif computer_choice == user_choice:
  print("It's a draw")
