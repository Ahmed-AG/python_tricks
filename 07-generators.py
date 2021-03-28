#07-generators.py
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
#for v in new_range(0, 10, 1):
#  print(v)