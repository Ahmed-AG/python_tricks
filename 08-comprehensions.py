squares = []
for i in range(5):
  squares.append(i**2)


squares = [v ** 2 for v in range(5)]
print(squares)



str_to_int = {str(v): v for v in squares}
print(str_to_int)

letter_set = {c for c in "aabbcc"}
print(letter_set)


generator_comprehension = (v**2 for v in range(10))
print(generator_comprehension)


filtered_squares = [v**2 for v in range(10) if v < 8]
filtered_squares = [v for v in squares if v < 10]