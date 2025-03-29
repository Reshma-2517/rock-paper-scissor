import random

a = ["rock", "paper", "scissors"]
computer = random.choice(a)


your_choice = input("rock , paper or scissors ? : ").lower()


print(f"computer's choice is {computer}")

if your_choice == computer:
    print("Tie !")
elif your_choice == "rock" and computer  == "scissors":
    print("You win ")
elif your_choice == "scissors" and computer == "paper":
    print("You win")
elif your_choice == "paper" and computer == "rock":
    print("You win")
else:
    print("You lose !")
    









