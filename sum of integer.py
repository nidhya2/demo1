n = input ("Enter number to calculate sum")
    n = int (n)
    average = 0
    sum = 0
    for num in range (0,n+1,-1):
        sum = sum+num
    print("sum of first", n,"value is:",sum)
