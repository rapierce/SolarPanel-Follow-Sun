from datetime import date
from datetime import datetime
import astral
from astral import Astral
import time

# Retrieves and returns current time
def get_Current_Time():
    curr_Time = datetime.now()
    return curr_Time
a = Astral()
city_Name = 'Cleveland'
curr_Date = date.today()
curr_Time = get_Current_Time()
# loc = astral.Location(('Thompson, Ohio', 'USA', 41.67, -81.05, 'EST'))
sun_Time = astral.Astral()
city = a[city_Name]
sun = city.sun(local=True)

print (sun)
riser = sun.get('sunrise')
nooner = sun.get('noon')
solar_Sunrise = str(sun['sunrise'])
solar_Noon = str(sun['noon'])
calc = nooner - riser

# parsed_Noon = datetime.strptime(formatted_Noon, '%I%M%S')
# calc_Sunrise_Noon = solar_Noon - solar_Sunrise
print (solar_Sunrise)
print (solar_Noon)
# print (ext_Solar_Noon)
# print (calc_Sunrise_Noon)

''' event_Noon = sun_Time.solar_noon_utc(curr_Time, 41.67 -81.05)
print (curr_Time)
print (event_Noon) '''

# print (loc)
# for event, time in loc.sun(date.today()).items():
# print(event, 'at', time)
print (curr_Time)
print (curr_Date)
print (riser)
print (nooner)
print (calc)