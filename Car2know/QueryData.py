from urllib2 import Request, urlopen, URLError
from datetime import time
from datetime import date
import datetime
import time
import sys
import os


# Using request and urlopen to get data from car2go's API
#   We need the city name and consumer_key
def querydata():
    request = Request("http://www.car2go.com/api/v2.1/vehicles?loc=Seattle&oauth_consumer_key=Fleet-size&format=json")

    try:
        response = urlopen(request)
        return response.read()
#         raise Exception('spam', 'eggs')
    except Exception as e:
        print datetime.datetime.now(), ' Got an error:', str(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return ""

# The input is the time interval to query data in seconds
#   as well as the storage path of the file
#   At first, automatically generate the date when query data
#   Then build a txt file with the date as the name
#   If a new day come, automatically build a new txt file
#   At last, query data from car2go's api
def StoreData(interval, path):
    dt = datetime.datetime.now()
    tt = dt.timetuple()
    year = tt[0]
    month = tt[1]
    day = tt[2]
    hour = tt[3]
    minute = tt[4]
    second = tt[5]
    previousDate = str(year) + str(month).zfill(2) + str(day).zfill(2)
    currentDate = str(year) + str(month).zfill(2) + str(day).zfill(2)
    
    f = open(path + currentDate + '.txt','a')
    
    while 1:
        time.sleep(1)
        dt = datetime.datetime.now()
        tt = dt.timetuple()
        year = str(tt[0])
        month = str(tt[1])
        day = str(tt[2])
        hour = str(tt[3])
        minute = str(tt[4])
        second = str(tt[5])
        
        currentDate = year + month.zfill(2) + day.zfill(2)
        currentTime = hour.zfill(2) + minute.zfill(2)+ second.zfill(2)
        
        if currentDate != previousDate:
            f = open(path + currentDate + '.txt','a')
            prviousDate = currentDate
        
        if int(second) % interval == 0:
#             print hour+" "+minute +" "+ second
            data = querydata()
            f.write(currentTime + ';' + data +'\n')
#   Main function
if __name__ == '__main__':
    path = 'F:\\car2godata\\Seattle\\'
    StoreData(30, path)
        
