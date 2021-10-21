import sys
import mymath

inputstring = sys.argv[1]
stringlist = inputstring.split(',')
numberlist = []
for i in stringlist:
    numberlist.append(int(i))

biggestnum = mymath.maximum(numberlist)
smallestnum = mymath.minimum(numberlist)

difference = mymath.subtraction(biggestnum, smallestnum)
summation = mymath.add(biggestnum, smallestnum)
inputlisttotal = mymath.sumTotal(numberlist)
evennumbers = len(mymath.evenNum(numberlist))

if smallestnum < 5:
    numberlist = mymath.clear(numberlist)

print("The difference is:",difference,"The summation is:",summation, "The summation of all inputs is:",inputlisttotal, "The number of even numbers is:",evennumbers, "The values in the list are:", numberlist)