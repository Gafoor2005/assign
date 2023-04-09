# 2) Python Program to check a given number is prime or not Using Recursion.

def prime(x,i = 2):
    if (x < 2):
        return 0
    if (i>=x):
        return 1
    if ( not x%i):  # if x is not prime then true
        return (x%i)  # returns 0 if x is not prime
    i = i + 1
    return prime(x,i)

number = int(input("enter a number :"))
if prime(number):
    print('the number is prime')
else:
    print('the number is not prime')