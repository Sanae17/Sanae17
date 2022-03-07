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

#Write your code below this line 👇
choice_list = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
user_choice_int = int(user_choice)

print(choice_list[user_choice_int])

computer_choice = random.randint(0,2)
print (f"Computer chose: \n{choice_list[computer_choice]}")

#Determine the winner
if choice_list[user_choice_int] == choice_list [computer_choice]:
  print("It's a draw.")
else:
  if choice_list[user_choice_int] == rock and choice_list[computer_choice] == paper:
    print("You lose")
  elif choice_list[user_choice_int] == rock and choice_list[computer_choice] == scissors:
    print("You win")
  elif choice_list[user_choice_int] == paper and choice_list[computer_choice] == rock:
    print("You win")
  elif choice_list[user_choice_int] == paper and choice_list[computer_choice] == scissors:
    print("You lose")
  elif choice_list[user_choice_int] == scissors and choice_list[computer_choice] == rock:
    print("You lose")
  elif choice_list[user_choice_int] == scissors and choice_list[computer_choice] == paper:
    print("You win")