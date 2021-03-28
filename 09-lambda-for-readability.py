# Basic Lambda
x = lambda a : a + 10
print(x(5))

# Lambda are anonymous function for quick operations
print(map(lambda x: x**2, [1,2,3]))

# You can use them to also improve readability
greater_than_5 = lambda x: x > 5
print(greater_than_5(10))

#my_dict = {'a': 1, 'b': 2}
#new_dict = {v: k for k, v in my_dict.items()}

#print(my_dict)
#print(new_dict)

#invert_dict = lambda d: {v: k for k, v in d.items()}
#new_dict = invert_dict(my_dict)

#print(my_dict)
#print(new_dict)
