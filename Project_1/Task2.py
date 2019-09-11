"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


calls_dict = {}

for call in calls:
  if call[0] in calls_dict:
    calls_dict[call[0]] += int(call[3])
  else:
    calls_dict[call[0]] = int(call[3])
  if call[1] in calls_dict:
    calls_dict[call[1]] += int(call[3])
  else:
    calls_dict[call[1]] = int(call[3])

#same as above
#from collections import defaultdict

#duration = defaultdict(int)

#for call in calls:
#  duration[call[0]] += int(call[3])
#  duration[call[1]] += int(call[3])


#print(type(calls_dict['78130 00821']))
#print(calls_dict)

#access dictionary calls_dict and find out the max value and it's key

phone_num = max(calls_dict, key=calls_dict.get)
max_time = calls_dict[phone_num]

#phone_num = ''
#max_time = 0

#for key, val in calls_dict.items():
#  if val > max_time:
#    max_time = val
#    phone_num = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_num, max_time))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

