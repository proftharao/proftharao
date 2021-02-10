import datetime
# import bus fare challenge
from datetime import date
import calendar
date = date.today()
print("Date:" + str(date))
print("Day:" + date.strftime("%a"))
fare = int(0)
if date.strftime('Mon'):
    fare = 100

if date.strftime('Tue'):
    fare = 100
elif date.strftime("Wed"):
    fare = 100
elif date.strftime("Thu"):
    fare = 100
elif date.strftime("Fri"):
    fare = 100 
elif date.strftime("Sat"):
    fare = 60
elif date.strftime("Sun"):
    fare = 80
print("Fare:" + str(fare))
