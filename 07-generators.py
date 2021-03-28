# Generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory. For an overview of iterators in Python, take a look at Python “for” Loops (Definite Iteration).
# https://realpython.com/introduction-to-python-generators/
 
def old_range(start, stop, step):
  l = []
  i = start
  while i < stop:
    l.append(i)
    i += step
  return l

def new_range(start, stop, step):
  i = start
  while i < stop:
    yield i
    i += step

print(old_range(0, 10, 1))

print(new_range(0, 10, 1))
for v in new_range(0, 10, 1):
  print(v)