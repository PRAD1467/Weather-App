import requests
import json
import os
city = input("Enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=b2bb1e2a47ea448197f140159230106&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
r = (wdic['location']['region'])
c = (wdic['location']['country'])
la = (wdic['location']['lat'])
lo = (wdic['location']['lon'])
lt = (wdic['location']['localtime'])
w_c = (wdic['current']['temp_c'])
w_f = (wdic['current']['temp_f'])
l_u= (wdic['current']['last_updated'])
print(f"The name of region and country are {r} & {c}")
print(f"The latitudes and longitudes are  {la} & {lo}")
print(f"The local time is  {lt}")
print(f"Current temperature of {city} is: {w_c} in Celsius")
print(f"Current temperature of {city} is: {w_f} in Farenheit")
print(f"Last Updated of data is: {l_u}")


