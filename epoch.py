import time
from datetime import datetime
#fromtime= input("Enter date & time using the following format:2018,12,26,12,45,31: 	")
#fromtime=(int(fromtime))

from dateutil import parser
from_time = input("Enter: Feb 12 2019 12:00AM")


dt = parser.parse(from_time)
print (dt)

#row=datetime(2018,05,16,12,45,31)
start_epoch = int(round(time.mktime(dt.timetuple())))
print (start_epoch)
