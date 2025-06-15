print("This program greets you with a message based on your "
"time,\nmake sure it's railway time based")
time = int(input("What is the time?"))

if time < 0 or time > 24:
    print("Invalid input! Try again.")
elif 0 <= time <= 11:
    print("Good Morning!")
elif 12 <= time <= 16:
    print("Good Afternoon!")
else:
    print("Good Night!")


## Above timer only works if you like round off the timming, below has hour and minute format

print("This timer uses railyway timmings too, but enter your time in HH:MM format ")

time = (input("Enter time in HH:MM format")) 
hour, minute = time.split(":")
hour = int(hour)
minute = int(minute)

if 0 <= hour <= 11:
    print("Good Morning!")
elif 12 <= hour <= 16:
    print("Good Afternoon!")
elif hour > 24 or minute >= 60:
    print("Invalid time.")
else:
    print("Good Night!")

### Below timer uses more advanced method, this time with a module.

import time
h = int(time.strftime("%H"))
m = int(time.strftime("%M"))
s = int(time.strftime("%S"))

if 0<=h<=11:
    print("Good Morning!")
elif 12<=h<=16:
    print("Good Evening")    
else: 
    print("Good night")

