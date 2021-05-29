# working with GIT 
# git config --global user.name "Krystof Edouwossi"
# git config --global user.email "kwadjooe@gmail.com"
# git init 
# git add *.*
# git status
# git commit -m "Initial commit"
# git log 
# git log --oneline
# git log --online -n 3
# git checkout hash_number identify [Detach from the master branch]
# git checkout master [Attach to the master branch]
# git commit --amend  [Replace previous commit]


import datetime

fname = input("what is your First name? \n") 
lname = input("What is  your Last name? \n")
# 
initial_birthday = input("What is your Birthday? (in DD/MM/YYYY) ")
ibirthdate = datetime.datetime.strptime(initial_birthday,"%d/%m/%Y").date() 
year_of_birth = ibirthdate.year 
month_of_birth = ibirthdate.month
day_of_birth = ibirthdate.day
next_birthday = input("When is your next Birthday Date? (in DD/MM/YYYY) ")  
nbirthdate = datetime.datetime.strptime(next_birthday,"%d/%m/%Y").date()  
todays_date = datetime.date.today();  
todays_year = todays_date.year
days = nbirthdate - todays_date;  
days_before_birthday = days.days

print("Your Birthday is in {0} Days. Please Enjoy !!! ".format(days_before_birthday)); 

print(todays_date.strftime('Please Join My Birthday party on %A, %d-%B-%Y'))  

age = todays_year - year_of_birth

print("Well {0}, You are {1} years old".format(fname,age))

# to get today's date
# todays_date = date.today()
# extract current year from today's date

current_year = todays_date.year

your_age = current_year - age

print("Awesome! {0}, you were born in {1}".format(fname, your_age))

if age >= 18:
    print("Great! {0}, you can vote this year".format(fname))
else:
    print("Sorry! {0}, You are not old enough to vote yet".format(fname))
