from datetime import date
from datetime import datetime, timezone, timedelta
import astral
from astral import Astral
import time
import pytz


# import RPi.GPIO as GPIO

# Global Variables
ast = Astral()
city_Name = 'Cleveland'
local_City = ast[city_Name]
sun_Position = local_City.sun(local=True)
reset_Solar = True

# Retrieves and returns current time
def get_Current_Time():
    eastern = pytz.timezone('America/New_York')
    curr_Time = datetime.now(eastern)
    return curr_Time

def main_Function():
    global sun_Position
    current_Time = get_Current_Time()
    solar_Sunrise = sun_Position.get('sunrise')
    solar_Noon = sun_Position.get('noon')
    solar_Sunset = sun_Position.get('sunset')
    calc_Sunrise_Noon = solar_Noon - solar_Sunrise

    total_Seconds = calc_Sunrise_Noon.seconds
    calc_Hours, remainder = divmod(total_Seconds, 3600)
    calc_Minutes, calc_Seconds = divmod(remainder, 60)

    time_To_Adjust = total_Seconds / 24

    if current_Time >= solar_Sunrise and current_Time < solar_Sunset:
        solar_Adjust_Active(time_To_Adjust)
    elif reset_Solar == True:
        reset_Solar_Panel()
    else:
        solar_Adjust_Deactive()

def solar_Adjust_Active(time_To_Adjust):

    while time_To_Adjust > 0:
        current_Time = get_Current_Time()
        time_To_Adjust = time_To_Adjust - 1
        time.sleep(1)
        print (current_Time)
        print (time_To_Adjust)
    daylight_Adjustment()
    
def solar_Adjust_Deactive():
    global local_City
    curr_Time = get_Current_Time()
    calc_Tomorrow = curr_Time + timedelta(days=1)
    sun_Position_Tomorrow = local_City.sun(local=True, date = calc_Tomorrow)
    solar_Sunrise_Tomorrow = sun_Position_Tomorrow.get('sunrise')

    time_Till_Sunrise = solar_Sunrise_Tomorrow - curr_Time

    sunrise_Total_Seconds = time_Till_Sunrise.seconds
    calc_Sunrise_Hours, remainder = divmod(sunrise_Total_Seconds, 3600)
    calc_Sunrise_Minutes, calc_Sunrise_Seconds = divmod(remainder, 60)

    while sunrise_Total_Seconds > 0:
        sunrise_Total_Seconds = sunrise_Total_Seconds - 1
        time.sleep(1)
        print ('Seconds till Sunrise', sunrise_Total_Seconds)
    main_Function()

def daylight_Adjustment():
    global reset_Solar
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
        timer = timer + 1
        
    print ('Panal adjusted')
    # set Open relay back to low (Turns Relay off)
    #GPIO.output(pin_Open, GPIO.LOW)

    # Reset GPIO settings
    #GPIO.cleanup()

    reset_Solar = True
    main_Function()

def reset_Solar_Panel():
    global reset_Solar
    print ('Setting panel back to original position')
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

    reset_Solar = False
    main_Function()

main_Function()