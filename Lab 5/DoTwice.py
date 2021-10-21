import sys

def double(x):
    return 2*x

def square(x):
    return x*x

def cube(x):
    return x*x*x

number = int(sys.argv[1])
operator = int(sys.argv[2])

if operator == 1:
    print(double(double(number)))

elif operator == 2:
    print(square(square(number)))

elif operator == 3:
    print(cube(cube(number)))

else:
    print("It cannot be supported!")