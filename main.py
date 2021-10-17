import math

active = True

while active:
    print("1) Add")
    print()
    print("0) Exit")

    try:
        answer = int(input("Option: "))
        print()

        if answer == 1:
            first = input("First Number: ")
            second = input("Second Number: ")
            final = float(first) + float(second)
            print("Answer:", float(final))
            print()
        elif answer == 0:
            active = False
        else:
            print()
            print("Please select a valid option number")
            print()
    except Exception:
        print()
        print("NameError: Please Use Numbers Only")
        print()
