import urllib.request, urllib.parse, urllib.error
import json
import ssl
from datetime import datetime
import zlib
import time
import gzip
import requests
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#in_date=input("Enter The 'Created Date' in the following format: ex: 01-01-01")
#out_date=input("Enter the 'To Date'in the following format: ex: 01-31-19")

url= "https://api.stackexchange.com/2.2/questions?in_date=1548266733&todate=1549390104&order=desc&sort=creation&tagged=azure-storage&site=stackoverflow"
#headers = {'Accept-Encoding': 'gzip'}

# PARAMETERS:
# fromdate=
# todate=
# order=desc
# sort=creation
# tagged=azure-storage
# site=stackoverflow

# data =
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])
# serviceurl =
# order=desc
# site=stackoverflow



    # url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx) # opens link
data = zlib.decompress(uh.read(), 16+zlib.MAX_WBITS)#reads + decompresses content
data=data.decode() #decodes from bytes
js = json.loads(data)
#print(json.dumps(js, indent=4))

list_ansewered = list()
list_untouched = list()
list_proposed = list()
list_creation = list()

for item in js["items"]:
    if item['is_answered'] == False:
        if item["answer_count"] == 0:
        #print("NOT ANSWERED: UNTOUCHED:")
            list_untouched.append(item['link'])
            list_creation.append(item["creation_date"])
        else:
            list_proposed.append(item['link'])
    else:
        list_ansewered.append(item['link'])
#for testing:
        #print("link",item['link'])
        #print("Is Answered",item['is_answered'])
    #elif item['is_answered'] == False and item["answer_count"] > 0 :
    #    list_proposed.append(item['link'])
        #print("ANSWERED:")
        #list_ansewered.append(item['link'])

        #print("link",item['link'])
        #print("Is Answered",item['is_answered'])
#    else: #item['is_answered'] == False and item["answer_count"] > 0 :
        #print ("PROPOSED ANSWERS:")
        #list_ansewered.append(item['link'])
        #print("link",item['link'])
        #print("Is Answered",item['is_answered'])
        #print("Answer Count:",item["answer_count"])
print("===========================================")
print ("UNTOUCHED:")
print("===========================================")
if len(list_untouched)== 0:
    print("No threads are in untouched status")
else:
    for link in list_untouched:
          for date in list_creation:
              date = datetime.fromtimestamp(date).strftime('%c')
              print("link:",link,"Creation Date:",date)
print("===========================================")
print ("PROPOSED:")
print("===========================================")
if len(list_proposed)== 0:
    print("No threads are in PROPOSED ONLY status")
else:
    for link in list_proposed:
        print (link)
print("===========================================")
print("Answered: ")
print("===========================================")
if len(list_ansewered)== 0:
    print("No threads are in ANSWERED")
else:
    for link in list_ansewered:
        print(link)











#print('Retrieved', len(data), 'characters')


#try:
#js = json.loads(data)
#except:
    #js = None

    #if not js or 'status' not in js or js['status'] != 'OK':
    #    print('==== Failure To Retrieve ====')
    #    print(data)
    #    continue

