def beerSong(beers):
    for i in range(beers):
        print(str(beers-i)+" bottles of beer on the wall, "+str(beers-i)+" bottles of beer \n Take one down, pass it around, "+str(beers-i-1)+" bottles of beer on the wall")
beerPick = int(input("How many bottles of beer? (1-99)"))

if beerPick <= 99:
    beerSong(beerPick)
else:
    print("Sorry! That's too many bottles to count.")
        
