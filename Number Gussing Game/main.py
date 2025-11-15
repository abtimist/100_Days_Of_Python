from art import logo
import random
print(logo+"\n\n\n")
ATTEMPTS_LEFT=0
def guess_number(ATTEMPTS_LEFT):
    random_number=random.randint(0,100)
    while ATTEMPTS_LEFT!=0:
        print(f"You have {ATTEMPTS_LEFT} attempts remaining to guess the number.")
        guess=int(input("Guess a number between 1 and 100: "))
        if guess==random_number:
            print("OMG!!, You Guessed it.")
            break
        elif guess<random_number:
            ATTEMPTS_LEFT -= 1
            print("Too Low")
        else:
            ATTEMPTS_LEFT -= 1
            print("Too High")
        if ATTEMPTS_LEFT==0:
            print(f"You've run out of guesses :(, The number was {random_number}")












while True:
    difficulty=input("What difficulty do you want? easy or hard?(type it): ").lower()
    if difficulty=="easy":
        ATTEMPTS_LEFT=10
    else:
        ATTEMPTS_LEFT=5
    guess_number(ATTEMPTS_LEFT)
    status = input("Do you want to play another game? y/n: ").lower()
    if status=="y":
        continue
    else:
        break