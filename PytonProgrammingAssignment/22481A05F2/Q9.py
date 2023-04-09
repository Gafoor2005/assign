# 9) Recursive Python function to check if a string is palindrome

def palindrome(string,n = None):
    if n==None:
        n = int(len(string)/2)
    if n<0:
        return 1
    if string[n] == string[len(string)-1-n]:
        return palindrome(string,n-1)
    return 0

string = input('enter a string ')
if palindrome(string.lower()):
    print('it is palindrome')
else:
    print('it is not palindrome')