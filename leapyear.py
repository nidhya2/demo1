
year = int(input("Enter value: "))


if year % 4 == 0 and year % 100 != 0:
    print(value, "is a Leap Year")
elif year % 100 == 0:
    print(value, "is not a Leap Year")
elif year % 400 ==0:
    print(value, "is a Leap Year")
else:
    print(value, "is not a Leap Year")
