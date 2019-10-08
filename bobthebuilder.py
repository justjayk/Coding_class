"""
Environment Diagrams: Draw out the environment diagrams for the code below.
What do you think they'll output?
"""
# Question 1. Solution: https://goo.gl/rZnzaM
def dessef(a, b):
    c = a + b
    b = b + 1
    return c + b

b = 6
dessef(b, 4)

# Question 2. Solution:  https://goo.gl/7Kcx6n
def foo(x, y):
    foo = bar
    return foo(bar(x, x), y)
def bar(z, x):
    return z + y

y = 5
foo(1, 2)


"""
Higher Order Functions: Lambda Expressions & Their Usage as a Key
Usages in: Min, Max, Maps, List Comprehensions, and more!
Calling min on a collection of elements will return the collection's smallest
element. min(letters) will return 'a' (the smallest key). min can also take an
optional 2nd argument: a one-argument key function.
"""
# Exercise

"""
dictionary_name.get('key_name')
dictionary_name['key_name']
both return coresponding value in list.
"""

letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """

    return min(d, key = lambda x: d.get(x)) # Your solution here
print(key_of_min_value(letters))
"""
List Comprehensions
Powerful way of creating new lists out of sequences. The syntax is:
[<expression> for <element> in <sequence> if <conditional>]
The if statement is optional.
Ex: [i**2 for i in [1, 2, 3, 4]] ---> [1, 4, 9, 16]
"""
# Exercise
nat_nums = range(20)
odd_nums = [i for i in nat_nums if i%2 == 1]


# Notes
