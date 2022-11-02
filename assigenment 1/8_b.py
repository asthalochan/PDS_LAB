#Display date separately in “dd/mm/yyyy” format 
import datetime
import calendar
dt=datetime.datetime.now()
today=dt.strftime("%d/%m/%y")
print(f"Today's date is :{today}")

