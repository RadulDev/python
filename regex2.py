import re

string = "Python is a programming language"

match = re.search('\APython', string)

if match:
  print(f"{match} pattern found inside the string")
else:
  print("pattern not found")  

