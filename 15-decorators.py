def square(x):
  return x ** 2

def print_square(x):
  print(f"Calling fn with {x}")
  return square(x)

response = print_square(5)
print(response)

# Section2

def print_arg(fn):
  def print_fn(x):
    print(f'Calling fn with {x}')
    return fn(x)
  return print_fn

print_square2 = print_arg(square)
print_cube = print_arg(lambda x: x**3)
print(print_square2(5))
print(print_cube(5))


# Section 3
#@print_arg
#def square(x):
#  return x ** 2

#print(square(5))