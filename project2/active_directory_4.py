# Active Directory

# In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

class Group(object):
  def __init__(self, _name):
    self.name = _name
    self.groups = []
    self.users = []

  def add_group(self, group):
    self.groups.append(group)

  def add_user(self, user):
    self.users.append(user)

  def get_groups(self):
    return self.groups

  def get_users(self):
    return self.users

  def get_name(self):
    return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child_user = "child_user"
child.add_user(child_user)

child.add_group(sub_child)
parent.add_group(child)

#Write a function that provides an efficient look up of whether the user is in a group.

# _single_leading_underscore
# This convention is used for declaring private variables, functions, methods and classes in a module. Anything with this convention are ignored in from module import *.
# https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc

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

def is_user_in_group(user=None, group=None):
  # """
  # Return True if user is in the group, False otherwise.

  # Args:
  #   user(str): user name/id
  #   group(class:Group): group to check user membership against
  # """
  # If group or user and group, both are not given
  if user == None or group == None:
    return ('user or group information not provided')
  if user in group.get_users():
    return True
  else:
    groups_list = []
    def g(group):
      groups = group.get_groups()
      for group in groups:
        groups_list.append(group)
        if len(group.get_groups())>0:
          g(group)
    g(group)

    users_list = []
    for group in groups_list:
      if len(group.get_users()) > 0:
        users_list.append(group.get_users())

    # flatten users_list and return true if user in users_list
    users_list_flattened = flatten_list(users_list)

    if user in users_list_flattened:
      return True
    else:
      return False

# def test_function(test_case):
#   if len(test_case) == 2:
#     user = test_case[0]
#     group = None
#     solution = test_case[1]
#     output = is_user_in_group(user, group)
#   elif len(test_case) == 1:
#     user = None
#     group = None
#     solution = test_case[0]
#     output = is_user_in_group(user, group)
#   #if len(test_case) == 3
#   else:
#     user = test_case[0]
#     group = test_case[1]
#     solution = test_case[2]
#     output = is_user_in_group(user, group)
#   if solution == output:
#     print('Pass')
#   else:
#     print('Fail')

print("Check if sub_child_user is in the parent group or it's children :")
print('Output : ', is_user_in_group(sub_child_user, parent))              # True

print("Check if sub_child_user is in child group or it's children :")
print('Output : ', is_user_in_group(sub_child_user, child))              # True

print("Check if sub_child_user is in sub_child group or it's children :")
print('Output : ', is_user_in_group(sub_child_user, sub_child))           # True

print("Check if child_user is in child group or it's children :")
print('Output : ', is_user_in_group(child_user, child))                  # True

print("Check if child_user is in sub_child group or it's children :")
print('Output : ', is_user_in_group(child_user, sub_child))             # False

print("Check if child_user is in parent group or it's children :")
print('Output : ', is_user_in_group(child_user, parent))            # True

print("Only username is provided, not the group name :")
print('Output : ', is_user_in_group(child_user))                   # user or group information not provided

print("username and the group name are not given as arguments :")
print('Output : ', is_user_in_group())                   # user or group information not provided

# # # parent_user does not exist
# # #print(is_user_in_group(parent_user, parent))
# SUGGESTION
# You can handle this case using try and except block like:

# # parent_user does not exist
# try:
#   print(is_user_in_group(parent_user, parent))
# except NameError:
#   print("user does not exist!")
# Refer to this for more on this concept, it's pretty interesting.

