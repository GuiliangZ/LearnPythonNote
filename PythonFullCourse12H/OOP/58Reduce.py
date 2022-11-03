# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            Performs function on first two elements and repeats process until 1 value remains
# 
# reduce(function, iterables)
# 

import functools
from math import factorial

letters = ["H", "E", "L", "L", "O"]
word = functools.reduce(lambda x, y : x + y, letters)
print(word)

factorial_x = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x * y, factorial_x)
print(result)











