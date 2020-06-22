import random;
player_wins = 0
computer_wins = 0
winning_score = 3


while player_wins < winning_score and computer_wins < winning_score:
    print("Welcome to RPS!")
    user_choice = input("Select your move: ")
    comp_choice = random.choice(['rock','paper','scissors'])
    if user_choice == "quit" or user_choice == "q":
        break
    if user_choice == comp_choice:
        print("PUSH")
    elif user_choice == "rock":
        if comp_choice == "scissors":
            print("Player wins!")
            player_wins += 1
        elif comp_choice == "paper":
            print("Computer wins")
            computer_wins += 1
    elif user_choice == "paper": 
        if comp_choice == "rock":
            print("Player wins")
            player_wins += 1
        elif comp_choice == "scissors":
            print("Computer Wins")
            computer_wins += 1
    elif user_choice == "scissors":
        if comp_choice == "rock":
            print("Player wins")
            player_wins += 1
        elif comp_choice == "paper":
            print("Computer wins")
            computer_wins += 1
    else:
        print("Something went wrong")

print(f"Final Score: Player: {player_wins} | Computer: {computer_wins}")