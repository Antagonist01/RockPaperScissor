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
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
# going to let the user choose a number
user_choice =  int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0 :
    print ("You typed an invalid  number")
    exit()  # Stops execution if input is invalid
else :
    print (game_images[user_choice])

random_choice = random.randint(0, 2)
#print(f"The Computer chose {random_choice}")
print ("Computer Chose: ")
print(game_images[random_choice])


if (user_choice == 0 and random_choice == 2) or \
        (user_choice == 1 and random_choice == 0) or \
        (user_choice == 2 and random_choice == 1):
    print("You win!")
elif user_choice == random_choice:
    print("It's a draw")
else:
    print("You lose!")
