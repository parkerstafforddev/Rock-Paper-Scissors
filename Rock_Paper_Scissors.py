import random

options = ["Rock", "Paper", "Scissors"]

def play_game():
    computer_choice = random.choice(options)
    player_choice = input("Rock, Paper, Scissors? (Type 'I quit' to end game): ")
    if player_choice == "I quit":
        print("Thank you for playing")
        return
    if player_choice == computer_choice:
        print("Game Tied")
    elif player_choice == "Rock" and computer_choice == "Paper":
        print("You Lose")
    elif player_choice == "Scissors" and computer_choice == "Rock":
        print("You Lose")
    elif player_choice == "Paper" and computer_choice == "Scissors":
        print("You Lose")
    else:
        print("You Win")

print("Welcome to Rock, Paper, Scissors!")
while True:
    play_game()