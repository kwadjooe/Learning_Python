

get_input = input("Do you want to store a new record (Y/N) ? ")

# Removing any extra spaces

get_input = get_input.strip()

# Convert all input to Lower Case

get_input = get_input.lower()

# Read the value and create a record

if ("y" in get_input):
    read_value_name = input("Enter your Name: ")
    read_value_age = input("Enter your Age: ")
    read_value_location = input("Enter your Location: ")
    read_value_language = input("Enter your Language: ")
    tmp_var = read_value_name+ ", "+read_value_age+", "+read_value_location+", "+read_value_language+ "\n"

# open a file myrecord.csv in write mode and write record and close it

    fopen = open("myrecord.csv", "w")
    fopen.write(tmp_var)
    fopen.close()

