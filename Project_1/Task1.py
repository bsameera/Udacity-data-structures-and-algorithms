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

#Make an empty set instead of a list, for efficiency and less lines of code
#phone_numbers_list = []
phone_numbers_set = set()

for text in texts:
  phone_numbers_set.update([text[0], text[1]])

for call in calls:
  phone_numbers_set.update([call[0], call[1]])


#phone_numbers_set = set(phone_numbers_list)


print("There are {} different telephone numbers in the records.".format(len(phone_numbers_set)))

"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
