<<<<<<< testbranch
#!/usr/bin/python -tt
import unittest
# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  nums = set(nums)
  return list(nums)


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
print("test github")
def linear_merge(list1, list2):
    lists = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            lists.append(list1.pop(0))
        else:
            lists.append(list2.pop(0))
    lists.extend(list1)
    lists.extend(list2)
    return lists

print("test github")

import list1
print(list1)

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
#def test(got, expected):
#  if got == expected:
#    prefix = ' OK '
#  else:
#    prefix = '  X '
#  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
class tests(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


    if __name__ == '__main__':
        unittest.main()
=======
#!/usr/bin/python -tt
import unittest
# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  nums = set(nums)
  return list(nums)

print("test second branch")
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
print("test github")
def linear_merge(list1, list2):
    lists = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            lists.append(list1.pop(0))
        else:
            lists.append(list2.pop(0))
    lists.extend(list1)
    lists.extend(list2)
    return lists

print("test github")

import list1
print(list1)

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
#def test(got, expected):
#  if got == expected:
#    prefix = ' OK '
#  else:
#    prefix = '  X '
#  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
class tests(unittest.TestCase):
    def test_remove_adjacent(self):
        self.assertEqual(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
        self.assertEqual(remove_adjacent([]), [])

    def test_linear_merge(self):
        self.assertEqual(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
        self.assertEqual(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


    if __name__ == '__main__':
        unittest.main()
>>>>>>> adc7365 changes in list1
