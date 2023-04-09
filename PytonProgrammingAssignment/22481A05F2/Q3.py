# 3) Python Program to generate Fibonacci Series Using Recursion.

# example series: 0 1 1 2 3 5 8 13 .. ..

def fibonacci(x,series = [0,1]):
    series.append(series[len(series)-1] + series[len(series)-2])
    if(len(series)>=x):
        return series
    return fibonacci(x,series)
    
number = int(input("enter a no of elements : "))
print("fibonacci series of",number,"elements :")
series = fibonacci(number)
for i in range(0,number):
    print(series[i],end=' ')
print('.....')
