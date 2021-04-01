import random
Chances = 0


def RandomNumberGenerator():
    # Randomly generated number using random module
    return random.randint(1, 9)


print("Guess the random number and if you guess correct then you win")

# Storing the random number inside a variable
RandomNumber = RandomNumberGenerator()
# print(RandomNumber)
UserInput = int(input("Please Enter your Guess"))

# Checking if the entered text is correct or not
if(RandomNumber == UserInput):
    print("You won")

else:
    print("Sorry You lose")
    Chances = Chances + 1

    if(UserInput < RandomNumber):
        print("Hint: Sorry the number you entered is too short")
    elif(UserInput > RandomNumber):
        print("Hint: Sorry the number you entered is too big")

# Number of chances is 5 then the user lose
    while Chances > 5:
        print("Sorry you have lost all of your chances")
        break
