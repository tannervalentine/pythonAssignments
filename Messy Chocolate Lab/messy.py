def main():
    print("It’s time to go on a scavenger hunt!")
    print("You'd be amazed how many things can go wrong!")
    initialPos = 7.0
    time  = float(input("Please enter how long you want to travel for:"))
    velocity =  5.0
    acceleration = 1.0
    position =  initialPos + velocity * time + (1 / 2) *acceleration*time*time
    print("Your new position is "+str(position)+".")
main()
