import random
random_number = random.randint(1,10)
resp = None
while True:
    resp = int(input('Pick number 1-10: '))
    if resp > random_number:
        print("Too High")
    elif resp < random_number:
        print("Too low")
    else:
        print("You got it!")
        again = input("Play again? y/n: ")
        if again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thanks for playing")
            break