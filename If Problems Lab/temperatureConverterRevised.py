eq = input("What would you like to convert to? (c/f)").lower()
temp = float(input("What is the starting temperature?"))

if eq == "f":
    newTemp = temp*(9/5)+32
    print("Your converted temperature is "+str(newTemp)+" degrees in "+eq+".")
elif eq == "c":
    newTemp = (temp-32)*(5/9)
    print("Your converted temperature is "+str(newTemp)+" degrees in "+eq+".")
else:
    print("Sorry! That's not a valid measurement to convert to.")
