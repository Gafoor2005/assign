# 8) Write a python program to accept a string from a user and re-display the same after removing vowels from it. 

string = input('enter a string ')
ovels = 'aeiouAEIOU'
ovels = list(ovels)
for e in ovels:
    string = string.replace(e,"")
print(string)