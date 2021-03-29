import requests
city = "london"
# this will provide a sample data of the city used in the variable 
urlx = "https://samples.openweathermap.org/data/2.5/weather?q="+city+"&appid=b6907d289e10d714a6e88b30761fae22"
# Send the request to the URL using GET method
req = requests.get(url = urlx)
output = req.json()

# Parse the valuable information from the returned JSON 

print("Raw JSON \n")
print(output)
print("\n")
#fetch output and print latitude and longitude information

city_longitude = output['coord']['lon']
city_latitude = output['coord']['lat']
print("The longitude for " + city + " is: " +str(city_longitude) + " , " + "and it's latitude is: " + str(city_latitude))