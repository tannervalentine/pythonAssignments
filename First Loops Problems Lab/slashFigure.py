def art(n):
    for i in range(n):
        print(i*"\\\\", end = "")
        print(((4*n)-(i*4)-2)*"!", end = "")
        print(i*"//", end = "")
        print("")
slashPick = int(input("What number for the slash figure?"))      
art(slashPick)       
