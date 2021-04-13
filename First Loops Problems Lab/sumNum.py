def sumNum(n):
    summed = 0
    for i in range(n):
        square = (i+1)**2
        summed += square
    return(summed)
squarePick = int(input("What number do you want to sum the squares of?"))

    
print("The sum of the squares from 1 to "+str(squarePick)+" is "+str(sumNum(squarePick)))
    
