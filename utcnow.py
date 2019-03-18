import datetime
utc_datetime = datetime.datetime.utcnow()
result = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
result=result.split()
print (result[0])
