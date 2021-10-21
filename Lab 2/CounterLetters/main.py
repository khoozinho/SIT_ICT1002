import sys

# This is for Step 1.
# string = sys.argv[1]

# def letter_count(string):
#     letterdict1 = {}
#     for char in string:
#         if char in letterdict1.keys():
#             letterdict1[char] += 1
#         else:
#             letterdict1[char] = 1
#     return letterdict1
# output = letter_count(string)
# print(output)

# This is for Step 2.
# string = sys.argv[1]
# string = string.split(",")
#
# def double_count(string1, string2):
#     letterdict2 = {}
#     lst = [string1, string2]
#     for word in lst:
#         for char in word:
#             if char in letterdict2.keys():
#                     letterdict2[char] += 1
#             else:
#                 letterdict2[char] = 1
#     return letterdict2
#
# output = double_count(string[0], string[1])
# print(output)

# This is for Step 3 and 4
string = sys.argv[1]
string = string.replace(",","")

def various_count(*string):
    letterdict3 = {}
    for word in string:
        for char in word:
            if char in letterdict3.keys():
                letterdict3[char] += 1
            else:
                 letterdict3[char] = 1
    return letterdict3

output = various_count(string)

sorted_total = sorted(output.items(), key=lambda item:item[0], reverse=True)

for item in sorted_total:
    print('%s:%d' % (item[0],item[1]), end=' ')