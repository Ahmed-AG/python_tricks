file_pointer = open("sample_file.txt")
r = file_pointer.read()
file_pointer.close()
print(r)

with open("sample_file.txt") as file_pointer:
  r = file_pointer.read()
  print(r)
#automatically closes