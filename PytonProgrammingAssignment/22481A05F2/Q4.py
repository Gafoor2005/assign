# 4.) Python Program to Compute GCD of two numbers Using Recursion.

def GCD(num1,num2,i = None):
    num = min(num1,num2) 
    if i == None:
        i = num
    r = num%i
    if not r:
        if not max(num1,num2)%i:
            return i
    return GCD(num1,num2,i-1)

number1 = int(input("enter a number :"))
number2 = int(input("enter another number :"))
print(f'the GCD of {number1} and {number2} is {GCD(number1,number2)}')