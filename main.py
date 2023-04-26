import random
num = random.randint(1,20)
print("Welcome to the Number Guessing Game!\n Can you guess the number I guess ?     ")
guess=int(input("Enter a number to start the game \n [Hint:It's between 1 to 20] : "))
while num!=guess:
    if guess>num:
        print("Sorry! Your Guess is High")
    else:
        print("Sorry! Your Guess is low")
    guess = int(input("You can Guess again: "))
print("Congraltulations !! \n  You won ")

