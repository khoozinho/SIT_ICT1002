# using a for loop
import sys

def sum_recursive(x):
    if x == 0:
        return x
    else:
        return x + sum_recursive(x-1)

def sum_iterative(x):
    result = 0
    for i in range(1, x + 1):
        result += i

    return result

value = int(sys.argv[1])
recursive = sum_recursive(value)
iterative = sum_iterative(value)

output = "The SUM value calculated by recursive is %d and by iterative is %d." %(recursive, iterative)
print(output)

