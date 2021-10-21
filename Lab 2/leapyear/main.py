#LeapYearCalculator
import sys

def leapyearcalc(startyear, endyear):
    yearlist = []
    try:
        for year in range(startyear, endyear+1):
            if year%4==0:
                if (year % 100 == 0) and (year % 400 != 0):
                    pass
                else:
                    yearlist.append(year)
        return yearlist

    except:
        print("Loser")
        sys.exit()


def main():
    startyear = int(sys.argv[1])
    endyear = int(sys.argv[2])

    yearlist = leapyearcalc(startyear, endyear)

    print("The number of Leap Years is %d, the Leap Years are %s." % (len(yearlist), str(yearlist)))
main()