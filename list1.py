<<<<<<< HEAD
#!/usr/bin/python -tt
from operator import itemgetter
import unittest
from list2 import remove_adjacent
import numpy as np

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
=======
<<<<<<< testbranch
#!/usr/bin/python -tt
from operator import itemgetter
import unittest
# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
>>>>>>> refs/remotes/origin/testbranch
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
print("test github")

print("let's find out what it happens!!")
list_numbers = []
for n in range(10):
    list_numbers.append(n)

sum_list = np.sum(list_numbers)

print(sum_list)
def match_ends(words):
    count = 0
    for word in words :
        if len(word) >= 2 and word[0]==word[-1]:
            count += 1
    return count

print(remove_adjacent([1,2,3,3,5,5,5,6]))
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    word_x = []
    word_notx = []
    all_words = []
    for word in words:
        if word.startswith('x'):
            word_x.append(word)
        else:
            word_notx.append(word)
    all_words = sorted(word_x) + sorted(word_notx)
    return all_words

print("test second branch")

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
#def test(got, expected):
#  if got == expected:
#    prefix = ' OK '
#  else:
#    prefix = '  X '
#  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


print("new test")

def match_ends(words):
    count = 0
    for word in words :
        if len(word) >= 2 and word[0]==word[-1]:
            count += 1
    return count


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    word_x = []
    word_notx = []
    all_words = []
    for word in words:
        if word.startswith('x'):
            word_x.append(word)
        else:
            word_notx.append(word)
    all_words = sorted(word_x) + sorted(word_notx)
    return all_words

print("test second branch")

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))


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
    def test_match_ends(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]),
           [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]),
           [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
           [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
      

    if __name__ == '__main__':
        unittest.main()

print("new test to cherry pick")

<<<<<<< HEAD
# and last chars of the string are the same.

print("new test")

def match_ends(words):
    count = 0
    for word in words :
        if len(word) >= 2 and word[0]==word[-1]:
            count += 1
    return count


print("test second branch")
=======
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    word_x = []
    word_notx = []
    all_words = []
    for word in words:
        if word.startswith('x'):
            word_x.append(word)
        else:
            word_notx.append(word)
    all_words = sorted(word_x) + sorted(word_notx)
    return all_words



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))


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
    def test_match_ends(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]),
           [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]),
           [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
           [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
      

    if __name__ == '__main__':
        unittest.main()
=======
#!/usr/bin/python -tt
from operator import itemgetter
import unittest
from list2 import remove_adjacent
# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
print("test github")
def match_ends(words):
    count = 0
    for word in words :
        if len(word) >= 2 and word[0]==word[-1]:
            count += 1
    return count

print(remove_adjacent([1,2,3,3,5,5,5,6]))
# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    word_x = []
    word_notx = []
    all_words = []
    for word in words:
        if word.startswith('x'):
            word_x.append(word)
        else:
            word_notx.append(word)
    all_words = sorted(word_x) + sorted(word_notx)
    return all_words

print("test second branch")

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    return sorted(tuples, key=itemgetter(-1))


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
    def test_match_ends(self):
        self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
        self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
        self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    def test_front_x(self):
        self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
        self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
        self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

    def test_sort_last(self):
        self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]),
           [(2, 1), (3, 2), (1, 3)])
        self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]),
           [(3, 1), (1, 2), (2, 3)])
        self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
           [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
      

    if __name__ == '__main__':
        unittest.main()
>>>>>>> adc7365 changes in list1
            
>>>>>>> refs/remotes/origin/testbranch
