# Regular Expressions
# https://www.py4e.com/lessons/regex
import re
string="Python is fun"
s=re.search('Python',string)
print(s)


import re
txt="The rain in banglore"
x=re.findall("[a-z]",txt)
print(x)