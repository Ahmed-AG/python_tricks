def treat_as_iterable(iterable_var):
  print(iterable_var)
  first_pass = []
  for v in iterable_var:
    first_pass.append(v)
  print("\tFirst Pass", first_pass)
  print("\tSecond pass", [v for v in iterable_var])
  print()


#lists_exist = [1, 2, 3]
#treat_as_iterable(lists_exist)

#range_generates = range(5)
#treat_as_iterable(range_generates)

#reverse_generates = reversed(range(10))
#treat_as_iterable(reverse_generates)

#map_generates = map(lambda x: x**2, range(5))
#treat_as_iterable(map_generates)

#zip_generates = zip(range(5), range(5, 10))
#treat_as_iterable(zip_generates)

#comprehensions_exist = [x for x in zip(range(5), range(5, 10))]
#treat_as_iterable(comprehensions_exist)

#Example 2:

#items = [ "one","two","three","four" ]
#iterator = iter(items)
#print(iterator)
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))
#print(next(iterator))