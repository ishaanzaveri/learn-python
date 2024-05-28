import random
guess = input("Pick a number ")
num = random.randint(1,9)
while(guess != "exit"):
    if int(guess) == num:
        print("You guessed correct")
        break
    elif int(guess) < num:
        print("Pick a higher number")
    else:
        print("Pick a lower number")
    guess = input("Pick a number ")