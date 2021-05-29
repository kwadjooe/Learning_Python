kilometers = input("Please provide the distance in kilometer: \n")
kilometers = float(kilometers)

# kilometers = 12.25

miles = input("Please provide the distance in miles: \n")
miles = float(miles)
# miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
