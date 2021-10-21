import sys
from functools import reduce

def scale(salesnumbers, factor):
    print("The scaled number is: " , (list(map(lambda x : x * factor, salesnumbers))))

def sort(salesnumbers):
    print("The sorted sales numbers are: " , list(sorted(salesnumbers, key=lambda x : x % 10)))

def goodsales(salesnumbers):
    print("The good sales numbers are: " , list(filter(lambda x : x > average, salesnumbers)))

# def userinput():
#     given = input("Enter a sequence of sales number:")
#     scale = input("Enter the scale factor: ")
#     salesnumbers = map(int, given.split(','))

salesnumbers = list(map(int, sys.argv[1].split(',')))
factor = int(sys.argv[2])

average = reduce(lambda x,y: (x + y), salesnumbers) / float(len(salesnumbers))

scale(salesnumbers, factor)
sort(salesnumbers)
goodsales(salesnumbers)