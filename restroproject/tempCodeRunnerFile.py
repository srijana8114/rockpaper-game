import random

def play_game():
    choice_game=["ROCK","PAPER","SCISSORS"]
    computer=random.choice(choice_game)

    print("please enter rock, paper or scissors")

    user =input("rock, paper or scissors:").upper()
    
    print(f"computer choose: {computer}")

    if user not in choice_game:
        print("Invaid Input")
        return None

    if user == computer:
        print("tie !!!")
        return "tie"

    elif user == "ROCK" and computer == "SCISSORS":
        print("you win!!")
        return "user"

    elif user == "SCISSORS" and computer == "PAPER":
        print("you win!!")
        return "user"

    elif user == "PAPER" and computer == "ROCK":
        print("you win!!")
        return "user"

    else:
        print("you lose!")
        return "computer"
while True:
    user_score = 0
    computer_score = 0
    while user_score < 2 and computer_score < 2:
        result = play_game()
        if result == "user":
            user_score +=1
        elif result == "computer":
            computer_score +=1
        else:
            continue
    
        print(f"score: you={user_score} | computer={computer_score}")

    print("Final Result:")
    if user_score == 2:
        print("you won the match !")
    else:
        print("computer won the match !")


    play_again=input("Do you want to play again? (y / n):").lower()
    if play_again != "y" :
        print("thankyou for playing!")
        break