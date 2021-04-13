def riddler():
    for num in range(1000,10000):
        a,b,c,d = str(num)
        if int(a)!=int(b) and int(a)!=int(c) and int(a)!=int(d) and int(b)!=int(c) and int(b)!=int(d) and int(c)!=int(d):
            if int(a) == 3*int(c):
                if num % 2 == 1:
                    if int(a)+int(b)+int(c)+int(d) == 27:
                        return(num)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
print("The next caper is on "+str(riddler())+" Pennsylvania Ave.")
