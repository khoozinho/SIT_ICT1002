#BMICalc
import sys

def main():
    unit = sys.argv[1]
    height = float(sys.argv[2])
    weight = float(sys.argv[3])

    if unit == 'imperial':
        bmi = 703 * weight / (height * height)
    elif unit == 'metric':
        bmi = weight / (height * height)
    else:
        print("wts scammed!!!")
        return

    if bmi < 16:
        cat = 'Severe Thinness'
    elif bmi >= 16 and bmi <= 17:
        cat = 'Moderate Thinness'
    elif bmi > 17 and bmi <= 18.5:
        cat = 'Mild Thinness'
    elif bmi > 18.5 and bmi <= 25:
        cat = 'Normal'
    elif bmi > 25 and bmi <= 30:
        cat = 'Overweight'
    elif bmi > 30 and bmi <= 35:
        cat = 'Obese Class I'
    elif bmi > 35 and bmi <= 40:
        cat = 'Obese Class II'
    else:
        cat = 'Obese Class III'

    print("{:0.2f} {}".format(bmi, cat))


if __name__ == '__main__':
     if len(sys.argv) < 4:
         print("Your input is invalid!")
         sys.exit()
     main()

