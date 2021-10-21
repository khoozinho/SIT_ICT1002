#SalaryCalc
import sys

def main():
    hours = int(sys.argv[1])
    normal = float(sys.argv[2])
    overtime = float(sys.argv[3])

    if hours <= 40:
        normalsalary = hours * normal
        extrasalary = 0
        totalsalary = normalsalary
    elif hours > 40 and hours < 168:
        normalsalary = (40 * normal)
        extrasalary = ((hours-40) * overtime)
        totalsalary = normalsalary + extrasalary
    elif hours > 168:
        print("Your input is invalid!")
        return

    print("Normal Salary:%.02f,"%normalsalary, "Extra Salary:%.02f,"%extrasalary, "Total Salary:%.02f"%totalsalary)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Don't scam!")
        sys.exit()
    main()
