# 1) Python Program to Convert Decimal to Binary Using Recursion 

def DtoB(x):
    if x<2:
        return x
    else:
        r = x%2
        x = int(x/2)
        return DtoB(x)*10+r

decimal = int(input("enter a decimal number :"))
binary = DtoB(decimal)
print("binary number is",binary)