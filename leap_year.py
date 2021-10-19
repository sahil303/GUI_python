while True:
    n = int(input("\nEnter year : "))
    m = int(input("Enter month : "))
    leap = 0
    if n%400 == 0:
        print("It is a leap year")
        leap = 1
    elif n%4 == 0:
        print("It is a leap year")
        leap = 1
    else:
       print("It is a leap year")

    month_days = [1,3,5,7,8,10,12]
    if m in month_days:
        days = 31
    else:
        if m == 2:
            if leap == 1:
                days = 29
            else:
                days = 28
        else:
            days = 30
    print("Number of days in the month is : ", days)
    a = str(input("\n Do you want to Continue (Y/n) : "))
    if a == 'Y' or a == 'y':
        continue
    else:
        break
