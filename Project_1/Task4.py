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

outgoing_call_nums= set()
recieving_call_nums = set()
text_nums = set()

for call in calls:
  outgoing_call_nums.add(call[0])
  recieving_call_nums.add(call[1])

for text in texts:
  text_nums.update([text[0], text[1]])

telemarketers = outgoing_call_nums - recieving_call_nums
telemarketers = telemarketers - text_nums

#sorted() returns a list
sorted_telemarketers = sorted(telemarketers)


print("These numbers could be telemarketers: ")
#print(len(sorted_telemarketers))
#for tele in sorted_telemarketers:
#  print(tele)

print(* sorted_telemarketers, sep='\n')

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

