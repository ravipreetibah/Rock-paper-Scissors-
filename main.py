import random

def get_choices():
    option = ["rock", "paper", "scissors"]
    while True:
        player_choice = input ("Enter a choice (rock, paper, scissors): ")
        if player_choice in option:
            break
        else:
            print("Invalid choice. Please enter either rock, paper, or scissors.")
    computer_choice = random.choice(option)
    choices = {"player": player_choice,"computer": computer_choice}
    return choices


def check_win(player, computer):
    print (f"You chose {player},  computer chose : {computer}")
    if player == computer:
        return "Its a boring tie!"
    elif player == "rock":
        if computer == "scissors":
            return "You win! rock breaks scissors!"
        else:
            return "Boo Hoo! sucks to be you!"
    elif player == "paper":
        if computer == "rock":
            return "You win! paper covers the rock!"
        else:
            return "Boo Hoo! sucks to be you!"
    elif player == "scissors":
        if computer == "paper":
            return "You win! scissor is cuts paper!"
        else:
            return "Boo Hoo! sucks to be you!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)





























