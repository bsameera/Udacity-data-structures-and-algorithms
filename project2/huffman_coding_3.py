# Huffman Coding
# A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

# The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

# To prevent ambiguities in decoding, our encoding should satisfy the prefix rule which will result into uniquely decodable codes. The prefix rule states that no code is a prefix of another code.

# There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

# Here is one type of pseudocode for this coding schema:

# Take a string and determine the relevant frequencies of the characters.
# Build and sort a list of tuples from lowest to highest frequencies.
# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).
# Encode the text into its compressed form.
# Decode the text from its compressed form.
# You then will need to create encoding, decoding, and sizing schemas.

# Resources :

# https://www.youtube.com/watch?v=0kNXhFIEd_w
# https://www.includehelp.com/algorithms/huffman-coding-algorithm-example-and-time-complexity.aspx
# https://www.tutorialspoint.com/Huffman-Coding-Algorithm#

# Huffman Visualization!
# https://people.ok.ubc.ca/ylucet/DS/Huffman.html

# Tree Generator -
# http://huffman.ooz.ie/

# Additional Explanation -
# https://www.siggraph.org/

# To sort custom objects :
# https://www.agnosticdev.com/content/how-sort-objects-custom-property-python

# For Example:

import sys

# create a node with char, freq, leftchild, rightchild, parent, code
# create a priority queue and store the sorted tuples of (char, freq)

class Node:
  def __init__(self, char, freq):
    self.char = char
    self.freq = freq
    self.leftchild0 = None
    self.rightchild1 = None
    self.parent = None
    self.code = None

def code_generator(node):
  code = ''
  while True:
    if node.parent is not None:
      code += str(node.code)
    else:
      return code
    node = node.parent

def huffman_encoding(data):
  # returns the encoded data, the tree == nodes_dict & root

  #If the input string is empty, return None
  if len(data) == 0:
    return ('0', None, None)

  root = None
  freq_dict = {}

  for char in data:
    if char in freq_dict:
      freq_dict[char] += 1
    else:
      freq_dict[char] = 1
  #print(freq_dict)

  freq_list = list(freq_dict.items())

  # if the freq_dict has only one element, create a dummy node
  if len(freq_list) == 1:
    freq_list.append(('0', 0))

  freq_list.sort(key=lambda tup: tup[1])

  # create nodes dictionary with keys taken from freq_list and values are nodes
  nodes_dict = {}
  for char, freq in freq_list:
    nodes_dict[char] = Node(char, freq)
  #print(nodes_dict)

  # create new nodes by combining the two minimum nodes, take the first two tuples from freq_list
  # add the new tuple to the freq_list and sort the list in ascending order

  while True:
    min_char1, min_freq1 = freq_list[0]

    min_char2, min_freq2 = freq_list[1]

    new_node = Node(min_char1+min_char2, min_freq1+min_freq2)

    new_node.leftchild0 = nodes_dict[min_char1]
    new_node.leftchild0.code = 0

    new_node.rightchild1 = nodes_dict[min_char2]
    new_node.rightchild1.code = 1

    nodes_dict[min_char1].parent = new_node
    nodes_dict[min_char2].parent = new_node

    # update the nodes dictionary
    nodes_dict[min_char1+min_char2] = new_node

    # update the freq_list with the new tuple
    freq_list.append((new_node.char, new_node.freq))

    # delete the first two tuples
    if len(freq_list) >= 2:
      del freq_list[0]
      del freq_list[0]

    # sort the freq_list
    freq_list.sort(key=lambda tup: tup[1])

    if len(freq_list) == 1:
      break

  rootchar, rootfreq = freq_list[0]
  root = nodes_dict[rootchar]

  codes_dict = {}
  for char in freq_dict:
    new_code = code_generator(nodes_dict[char])
    codes_dict[char] = new_code[::-1]              # reverse the code string

  # print('codes_dict : ',codes_dict)

  encoded_data = ''
  for char in data:
    encoded_data += codes_dict[char]

  return encoded_data, nodes_dict, root


def huffman_decoding(encoded_data, tree, root):
  # tree == nodes_dict
  # when tree, root are None
  if encoded_data == '0' and tree == None and root == None:
    return ''
  root_node = root
  decoded_data = ''

  for bit in encoded_data:
    if bit == '0':
      next_node = root_node.leftchild0
      root_node = next_node
      # check if next_node is a leaf node
      if next_node.leftchild0 is None and next_node.rightchild1 is None:
        char = next_node.char
        decoded_data += char
        root_node = root
    elif bit == '1':
      next_node = root_node.rightchild1
      root_node = next_node
      # check if next_node is a leaf node
      if next_node.leftchild0 is None and next_node.rightchild1 is None:
        char = next_node.char
        decoded_data += char
        root_node = root

  return decoded_data


if __name__ == "__main__":
  codes = {1: "This bird is the world's most beautiful thing.", 2: 'Huffman coding is a data compression algorithm.',
  3: "Udacity's algorithms and data structures.", 4: 'zzzzzzzzzz', 5: ''}

  # test_case is the input string which needs to be encoded and decoded
  def test_function(a_great_sentence):

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data = '1100'+'1101'
    encoded_data, tree, root = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = 'a'+'b'
    decoded_data = huffman_decoding(encoded_data, tree, root)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
    print('*********************************************************************************************************************************************')

  test_function(codes[1])
  test_function(codes[2])
  test_function(codes[3])
  test_function(codes[4])
  test_function(codes[5])

  #a_great_sentence = "Udacity's algorithms and data structures."
  #a_great_sentence = 'zzzzzzzzzz'
  #a_great_sentence = ''


# #print(huffman_encoding(a_great_sentence))
# encoded_data, tree, root = huffman_encoding(a_great_sentence)

# # encoded_data = '1100'+'1101'
# print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
# print ("The content of the encoded data is: {}\n".format(encoded_data))

# decoded_data = huffman_decoding(encoded_data, tree, root)

# # decoded_data = 'a'+'b'
# print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# print ("The content of the decoded data is: {}\n".format(decoded_data))



# explanation for __name__ == __main__:

# # File1.py
# print "File1 __name__ = %s" %__name__

# if __name__ == "__main__":
#   print "File1 is being run directly"
# else:
#   print "File1 is being imported"


# # File2.py
# import File1

# print "File2 __name__ = %s" %__name__

# if __name__ == "__main__":
#   print "File2 is being run directly"
# else:
#   print "File2 is being imported"


# Now the interpreter is given the command to run File1.py.
# python File1.py
# Output :
# File1 __name__ = __main__
# File1 is being run directly


# And then File2.py is run.
# python File2.py
# Output :
# File1 __name__ = File1
# File1 is being imported
# File2 __name__ = __main__
# File2 is being run directly
# As seen above, when File1.py is run directly, the interpreter sets the __name__ variable as __main__ and when it is run through File2.py by importing, the __name__ variable is set as the name of the python script, i.e. File1. Thus, it can be said that if __name__ == “__main__” is the part of the program that runs when the script is run from the command line using a command like python File1.py.

