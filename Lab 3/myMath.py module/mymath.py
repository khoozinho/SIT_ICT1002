from functools import reduce

def add(x,y):
    result = x + y
    return result

def subtraction(x,y):
    result  = x - y
    return result

def evenNum(x):
    result = []
    for number in x:
        if (number % 2 == 0):
            result.append(number)
    return result

def maximum(x):
    result = sorted(x, reverse = True)[0]
    return result

def minimum(x):
    result = sorted(x)[0]
    return result

def absolute(x):
    result = abs(x)
    return result

def sumTotal(x):
    total = reduce(add,x)
    return total

def clear(x):
    result = [] * len(x)
    return result