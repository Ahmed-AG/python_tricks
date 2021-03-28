print("With range")
x = ['a', 'b', 'c']
for i in range(len(x)):
  v = x[i]
  print(i, v)

print("With enumerate")
for i, v in enumerate(x):
  print(i, v)