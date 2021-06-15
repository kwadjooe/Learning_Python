

# a = {
#     "name": "Albert Einstein",
#     "birthday": "03/14/1879"
# }

# b = {
#     "name": "Benjamin Franklin",
#     "birthday": "01/17/1706"
# }


# c = {
#     "name": "Ada Lovelace",
#     "birthday": "12/10/1815"
# }

print("\n")

if __name__ == '__main__':

    birthdays = {
        "Albert Einstein":"03/14/1879",
        "Benjamin Franklin" :"01/17/1706",
        "Ada Lovelace" :"12/10/1815",
        "Donald Trump":"06/14/1946",
        "Rowan Atkinson":"01/6/1955",
        "K Ed.":"07/24/1798"
    }


    print("Welcome to the birthday dictionary. We know the birthdays of: \n")
    for name in birthdays:
        print(name)

name = input("Who's birthday do you want to look up? \n")
if name in birthdays:
    print("{}\'s birthday is {}.".format(name, birthdays[name]))
else:
    print("Sadly, we don\'t have {}\'s birthday.".format(name), '\n')

print("Thank you for playing with us!")
