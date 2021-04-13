date = input("Please enter a valid date (MM/DD/YYYY): ")
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:10])

if month==4 or month==6 or month==11 or month==9:
    if 1 <= day <= 30:
        print("This is a valid date")
    else:
        print(str(day)+" is not valid for month "+str(month))
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    if 1 <= day <= 31:
        print("This is a valid date")
    else:
        print(str(day)+" is not valid for month "+str(month))
elif month==2:
    if day < 1 or day > 29:
        print(str(day)+" is not valid for month "+str(month))
    elif day == 29:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("This is a valid date")
                else:
                    print("29 is not a valid day on non leap years")
            else:
                print("This is a valid date")
        else:
            print("29 is not a valid day on non leap years")
    else:
        print("This is a valid date")
else:
    print("This date is invalid")
