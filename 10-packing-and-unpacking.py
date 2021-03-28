# example 1

my_dict = {x: x**2 for x in range(10)}

for k, v in my_dict.items():
  print(k, v)

# example 2

def fn_returning_list():
  return ('a', 'b', 'c')

#a, b, c = fn_returning_list()
#print(a, b, c)

# example 3

#def bar(a, b, c, k1=None, k2=None, k3=None):
#  print(a, b, c, k1, k2, k3)

#args = [1, 2, 3]
#kwargs = { "k1": 4 }

#bar(*args, **kwargs)