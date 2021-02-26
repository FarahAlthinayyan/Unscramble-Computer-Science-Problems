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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

numbers_called = []


#iterate through all th calls 
for call in calls:
      
      #make sure callers are people from bangalore 
      if call[0][0:5].find("(080)") != -1:
            
            #if it is a fixed line
            if call[1][0] == '(':
                  
                  par_index = call[1].find(')')
                  numbers_called.append(call[1][:par_index+1])

            #if it is a Telemarketer's number 
            elif call[1][0:3].find("140") != -1:
                  
                  numbers_called.append('140')
            
            # all the other numbers 
            else:
                  numbers_called.append(call[1][:4])



#iterate and print all the numbers called by people from bangalore
print("The numbers called by people in Bangalore have codes:")
for code_str in sorted(set(numbers_called)):
    print(code_str)


called_080_sum = numbers_called.count('(080)')
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(called_080_sum*100/(len(numbers_called)), 2)))

                  
            






