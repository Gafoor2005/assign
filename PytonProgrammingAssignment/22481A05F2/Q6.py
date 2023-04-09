# 6) Python Program to Compute length of a given string Using Recursion

def length(string):
    if type(string)==str:
        string = list(string)
    
    try:
        string.pop()
        return 1+length(string)
    except:
        return 0

string = input('enter a string : ')
print('length of string is '+str(length(string)))