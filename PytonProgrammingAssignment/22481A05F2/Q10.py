# 10) Recursive Python function to calculate sum of elements in a given nested list
# For example if Input is : [1, 2, [3,4],[5,6]] then output is 21

def sumlist(l):
    sum = 0
    for e in l :
        if type(e) == list:
            sum += sumlist(e)
        else:
            sum = sum + e
    return sum

data = [1, 2, [3,4],[5,6]]
sum = sumlist(data)
print('the sum of elements is',sum)