import random
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


game_icons = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))


computer_choice = random.randint(0, 2)
print(game_icons[user_input])
print(f"Computer choose: {game_icons[computer_choice]}")


if user_input == computer_choice:
    print("It's a draw!")
elif user_input == 0 and computer_choice == 1:
    print("You win!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif user_input == 1 and computer_choice == 0:
    print("You lose")
elif user_input == 1 and computer_choice == 2:
    print("You win!")
elif user_input == 2 and computer_choice == 0:
    print("You lose!")
elif user_input == 2 and computer_choice == 1:
    print("You win!")
    