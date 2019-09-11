# Union and Intersection of Two Linked Lists
# Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

# You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

# We have provided a code template below, you are not required to use it:

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __repr__(self):
    return str(self.value)

class LinkedList:
  def __init__(self):
    self.head = None

  def __str__(self):
    cur_head = self.head
    out_string = ""
    while cur_head:
        out_string += str(cur_head.value) + " -> "
        cur_head = cur_head.next
    return out_string


  def append(self, value):

    if self.head is None:
        self.head = Node(value)
        return

    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)

  def size(self):
    size = 0
    node = self.head
    while node:
        size += 1
        node = node.next

    return size

# def union(linked_list_1, linked_list_2):
#   # store the nodes in a dictionary with the value as the key
#   union_dict = {}

#   head1 = linked_list_1.head
#   while head1:
#     if head1.value not in union_dict:
#       union_dict[head1.value] = head1.value
#     head1 = head1.next

#   head2 = linked_list_2.head
#   while head2:
#     if head2.value not in union_dict:
#       union_dict[head2.value] = head2.value
#     head2 = head2.next

#   linked_list_union = LinkedList()
#   for key in union_dict:
#     linked_list_union.append(key)

#   return linked_list_union


# def intersection(linked_list_1, linked_list_2):
#   linked_list_1_dict = {}
#   linked_list_2_dict = {}
#   linked_list_intersection = LinkedList()

#   head1 = linked_list_1.head
#   while head1:
#     if head1.value not in linked_list_1_dict:
#       linked_list_1_dict[head1.value] = head1.value
#     head1 = head1.next

#   head2 = linked_list_2.head
#   while head2:
#     if head2.value not in linked_list_2_dict:
#       linked_list_2_dict[head2.value] = head2.value
#     head2 = head2.next

#   temp = set(linked_list_2_dict.keys())
#   intersection = set([value for value in linked_list_1_dict.keys() if value in temp])

#   for element in intersection:
#     linked_list_intersection.append(element)

#   return linked_list_intersection

# https://www.jessicayung.com/python-lists-vs-dictionaries-the-space-time-tradeoff/
def union(linked_list_1, linked_list_2):
  linked_list_union = LinkedList()

  # create two sets for each linkedlist individually
  set1 = set()
  head1 = linked_list_1.head
  while head1:
    set1.add(head1.value)
    head1 = head1.next

  set2 = set()
  head2 = linked_list_2.head
  while head2:
    set2.add(head2.value)
    head2 = head2.next

  union_set = set1.union(set2)

  for i in union_set:
    linked_list_union.append(i)

  return linked_list_union

def intersection(linked_list_1, linked_list_2):

  if linked_list_1.head == None or linked_list_2.head == None:
    return None

  linked_list_intersection = LinkedList()

  # create two sets for each linkedlist individually
  set1 = set()
  head1 = linked_list_1.head
  while head1:
    set1.add(head1.value)
    head1 = head1.next

  set2 = set()
  head2 = linked_list_2.head
  while head2:
    set2.add(head2.value)
    head2 = head2.next

  intersection_set = set1.intersection(set2)

  # when there are no common elements
  if len(intersection_set) == 0:
    return None

  for i in intersection_set:
    linked_list_intersection.append(i)

  return linked_list_intersection


# def are_equal(linked_list_1, linked_list_2):
#   if linked_list_1.size() != linked_list_2.size():
#     return False
#   else:
#     head1 = linked_list_1.head
#     head2 = linked_list_2.head
#     while head1:
#       if head1.value != head2.value:
#         return False
#       else:
#         head1 = head1.next
#         head2 = head2.next
#   return True


# def test_function(test_case):

#   linked_list_1 = test_case[0]
#   linked_list_2 = test_case[1]
#   union_solution = test_case[2]
#   intersection_solution = test_case[3]

#   union_output = union(linked_list_1,linked_list_2)

#   intersection_output = intersection(linked_list_1,linked_list_2)

#   if are_equal(union_solution, union_output)==True and are_equal(intersection_solution, intersection_output)==True:
#     print('Pass')
#   else:
#     print('Fail')
print('\n')
print('Test case 1')

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
# union_solution = LinkedList()
# intersection_solution = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
# element_3 = sorted([3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11])
# element_4 = sorted([4, 21, 6])

for i in element_1:
  linked_list_1.append(i)

for i in element_2:
  linked_list_2.append(i)

# for i in element_3:
#   union_solution.append(i)

# for i in element_4:
#   intersection_solution.append(i)

# test_function([linked_list_1, linked_list_2, union_solution, intersection_solution])
print('linked_list_1 : ', linked_list_1)
print('linked_list_2 : ', linked_list_2)
print ('Union : ', union(linked_list_1,linked_list_2))
print ('Intersection : ', intersection(linked_list_1,linked_list_2))

print('\n')
print('Test case 2')

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
# union_solution = LinkedList()
# intersection_solution = LinkedList()

element_3 = [3,2,4,35,6,65,6,4,3,23]
element_4 = [1,7,8,9,11,21,1]
# element_3 = sorted([3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21])
# element_4 = []

for i in element_3:
  linked_list_3.append(i)

for i in element_4:
  linked_list_4.append(i)

# for i in element_3:
#   union_solution.append(i)

# for i in element_4:
#   intersection_solution.append(i)

# test_function([linked_list_3, linked_list_4, union_solution, intersection_solution])
print('linked_list_3 : ', linked_list_3)
print('linked_list_4 : ', linked_list_4)
print ('Union : ', union(linked_list_3,linked_list_4))
print ('Intersection : ', intersection(linked_list_3,linked_list_4))

print('\n')
print('Test case 3')

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_5 = [6, 4, 3, 2, 1, 90, 44, 126, 33]
element_6 = []

for i in element_5:
  linked_list_5.append(i)

for i in element_6:
  linked_list_6.append(i)

print('linked_list_5 : ', linked_list_5)
print('linked_list_6 : ', linked_list_6)
print ('Union : ', union(linked_list_5,linked_list_6))
print ('Intersection : ', intersection(linked_list_5,linked_list_6))
