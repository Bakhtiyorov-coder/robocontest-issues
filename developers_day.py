 #A0002


year = int(input("Year:  "))

is_leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if is_leap:
    print(f"12/09/{year:04d}")
else:
    print(f"13/09/{year:04d}")