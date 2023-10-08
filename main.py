import math
num11 = 0
num22 = 0

def initnum(num):
    while True:
        try:
            num = int(input("Give a number: "))
        except ValueError:
            print("This input is invalid.")
        else:
            return num


def main():
    print("Calculator")
    num1 = initnum(num11)
    num2 = initnum(num22)
    while True:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
        print("Current numbers: ", num1, num2)
        selec = int(input("Please select something (1-6): "))
        if selec == 1:
            print("The result is: ", (num1 + num2))
            continue
        elif selec == 2:
            print("The result is: ", (num1 - num2))
            continue
        elif selec == 3:
            print("The result is: ", (num1 * num2))
            continue
        elif selec == 4:
            print("The result is: ", (num1 / num2))
            continue
        elif selec == 5:
            ssin = math.sin((num1 / num2))
            print("The result is: ", ssin)
        elif selec == 6:
            ccos = math.cos((num1 / num2))
            print("The result is: ", ccos)
        elif selec == 7:
            num1 = initnum(num1)
            num2 = initnum(num2)
            continue
        elif selec == 8:
            print("Thank you!")
            break
        elif selec != 1 and selec != 2 and selec != 3 and selec != 4:
            print("Selection was not correct.")
            continue


if __name__ == "__main__":
    main()