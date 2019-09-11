# Finding Files -
# For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

# Here is an example of a test directory listing, which can be downloaded here:

# ./testdir
# ./testdir/subdir1
# ./testdir/subdir1/a.c
# ./testdir/subdir1/a.h
# ./testdir/subdir2
# ./testdir/subdir2/.gitkeep
# ./testdir/subdir3
# ./testdir/subdir3/subsubdir1
# ./testdir/subdir3/subsubdir1/b.c
# ./testdir/subdir3/subsubdir1/b.h
# ./testdir/subdir4
# ./testdir/subdir4/.gitkeep
# ./testdir/subdir5
# ./testdir/subdir5/a.c
# ./testdir/subdir5/a.h
# ./testdir/t1.c
# ./testdir/t1.h


# Python's os module will be useful—in particular, you may want to use the following resources:

# os.path.isdir(path)
# https://docs.python.org/3.7/library/os.path.html#os.path.isdir

# os.path.isfile(path)
# https://docs.python.org/3.7/library/os.path.html#os.path.isfile

# os.listdir(directory)
# https://docs.python.org/3.7/library/os.html#os.listdir

# os.path.join(...)
# https://docs.python.org/3.7/library/os.path.html#os.path.join

# Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().

# Here is some code for the function to get you started:

#def find_files(suffix, path):
   # """
   # Find all files beneath path with file name suffix.

   # Note that a path may contain further subdirectories
   # and those subdirectories may also contain further subdirectories.

   # There are no limit to the depth of the subdirectories can be.

   # Args:
   #   suffix(str): suffix if the file name to be found
   #   path(str): path of the file system

   # Returns:
   #    a list of paths
   # """
#    return None

# recursion - space complexity
# https://www.ideserve.co.in/learn/time-and-space-complexity-of-recursive-algorithms

# OS Module Exploration Code :

# Code to demonstrate the use of some of the OS modules in python

import os

# # Let us print the files in the directory in which you are running this script
# print (os.listdir("."))

# # Let us check if this file is indeed a file!
#print (os.path.isfile("LRU_cache_1.py"))
#print (os.path.isfile("t1.c"))

# print (os.path.isdir("./LRU_cache_1.py"))

# # Does the file end with .py?
# print ('file end with .py? ', "./LRU_cache_1.py".endswith(".py"))

# print ('project2 is a dir : ',os.path.isdir('/Users/bsameera/Documents/Udacity_Nano_Degree/project2'))

# print ('LRU_cache_1.py is a file : ',os.path.isfile('/Users/bsameera/Documents/Udacity_Nano_Degree/project2/LRU_cache_1.py'))
# print ('LRU_cache_1.py is a dir : ',os.path.isdir('/Users/bsameera/Documents/Udacity_Nano_Degree/project2/LRU_cache_1.py'))

#print(os.path.splitext("LRU_cache_1.py"))       # '.py'
#print(os.path.splitext('.DS_Store'))

# To flatten the nested list
def flatten_list(l):
  output = []
  def remove_nestings(l):
    for i in l:
      if type(i) == list:
        remove_nestings(i)
      else:
        output.append(i)
    return output
  return remove_nestings(l)

def find_files(suffix=None, path=None):
  if suffix == None or path == None:
    return None
  files = []
  file_list = os.listdir(path)
  #print(file_list)           # ['.DS_Store', 'subdir1', 'subdir2', 'subdir3', 'subdir4', 'subdir5', 't1.c', 't1.h']
  for file in file_list:
    file = path+'/'+file
    if os.path.isdir(file):
      files.append(find_files(suffix, file))
    elif os.path.isfile(file):
      last_two_chars = file[-2:]
      if last_two_chars == suffix:
        files.append(file)
  return files

# def test_function(test_case):
#   if len(test_case) == 1:
#     suffix = None
#     path = None
#     solution = test_case[0]
#     output = find_files(suffix, path)
#   elif len(test_case) == 2:
#     suffix = test_case[0]
#     path = None
#     solution = test_case[1]
#     output = find_files(suffix, path)
#   elif len(test_case) == 3:
#     suffix = test_case[0]
#     path = test_case[1]
#     solution = test_case[2]
#     output = flatten_list(find_files(suffix, path))
#   if output == solution:
#     print("Pass")
#   else:
#     print("Fail")

# testcases :

# Normal case :

print('path is ./testdirectory and files to be found with suffix .c : ')
print(flatten_list(find_files('.c', './testdirectory')))
# returns ['./testdirectory/subdir1/a.c', './testdirectory/subdir3/subsubdir1/b.c', './testdirectory/subdir5/a.c', './testdirectory/t1.c']

# When no path is passed and the first argument, suffix is given
print('When no path is passed and the first argument, suffix is given : ', find_files('.py'))

# When no suffix and path are passed
print('path and suffix are not given : ', find_files())


