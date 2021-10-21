# import sys
#
# value = int(sys.argv[1])
# if value < 0:
#     sys.exit()
#
# def digit(x):
#     if x < 10:
#         return 1
#     else:
#         return 1 + digit(x/10)
#
# def digit_iterative(x):
#     count = 1
#     while (x > 10):
#         x = x/10
#         count = count + 1
#     return count
#
# recurse = digit(value)
# iterative = digit_iterative(value)
# print("The number of digit(s) calculated by recursive is %d and by iterative is %d" %(recurse, iterative))

print(int(2*'2')//7)