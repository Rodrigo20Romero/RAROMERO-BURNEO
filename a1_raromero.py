#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Winter 2020
Program: a1_raromero.py 
Author: Rodrigo Romero
The python code in this file (a1_raromero.py) is original work written by
--Rodrigo Romero--. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''

import sys
import os

def usage():
    '''
    Usage: a1_rchan.py [--step] YYYY-MM-DD +/-n
    Takes a valid date (DATE) and a number of days (NUMDAYS)
    and returns a certain number of days specified.
    '''
    if len(sys.argv) != 4 or len(sys.argv) != 3:
        print('Usage:',sys.argv[0],'[--step] YYYY-MM-DD +/- n')

if len(sys.argv) == 4:
    if len(sys.argv[2]) == 10:
        date1=sys.argv[2]
        str_year, str_month, str_date=date1.split('-')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[3])
        step=True
    else:
	    print("Error: wrong date entered")
	    sys.exit()
elif len(sys.argv) == 3:
    if len(sys.argv[1]) == 10:
        date1=sys.argv[1]
        str_year, str_month, str_date=date1.split('-')
        year=int(str_year)
        month=int(str_month)
        date=int(str_date)
        days=int(sys.argv[2])
    else:
	    print("Error: wrong date entered")
	    sys.exit()
else:
    usage()   


def valid_date():
    '''
   The valid_date() function will take a date in "YYYY-MM-DD" format, 
        and return True if the given date is a valid date, otherwise return False.
    '''
    if len(sys.argv) == 4:
        if date <= 31 and month <= 12 and len(sys.argv[2]) == 10:
            return 'true'
        else:
            if date > 31:
                b= "Error: wrong day entered"
            elif month > 12:
                b = 'Error: wrong month entered'
            elif len(sys.argv[2]) != 10:
                b = "Error: wrong date entered"
            return b
    elif len(sys.argv) == 3:
        if date <= 31 and month <= 12 and len(sys.argv[1]) == 10:
            return 'true'
        else:
            if date > 31:
                b= "Error: wrong day entered"
            elif month > 12:
                b= "Error: wrong month entered"
            elif len(sys.argv[1]) != 10:
                b= "Error: wrong date entered"
            return b
    else:
        usage()



def leap_year():
    '''
    The leap_year() function will take a year in "YYYY" format, 
        and return True if the given year is a leap year, otherwise return False.
        Examples:
        leap_year(2018)
        -False
        leap_year(2020)
        -True
    '''
    if valid_date() == 'true':
        if (year % 400) == 0 or (year%100 !=0 and year%4==0) :
	        return True
        else:
            return False
    else:
        return valid_date()


def days_in_month(month):
    '''
    days_in_mon() function will take given year and calculate the maximum days of each month
        It will return the dictionary which contains all the months with its maximum days.
    ''' 
    if valid_date() == 'true':
        if leap_year():
            feb_max=29
        else:
            feb_max=28
        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        days_m=mon_max[month]
        return days_m


def after(today):
    '''
    after(today) -> str
    after() -> date for next day in YYYY-MM-DD string format
    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    if valid_date() == 'true':
        date_1=today
        str_year, str_month, str_date=date_1.split('-')
        year_1=int(str_year)
        month_1=int(str_month)
        date_1=int(str_date)
        temp_date= date_1 + 1
        if temp_date > days_in_month(month_1):
            temp_date = 1
            temp_month = month_1+1
            temp_year=year_1
            if temp_month > 12: 
                temp_month = 1
                temp_year=year_1 +1
        else:
            temp_month=month_1
            temp_year=year_1 
        next_day=str(temp_year).zfill(4)+'-'+str(temp_month).zfill(2)+'-'+str(temp_date).zfill(2)
        return next_day
    else:
        return valid_date()


          
def before(today):
    '''
   after() -> date for previous day in YYYY-MM-DD string format
    Return the date for the previous day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    if valid_date() == 'true':
        date2=today
        str_year, str_month, str_date=date2.split('-')
        year_2=int(str_year)
        month_2=int(str_month)
        date_2=int(str_date)
        temp_date2= date_2 - 1
        if temp_date2 == 0 :
            temp_month2 = month_2 - 1
            if temp_month2 == 0: 
                temp_month2 = 12
                temp_year2=year_2 - 1
            else:
                temp_year2=year_2
            temp_date2=days_in_month(temp_month2)
        else:
            temp_month2=month_2
            temp_year2=year_2 
        previous_day=str(temp_year2).zfill(4)+'-'+str(temp_month2).zfill(2)+'-'+str(temp_date2).zfill(2)
        return previous_day
    else:
        return valid_date()



def dbda(z, days):
    '''
    The function will add or subtract the amount of days corresponding to the interger from the given date and determine the new date.
    '''
    if len(sys.argv) == 3:
        if int(days)>= 0:
            for x in range(int(days)):
                z=after(z)
            return z
        if int(days) < 0:
            for x in range(abs(int(days))):
                z=before(z)
            return z
    elif  len(sys.argv) == 4:
        if int(days) >= 0:
            for x in range(int(days)):
                z=after(z)
                print(z)
        if int(days) < 0:
            for x in range(abs(int(days))):
                z=before(z)
                print(z)	
    


if __name__ == "__main__":
    if len(sys.argv) == 3: 
        print(dbda(sys.argv[1],sys.argv[2]))
    elif (len(sys.argv)==4 and sys.argv[1]== '--step'):
        dbda(sys.argv[2],sys.argv[3]) 