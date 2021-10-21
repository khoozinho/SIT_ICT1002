#EvenOddCalculator
import sys

def main():
    inputstring = sys.argv[1]
    evenoddcalc(inputstring)

def evenoddcalc(string):
    splitstring = string.split(",")
    evensum = 0
    oddsum = 0
    numberlist = []
    evenlist = []
    oddlist = []

    try:
        for number in splitstring:
            number = int(number)
            numberlist.append(number)
            if number % 2 == 0:
                evenlist.append(number)
                evensum = evensum + number
            else:
                oddlist.append(number)
                oddsum = oddsum + number

        minnumber = min(numberlist)
        maxnumber = max(numberlist)

        difference = maxnumber - minnumber

        numberlist.remove(minnumber)
        numberlist.remove(maxnumber)

        avg = sum(numberlist)/len(numberlist)

        output = "The sum of all even numbers is %d, the sum of all odd numbers is %d, the difference between the biggest and smallest number is %d, the total number of even numbers is %d, the total number of odd numbers is %d, the centered average is %d."
        print(output % (evensum, oddsum, difference, len(evenlist), len(oddlist), avg))

    except:
         print("Please enter valid integers.")
         sys.exit()

main()