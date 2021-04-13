def evenDigits(n):
    numEvens = 0
    for digit in str(n): #to make it so the for loop can go over each digit like a string, it may alreasdy do that but this feels smart
        if int(digit) % 2 == 0:
            numEvens += 1
    return(numEvens)
print("You have "+str(evenDigits(int(input("Enter a number"))))+" even digits in your number.")
