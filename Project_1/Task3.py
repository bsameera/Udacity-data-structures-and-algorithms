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

area_codes_list = []

count_080 = 0
#call[0] == A and call[1] == B
for call in calls:
  if call[0][0:5] == '(080)':
    area_code = ''
    recieved = call[1]
    if recieved[0] == '(':
      area_code = recieved.split(')')[0][1:]
      if area_code == '080':
        count_080 += 1
    if recieved[0] == '7' or recieved[0] == '8' or recieved[0] == '9':
      area_code = recieved[0:4]
    if recieved[0:3] == '140':
      area_code = '140'
    area_codes_list.append(area_code)

#print(len(area_codes_list))
#print(count_080)

#uniq_area_codes_list = list(set(area_codes_list))
#uniq_area_codes_list.sort()

uniq_area_codes_list = sorted(set(area_codes_list))
#print(uniq_area_codes_list)
print("The numbers called by people in Bangalore have codes:")
#for area_code in uniq_area_codes_list:
#  print(area_code)
print(* uniq_area_codes_list, sep='\n')

#part B
calls_bang_to_bang = (count_080*100)/len(area_codes_list)
#print(round(calls_bang_to_bang, 2))
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(calls_bang_to_bang, 2)))

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
