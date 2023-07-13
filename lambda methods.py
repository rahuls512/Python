#Lambda functions can be used in various Python methods such as filter(), map(), and reduce().
# These methods take a function as an argument and can be replaced with lambda functions.

#filter():
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, my_list))
print(even_numbers) # Output: [2, 4, 6, 8, 10]

#map():
my_list = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, my_list))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]

#reduce():
from functools import reduce
my_list = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, my_list)
print(product) # Output: 120
