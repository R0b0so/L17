import random
Choice = ["Rock","Paper","Scissors"]
user_choice = input("Choose Rock, Paper or Scissors")
computer_choice = random.choice(Choice)
print("You chose:", user_choice)
print("\n The computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie.")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock wins")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper wins")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors wins")
else:
    print("You lose")