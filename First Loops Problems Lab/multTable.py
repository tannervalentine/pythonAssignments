##def multTable(num):
##   for f in range(num): 
##        for i in range(num+1):
##            if i != 0:
##                print(str(int((f+1)*i)), end = " ")
##        print("\n")

def multTable(num):
   for rows in range(num):
      for i in range(1,num+1):
         print(str(int((rows+1)*i)), end = " "*(6-(len(str((rows+1)*i)))))
      print("\n")

multPick = int(input("What number would you like to see a table of?"))




multTable(multPick)
