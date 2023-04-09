# 7)Write about Documentation string with example program 

# the documentation string is a string which contains a non executable part of code or comments, it starts and ends with 3 sigle/double quotations 

# we can use this to maintain documentaion in our code 
# we can use this as multi line comment 

# syntax:

'''hello'''
"""hello"""

"""
this is 
multi line
"""

'''
this is 
multi line
'''
print(__doc__) # __doc__ is a documentation string. 

#------------printing documentaion string of a function -------------------
def func():
    '''
    this is inside
    a function
    '''
    print("this is a function")

print(func.__doc__) # func.__doc__ is a documentation string inside func().