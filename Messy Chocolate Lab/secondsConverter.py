secondsStart = float(input("How many seconds do you have?"))
hours = secondsStart//3600
minutes = (secondsStart%3600)//60
secondsEnd = (secondsStart%3600)%60
print("This is equal to "+str(hours)+" hours, "+str(minutes)+" minutes, and "+str(secondsEnd)+" seconds.")
