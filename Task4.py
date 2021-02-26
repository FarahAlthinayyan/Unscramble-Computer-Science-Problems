"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from itertools import chain
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# how to Identify the numbers that might be doing telephone marketing 

#they always call but never called  and never send texts or receive texts


callers = []
called = []

#get all th numbers
for row in calls:
    callers.append(row[0])
    called.append(row[1])

# to remove the dupicates make a set out of it 
callers = set(callers)
called = set(called)


texters = []
texted = []

#get all the numbers
for row in texts:
    texters.append(row[0])
    texted.append(row[1])

# to remove the dupicates make a set out of it 
texters = set(texters)
texted = set(texted)


# find number of possible telemarketers 
possible_telemarketers = [number for number in callers if((number not in called) & (number not in texters) & (number not in texted))]


print("These numbers could be telemarketers: ")
# sorting the numbers 
possible_telemarketers = sorted(possible_telemarketers)
for number in possible_telemarketers:
    print(number)