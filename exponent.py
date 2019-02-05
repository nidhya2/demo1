number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The Result of {2} Power {2} = {4}".format(number, exponent, power))
