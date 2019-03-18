import urllib.request, urllib.parse, urllib.error
import json
import ssl
from datetime import datetime
import zlib
import time
import gzip
import requests
from dateutil import parser
#pip3 install python-dateutil
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
in_date=input("Enter The 'From Created Date' in the following format: ex: Feb 12 2019 12:00AM:  ")
out_date=input("Enter The 'TO Created Date' in the following format: ex: Feb 12 2019 12:00AM:   ")

dt_from = parser.parse(in_date)
dt_to = parser.parse(out_date)

epoch_from = int(round(time.mktime(dt_from.timetuple())))
epoch_from = str(epoch_from)
epoch_to = int(round(time.mktime(dt_to.timetuple())))
epoch_to=str(epoch_to)
storageurls= []
tag_list_storage=["azure-storage","azure-storage-queues","azure-blob-storage","azure-disk","azure-storage-emulator","azure-files"]
for tag in tag_list_storage:
    url= "https://api.stackexchange.com/2.2/questions?fromdate="+epoch_from+"&todate="+epoch_to+"&order=desc&sort=creation&tagged="+tag+"&site=stackoverflow"
    storageurls.append(url)

#headers = {'Accept-Encoding': 'gzip'}
# all tags:
# PARAMETERS:
# fromdate=
# todate=
# order=desc
# sort=creation
# tagged=azure-storage, azure-storage-queues,azure-blob-storage, azure-disk,azure-storage-emulator,azure-files
# site=stackoverflow
# data =
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])
# serviceurl =
# order=desc
# site=stackoverflow

# url = serviceurl + urllib.parse.urlencode(parms)
for url in storageurls:
    #print('Retrieving', url)
    divided = url.split("&")
    #print (divided)


    uh = urllib.request.urlopen(url, context=ctx) # opens link
    data = zlib.decompress(uh.read(), 16+zlib.MAX_WBITS)#reads + decompresses content
    data=data.decode() #decodes from bytes
    js = json.loads(data)
#print(json.dumps(js, indent=4))

    list_ansewered = []
    list_untouched = []
    list_proposed = []
    list_creation = []
    list_creation_proposed=[]
    list_creation_ansewered=[]

    for item in js["items"]:
        if item['is_answered'] == False:
            if item["answer_count"] == 0:
        #print("NOT ANSWERED: UNTOUCHED:")
                list_untouched.append(item['link'])
                list_creation.append(item["creation_date"])
            else:
                list_proposed.append(item['link'])
                list_creation_proposed.append(item["creation_date"])
        else:
            list_ansewered.append(item['link'])
            list_creation_ansewered.append(item["creation_date"])

    print("\n" * 2)
    print("==============",divided[4],"==============")
    print("===========================================")
    print ("UNTOUCHED:")
    print("===========================================")
    if len(list_untouched)== 0:
        print("No threads are in untouched status")
    else:
        for link,date in zip(list_untouched, list_creation):
            date = datetime.fromtimestamp(date).strftime('%c')
            print('{} {}'.format(link, date))

    print("===========================================")
    print ("PROPOSED:")
    print("===========================================")
    if len(list_proposed)== 0:
        print("No threads are in PROPOSED ONLY status")
    else:

        for link,date in zip(list_proposed,list_creation_proposed):
            date = datetime.fromtimestamp(date).strftime('%c')
            print('{} {}'.format(link, date))

    print("===========================================")
    print("Answered: ")
    print("===========================================")
    if len(list_ansewered)== 0:
        print("No threads are in ANSWERED")
    else:
        for link,date in zip(list_ansewered,list_creation_ansewered):
            date = datetime.fromtimestamp(date).strftime('%c')
            print('{} {}'.format(link, date))

