squares = []
for i in range(5):
  squares.append(i**2)
print(squares)

squares = [v ** 2 for v in range(5)]
print(squares)

#dict
str_to_int = {str(v): v for v in squares}
print(str_to_int)


generator_comprehension = (v**2 for v in range(10))
print(generator_comprehension)
#for item in generator_comprehension:
#  print(item)


filtered_squares = [v**2 for v in range(10) if v < 8]
print(filtered_squares)

filtered_squares = [v for v in squares if v < 10]
print(filtered_squares)
