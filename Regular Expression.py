import re

sample_data = "From Jan 2020 till Nov 2021 I am learning python every weekend at 10:00AM"

# '\W+' represents Non-Alphanumeric characters or group of characters

print(re.split('\W+', sample_data))

# Extracting only the Month and Year from the string and print it

regex = re.compile('(?P<month>\w{3})\s+(?P<year>[0-9]{4})')
for m in regex.finditer(sample_data):
    value = m.groupdict()
    print("The Month is: "+ value['month']+" , " + " and the Year is: "+ value['year'])

# Extracting the time with AM or PM Addition

regex = re.compile('\d+:\d+\s[AP]M')
m = re.findall(regex, sample_data)


print(m)

