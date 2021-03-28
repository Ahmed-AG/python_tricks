#def foo():
#    return True

try:
  foo() 
except (Exception, RuntimeError): 
  print("Exception occured")
except OSError as e:
  print(e)
else:
  print("Exception didnt occur")
finally:
  print("Always gets here")

