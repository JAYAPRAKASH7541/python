Input:
3
Sun 05 Jan 2020 13:54:30 -0000
Sun 05 Jan 2020 13:54:58 -0000
Thu 08 Jan 2020 09:00:00 -0000
Thu 08 Jan 2020 14:01:00 +0500
Wed 07 Jan 2020 07:30:00 +0500
Wed 07 Jan 2020 02:35:39 -0000

Output:
just now
1 minute ago
5 minutes ago


--------
from datetime import datetime,timedelta

def cal_time(date_obj):
         date_obj = date_obj//60
         if date_obj//60>1:
             print('{} hours ago'.format(date_obj//60))
         elif date_obj//60==1:
             print('1 hour ago')
         elif date_obj<1:
             print('just now')
         elif date_obj==1:
             print('{} minute ago'.format(date_obj))
         else:
             print('{} minutes ago'.format(date_obj))

def cal_days(date_obj):
         if date_obj==1:
             print('{} day ago'.format(date_obj))
         else:
             print('{} days ago'.format(date_obj))

def cal_weeks(date_obj):
         if date_obj==1:
             print('{} week ago'.format(date_obj))
         else:
             print('{} weeks ago'.format(date_obj))
def cal_years(date_obj):
         if date_obj==1:
             print('{} year ago'.format(date_obj))
         else:
             print('{} years ago'.format(date_obj))
def cal_months(date_obj):
         if date_obj==1:
             print('{} month ago'.format(date_obj))
         else:
             print('{} months ago'.format(date_obj))

num = int(input())
for i in range(num):
     timezone1 = input()
     timezone2 = input()
     date1 = datetime.strptime(timezone1,'%a %d %b %Y %H:%M:%S %z')
     date2 = datetime.strptime(timezone2,'%a %d %b %Y %H:%M:%S %z')

     result = date2-date1
     if result.days//365>=1:
         cal_years(result.days//365)
     elif result.days//31>=1:
         cal_months(result.days//31)
     elif result.days//7>=1:
         cal_weeks(result.days//7)
     elif result.days!=0 and result.days//7<1:
         cal_days(result.days)
     elif result.days==0:
         cal_time(result.seconds)
