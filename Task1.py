"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# add all the telephone numbers to the list 
number_of_phone_numbers = []

#iterate through each and every row of texts
for text in texts:
    #add the incoming and recieving numbers for texts 
    number_of_phone_numbers.append(text[0])
    number_of_phone_numbers.append(text[1])

#iterate through each and every row of calls 
for call in calls:
    #add the incoming and recieving numbers for calls 
    number_of_phone_numbers.append(call[0])
    number_of_phone_numbers.append(call[1])


# print the different telephone numbers
print("There are {} different telephone numbers in the records.".format(len(set(number_of_phone_numbers))))
