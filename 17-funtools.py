#https://docs.python.org/3/library/functools.html

from functools import lru_cache, partial

#lru_cache: Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

#@lru_cache()
def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

print(fib(20))

#@lru_cache()
#def fib(n):
#  if n == 1 or n == 2:
#    return 1
#  else:
#    return fib(n - 1) + fib(n - 2)

#fib(200)

#Partial: Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords.

def add(a, b):
  return a + b

add_5 = partial(add, 5)
print(add_5(10))