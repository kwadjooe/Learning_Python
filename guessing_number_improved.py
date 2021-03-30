name = input("Please enter your name: ")
print("{0}, Please guess a number between 0 and 10: ".format(name))
guess = int(input())
if guess != 5:
    if guess < 5 :
        print("Please guess higher")
    else:
        print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, {0}. You guessed it ".format(name))
    else:
        print("Sorry, {0} you have not guessed correctly.".format(name))

else:
    print("Great job! {0}, you got it first time".format(name))
    
print("This game has ended. Please try again later")
