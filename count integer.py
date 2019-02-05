
Number = int(input("Please Enter any value: "))
Count = 0
while(Number > 0):
    Number = Number // 10
    Count = Count + 1

print("\n Number of Digits in a Given value = %d" %Count)
