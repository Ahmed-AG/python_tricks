my_dict = {x: x**2 for x in range(10)}

for k, v in my_dict.items():
  print(k, v)

def fn_returning_list():
  return ('a', 'b', 'c')

a, b, c = fn()
print(a, b, c)

def foo(a, *args, **kwargs):
  print(f"a was {a} and the extra args were {args} and extra kwargs were {kwargs}")

print(foo('first'))
print(foo('first', 'second', 'third', one_kwarg="kwarg"))

.....