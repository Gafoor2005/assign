# 12) Write a function to take a string and Reverse a string after removing Duplicates characters in it

def reverse(s):
    s = list(s)
    s.reverse()
    result = ""
    for e in s:
        if e not in result:
            result += e 
    return result
string = input("enter a string ")
r = reverse(string)
print("result is",r)