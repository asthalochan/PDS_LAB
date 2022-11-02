#Display time in 12 hour format
import datetime
import calendar
dt=datetime.datetime.now()
time=dt.strftime("%I:%M:%S %p")
print(f"The time is : {time}")

