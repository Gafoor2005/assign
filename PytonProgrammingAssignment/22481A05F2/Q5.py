# 5) Python Program to Compute exponent of a given number Using Recursion

def power(base,exponent):
    if exponent:
        return base*power(base,exponent-1)
    return 1

base = int(input('enter base '))
exponent = int(input('enter exponent '))

result =  power(base,exponent)
print("the result is ",result)