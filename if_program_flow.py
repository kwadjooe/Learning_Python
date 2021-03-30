name = input("Please enter your name: ")
age = int(input("How old are you, {0} ? ".format(name)))

# Making decision base on the age 

if (age >= 18):
    print("Congratulation! {0}, you are old enough to vote".format(name))
    print("Did you register to vote? it's important!")
else:
    print("Sorry! {0}, Please wait until you turn 18 to register to vote. ".format(name))
    print("Friendly reminder: you can register to vote in {0} years".format(18 - age))

