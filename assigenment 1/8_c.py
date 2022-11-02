#Display time in 24 hour forma 
import datetime
import calendar
dt=datetime.datetime.now()
time=dt.strftime("%H:%M:%S")
print(f"The time is :{time}")

