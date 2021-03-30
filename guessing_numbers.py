name = input("Please enter your name: ")
print("Please guess a number {0}".format(name))
guess = int(input())
if guess < 5:
    print("Please guess higher")
    guess = int(input())
    if guess == 5:
        print("Well done, {0}. You guessed it ".format(name))
    else:
        print("Sorry, {0} you have not guessed correctly.".format(name))
print("This game has ended. Please try again later")

