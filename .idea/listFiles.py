import os

print(("The files and folders in {} are:".format(os.getcwd())))
items = os.listdir('.')
for item in items:
    print(item)

"""
1.     When will a ValueError occur?
    When the user input string instead of integer
2.     When will a ZeroDivisionError occur?
    When user input 0 in denominator
3.   Could you change the code to avoid the possibility of a ZeroDivisionError?
    Many ways can be used to avoid the possibility of a ZeroDivisionError, for example: while loop.
"""