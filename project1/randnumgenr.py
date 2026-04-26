import random
def game():
    secret_num=random.randint(1,100)
    attempt = 0
    max_attempt=5
    print("guess you number between 1 - 100")
    
    while attempt < max_attempt:
        try:
            guess=int(input("Guess the number:"))
        except ValueError:
            print("please enter valid number between 1-100")
            continue

        if guess < 1 or guess > 100:
            print("enter the number between 1 - 100")
            continue
        attempt += 1
        
        if guess > secret_num:
            print("TOO HIGH !")
        elif guess < secret_num:
            print("TOO LOW !")
        else:
            print(f"you have guessed it correct in {attempt} attempt !")
            return
    
    print(f"you are out of attempts! the number was {secret_num}!")
while True:
    game()
    play_again= input("do you want to play again y/n:").lower()
    if play_again != "y":
        print("thankyou for playing!!")
        break

    
