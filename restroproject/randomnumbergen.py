import random 
num=random.randint(1,10)
print(num)

import random 
num= random.randint(1,100)
print("secret number generated!")
user_guess=int(input("enter your guessing num (1,100):"))
if user_guess > num:
    print("Too High!")
elif user_guess < num:
    print("Too Low!")
else:
    print("correct! you guessed it......")


import random
secret_num=random.randint(1,100)
attempt = 0
while True:
    try:
        guess=int(input("enter the guess number(1-100):"))
        
    except ValueError:
        print("enter valid number (1-100):")
        continue
    
    if guess < 1 or guess > 100:
        print("please enter numbers between (1-100)")
        continue

    attempt += 1
    
    if guess > secret_num:
        print("TOO HIGH !")
    elif guess < secret_num:
        print("TOO LOW !")
    else:
        print(f"CORRECT GUESS in {attempt} attempts.......!")
        break 