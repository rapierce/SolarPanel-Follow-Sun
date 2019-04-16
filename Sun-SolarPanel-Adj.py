from datetime import date
from datetime import datetime
import astral
from astral import Astral
import time

# Retrieves and returns current time
def get_Current_Time():
    curr_Time = datetime.now()
    return curr_Time

def solar_Adjust_Active(sol_Rise, sol_Set, tta):
    adjustment_Timer = tta
    current_Time = get_Current_Time()
    while current_Time > sol_Rise and current_Time < sol_Set:
        if tta != 0:
            current_Time = get_Current_Time
            tta = tta - 1
            time.sleep(1)
            print (tta)
        else:
            daylight_Adjustment()
    reset_Solar_Panel()

def daylight_Adjustment():
    # Adustment to Solar Panel
    #GPIO.setmode(GPIO.BCM)

    # init pin numbers
    #pin_Open = [6]

    # set mode default state is 'low'
    #GPIO.setup(pin_Open, GPIO.OUT) 
   
    # Activate Open Relay to High (High turns Relay on)
    #GPIO.output(pin_Open, GPIO.HIGH)     # Activate Open relay
    
    # Start Timer for duration actuator will be activated
    timer = 0
    while timer <= 1:
        time.sleep(1)
        timer = timer + .1
        

    # set Open relay back to low (Turns Relay off)
    #GPIO.output(pin_Open, GPIO.LOW)

    # Reset GPIO settings
    #GPIO.cleanup()

def reset_Solar_Panel():
    # Adustment to Solar Panel
    # GPIO.setmode(GPIO.BCM)

    # init pin numbers
    # pin_Open = [XX]

    # set mode default state is 'low'
    # GPIO.setup(pin_Open, GPIO.OUT) 
   
    # Activate Open Relay to High (High turns Relay on)
    # GPIO.output(pin_Open, GPIO.HIGH)     # Activate Open relay
    
    # Start Timer for duration actuator will be activated
    timer = 0
    while timer <= 48:
        time.sleep(1)
        timer = timer + 1
        

    # set Open relay back to low (Turns Relay off)
    # GPIO.output(pin_Open, GPIO.LOW)

    # Reset GPIO settings
    # GPIO.cleanup()


ast = Astral()
city_Name = 'Cleveland'
curr_Date = date.today()
curr_Time = get_Current_Time()
local_City = ast[city_Name]
sun_Position = local_City.sun(local=True)

solar_Sunrise = sun_Position.get('sunrise')
solar_Noon = sun_Position.get('noon')
solar_Sunset = sun_Position.get('sunset')
calc_Sunrise_Noon = solar_Noon - solar_Sunrise

total_Seconds = calc_Sunrise_Noon.seconds
calc_Hours, remainder = divmod(total_Seconds, 3600)
calc_Minutes, calc_Seconds = divmod(remainder, 60)

time_To_Adjust = total_Seconds / 24

print (solar_Sunrise)
print (solar_Noon)
print (calc_Sunrise_Noon)
print (total_Seconds)
print (time_To_Adjust)

solar_Adjust_Active(solar_Sunrise, solar_Sunset, time_To_Adjust)