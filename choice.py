my_dict = {
    "Student": "Study hard and do all your school work on time! ",
    "Parent": "Please take goog care of your child! ",
    "Staff": "Please respect your work place policy and do your work! "

}
get_choice = input("Enter your Profile type (Student/Parent/Staff): ")

if (get_choice == "Student"):
    print(my_dict.get("Student"))
 if (get_choice == "Parent"):
    print(my_dict.get("Parent"))
 if (get_choice == "Staff"):
    print(my_dict.get("Staff"))


