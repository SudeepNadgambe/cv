import random

print("Welcome to the Number Guessing Game\nI am thinking of a number between 1 and 100")
guessed_number=random.randint(1,100)
print(guessed_number)
level=input("Type 'e' for easy level\nType 'h' for hard level\n")
if level == 'e':
    chances = 10
elif level == 'h':
    chances = 5
else:
    print("Invalid input")
end = False
while not end:
    print(f"You have {chances} live left")
    user_guess=int(input("Make a guess"))
    if user_guess==guessed_number:
        print("You won")
        end = True
    else:
        chances-=1
        if user_guess > guessed_number:
            print("Too high")
        elif user_guess < guessed_number:
            print("Too low")
    if chances==0:
        print("Your lives ended \nYou lose")
        end = True




