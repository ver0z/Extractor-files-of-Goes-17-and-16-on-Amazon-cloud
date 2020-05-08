import s3fs
import numpy as np
import datetime
from datetime import date

today = str(date.today())
today_date_time = datetime.datetime.today()
now = datetime.datetime.now()
year = now.year


# Get the data from today
time_finish = today_date_time.hour
fmt = '%Y-%m-%d'
dt = datetime.datetime.strptime(today, fmt)
tt = dt.timetuple()
day_in_year = str(tt.tm_yday)
hour = range(0, 24)

# Get the data from a specific year, day and time.
# year = 2020
# day_in_year = 189

# Use the anonymous credentials to access public data
fs = s3fs.S3FileSystem(anon=True)

# List contents of GOES-16 bucket.
fs.ls('s3://noaa-goes16/')

for t in hour:

    if t < 10:
        files = np.array(fs.ls('noaa-goes17/ABI-L1b-RadC/{0}/{1}/0{2}/'.format(year, day_in_year, t)))
        print(files)

    else:
        files = np.array(fs.ls('noaa-goes17/ABI-L1b-RadC/{0}/{1}/{2}/'.format(year, day_in_year, t)))
        print(files)

length = len(files)  # Getting the number of .nc files
print(length)
# for i in range(0, length):
#    fs.get(files[i], files[i].split('/')[-1])  # Writting all those .nc files in the directory of your script

print('End')
