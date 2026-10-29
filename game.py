#Rcok, Paper, Scissors

import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
ties = 0

while True:
    computer = random.choice(choices)
    player = input("Enter rock, paper, scissors or exit: ")

    if player == "exit":
        print("==== FINAL SCORE ====")
        print(f"player: {player_score}")
        print(f"computer: {computer_score}")
        print(f"ties: {ties}")

        if player_score > computer_score:
            print("You are the champion!")
        elif computer_score > player_score:
            print("Computer is the champion!")
        else:
            print("The match is a draw!")

        print("Goodby!")
        break

    print("Computer choose:", computer)
    if player not in choices:
        print("Invalid choice!")
    else:
        print("computer choose:", computer)

        if player == computer:
            print("It's a tie!")
            ties += 1

        elif player == "rock" and computer == "scissors":
             print("you won!")
             player_score += 1

        elif player == "paper" and computer == "rock":
             print("you won!")
             player_score += 1

        elif player == "scissors" and computer == "paper":
            print("player won!")
            player_score += 1
              
        else:
            print("computer wins!")
            computer_score += 1

        print("\n==== SCOREBOARD ====")
        print(f"player: {player_score}")
        print(f"computer: {computer_score}")
        print(f"ties: {ties}")
        print("======================")