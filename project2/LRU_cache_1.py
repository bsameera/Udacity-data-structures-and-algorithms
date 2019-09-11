# Least Recently Used Cache :
# We have briefly discussed caching as part of a practice problem while studying hash maps.

# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

# Your job is to use an appropriate data structure(s) to implement the cache.

# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.

# For the current problem, you can consider the size of cache = 5.

# Here is some boiler plate code and some example test cases to get you started on this problem:
# create a node with prev and next pointers i.e. doubly linkedlist

# https://www.geeksforgeeks.org/ordereddict-in-python/ - ordered dict

# The dictionary has a key and the value is the double node, also the node has attributes of key, data, next and prev

class Double_node:
  def __init__(self, key, data):
    self.key = key
    self.data = data
    self.next = None
    self.prev = None

class LRU_Cache(object):

  def __init__(self, capacity):
    # Initialize class variables
    self.LRU_dict = dict()
    self.size = 0
    self.capacity = capacity
    self.head = None
    self.tail = None
    self.key_to_tail = None

  def add_to_top(self, key, value):
    # make the new node as head
    new_node = Double_node(key, value)
    if self.head is None:
      self.head = new_node
      self.tail = self.head
      # since head and tail are same for the first node created, and this key can be used to delete the tail node when the cache reaches the limit
      self.key_to_tail = key
    else:
      self.head.prev = new_node
      new_node.prev = None
      new_node.next = self.head
      self.head = new_node
    #update key and value in the dictionary
    self.LRU_dict[key] = new_node

  def delete_node(self, key):
    cur_node = self.LRU_dict[key]

    # case 1 - node to be deleted is the tail node
    # if the node to be deleted is a tail node, change the value of self.key_to_tail
    if cur_node.next == None:
      pre = cur_node.prev
      pre.next = None
      cur_node.prev = None
      cur_node = None
      #update tail_node and self.key_to_tail
      self.tail = pre
      self.key_to_tail = pre.key
      # delete the key/value in dictionary
      del self.LRU_dict[key]
      return
    # case 2 - If node to be deleted is the head node
    elif cur_node.prev == None:
      nxt = cur_node.next
      nxt.prev = None
      # change the next node to head node
      self.head = nxt
      cur_node.next = None
      cur_node = None
      # delete the key/value in dictionary
      del self.LRU_dict[key]
      return
    # case 3 - node to be deleted is in the middle of the doubly linkedlist
    else:
      nxt = cur_node.next
      pre = cur_node.prev
      pre.next = nxt
      nxt.prev = pre
      # set cur_node's value, next and prev to None
      cur_node.prev = None
      cur_node.next = None
      cur_node = None
      # delete the key/value in dictionary
      del self.LRU_dict[key]
      return

  def get(self, key):
    # Retrieve item from provided key. Return -1 if nonexistent.
    if key in self.LRU_dict:
      value = self.LRU_dict[key].data
      # delete node and add to top, self.size remains same
      self.delete_node(key)
      self.add_to_top(key, value)
      # print('key : ', key)
      return value
    # returns -1, if key not present in dictionary
    return -1

  def set(self, key, value):
    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    if key in self.LRU_dict:
      # delete node and add node to top/head
      self.delete_node(key)
      self.add_to_top(key, value)

    if key not in self.LRU_dict:
      if self.capacity == 0:
        print('Capacity while creating cache should be more than zero, can not add new keys')
        return
      elif self.size < self.capacity:
        # add node to top/head
        self.add_to_top(key, value)
        self.size += 1
      elif self.size == self.capacity:
        # delete tail node and add the new node to top/head
        tail_key = self.key_to_tail
        self.delete_node(tail_key)
        self.add_to_top(key, value)

    # print('key : ', key)
    # print('value : ', (self.LRU_dict[key]).data)
    # print('dict - ', self.LRU_dict)

our_cache = LRU_Cache(5)

print('Add 1 to LRU cache')
our_cache.set(1, 1)

print('Add 2 to LRU cache')
our_cache.set(2, 2)

print('Add 3 to LRU cache')
our_cache.set(3, 3)

print('Add 4 to LRU cache')
our_cache.set(4, 4)

print('Size of LRU Cache is ', our_cache.size)           # returns 4

print('Retrieve 1 if available : ', our_cache.get(1))       # returns 1
print('Retrieve 2 if available  : ', our_cache.get(2))       # returns 2
print('Retrieve 9 if available  : ', our_cache.get(9))      # returns -1 because 9 is not present in the cache

print('Add 5 to LRU cache')
our_cache.set(5, 5)
print('Add 6 to LRU cache')
our_cache.set(6, 6)

print('Retrieve 3 if available  : ', our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry and was deleted

print('Add 7 to LRU cache')
our_cache.set(7, 7)

print('Size of LRU Cache is ', our_cache.size)       # returns 5

print('Retrieve 4 if available : ', our_cache.get(4))
# returns -1 because the cache reached it's capacity and 4 was the least recently used entry and was deleted

print('Update 7 in LRU cache to 3')
our_cache.set(7, 3)

print('Retrieve 7 if available : ', our_cache.get(7))

# testcase where capacity is zero
new_cache = LRU_Cache(0)

print('Add 1 to LRU cache')
new_cache.set(1, 1)

print('Retrieve 1 if available : ', new_cache.get(1))
