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
game_images = [rock , paper, scissors]
print("RULES: Rock wins against Scissors while Scissors win against Paper and Paper wins against Rock.")
import random
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n "))
print(game_images[user_input])
comp_selection = random.randint(a= 0 , b= 2)
print(f"Computer Choose {comp_selection}")
print(game_images[comp_selection])
if user_input >= 3 or user_input < 0:
    print("You Type an Invalid Number You Lose!")
if user_input == 0 and comp_selection == 2:
    print("You Win")
elif comp_selection == 0 and user_input == 2:
    print("You Lose!")
elif comp_selection > user_input:
    print("You lose!")
elif user_input > comp_selection:
    print("You Win")
elif comp_selection == user_input:
    print("It's a draw")













