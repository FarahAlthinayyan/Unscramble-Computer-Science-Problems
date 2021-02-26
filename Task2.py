"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from itertools import chain
from collections import deque, defaultdict
from datetime import date, datetime

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016"
"""
from datetime import datetime

calls_dictionary = defaultdict(int)

#iterate through the calls 
for calling_number, recieving_number, timestamp, duration_string in calls:

    date_and_time = datetime.strptime(timestamp, '%d-%m-%Y %H:%M:%S')

    if(date_and_time.month == 9 and date_and_time.year == 2016):
        #convert to integer
        duration = int(duration_string)
        calls_dictionary[calling_number] += duration
        calls_dictionary[recieving_number] += duration


# find the max duration 
max_duration = max(calls_dictionary.values())


list_of_values = list(calls_dictionary.values())
list_of_keys = list(calls_dictionary.keys())

position = list_of_values.index(max_duration)

print( list_of_keys[position]," spent the longest time, ",max_duration," seconds, on the phone during September 2016.")

