# 13) Write a function to take a string (A string will be given combination of letters and special characters). You have to return a reversed string keeping the special characters at the same place

# Example input : sd&hg#j
# Output to be returned is : jg&hd#s 

def func(s):
    li = list(s)
    li.reverse()
    i = 0
    for e in li:
        if not e.isalpha():
            li.pop(i)
        i += 1
    i = 0
    a = []
    a.append(list(s))
    for e2 in a:
        e2 = 'f'
        print(e2)
    print(a)

string = input("enter a string ")
# func(string)
li = ['f','h','g']
for e in li:
    e = 'k'
print(li)
