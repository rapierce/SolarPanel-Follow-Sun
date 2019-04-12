from datetime import date
from datetime import datetime
import astral


# Retrieves and returns current time
def get_Current_Time():
    curr_Time = datetime.now()
    return curr_Time

curr_Date = date.today()
curr_Time = get_Current_Time()
loc = astral.Location(('Thompson, Ohio', 'USA', 41.67, -81.05, 'EST'))
print (loc)
for event, time in loc.sun(date.today()).items():
    print(event, 'at', time)
    print (curr_Time)
    print (curr_Date)