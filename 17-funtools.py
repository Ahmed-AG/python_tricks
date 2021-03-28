from functools import lru_cache, partial

def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

fib(20)


@lru_cache()
def fib(n):
  if n == 1 or n == 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

fib(200)


def add(a, b):
  return a + b

add_5 = partial(add, 5)
add_5(10)