# Blockchain :

# https://en.wikipedia.org/wiki/Blockchain
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/Greenwich_Mean_Time

# A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

# Use your knowledge of linked lists and hashing to create a blockchain implementation.

# We can break the blockchain down into three main parts.

# First is the information hash:

# import hashlib

# def calc_hash(self):
#   sha = hashlib.sha256()

#   hash_str = "We are going to encode this string of data!".encode('utf-8')

#   sha.update(hash_str)

#   return sha.hexdigest()

# We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

# The next main component is the block on the blockchain:

import hashlib
import datetime

class BlockChainList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.num_blocks = 0

  def add_block(self, data=None):
    if type(data) != str or data == None:
      print('Please enter valid data of type string')
      return
    new_block = Block(data)
    if self.head is None:
      self.head = new_block
      self.tail = new_block
    else:
      new_block.previous_hash = self.tail.hash
      self.tail = new_block
    self.num_blocks += 1
    print('Block - ' + str(self.num_blocks))
    print(new_block)

  def size(self):
    return self.num_blocks


class Block:
  def __init__(self, data):
    self.data = data
    self.previous_hash = 0
    self.hash = self.calc_hash()
    self.timestamp = datetime.datetime.now().strftime("%d %B,%Y %I:%M%p")

  def calc_hash(self):
    sha = hashlib.sha256()
    #hash_str = "We are going to encode this string of data!".encode('utf-8')
    hash_str = self.data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()

  def __str__(self):
    # return str(self.__class__) + ": " + str(self.__dict__)
    return str(self.__dict__)

# Above is an example of attributes you could find in a Block class.

# Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. All of this will help you build up to a simple but full blockchain implementation!

BlockChainList = BlockChainList()
BlockChainList.add_block('Udacitys')
BlockChainList.add_block('Algorithms')
BlockChainList.add_block('And')
BlockChainList.add_block('Datastructures')
BlockChainList.add_block('')

# Different input other than string
BlockChainList.add_block(5)

# No input
BlockChainList.add_block()

print(BlockChainList)

print('Size of the Block Chain is : ', BlockChainList.size())

# def test_function(test_case):
#   block_chain_list = test_case[0]
#   solution = test_case[1]
#   output = block_chain_list.size()
#   if solution == output:
#     print('Pass')
#   else:
#     print('Fail')

# test_function([BlockChainList, 4])
# #print('Size of the Block Chain is : ', BlockChainList.size())



