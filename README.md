# SolarPanel-Follow-Sun
Program to adjust the solar panels to face the sun as it moves throughout the day.

Plan is to pull in the sunrise, sunset, and solarnoon times and calculate how much to move an 8 inch actuator every 10 minutes so that the solar panels are always getting optimum sunlight throughout the day.  At sunset, the solar panels will return to sunrise positioning.

The actuator will be controled using a raspberry pi turning the relays on for the given amount of time every 10 minutes. The program will be written in Python.
