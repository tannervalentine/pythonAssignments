#whoever reads this i know this is overcomplicated that's how it worked in my BRAIN
int1 = int(input("Enter an integer."))
int2 = int(input("Please enter another."))
int3 = int(input("Please enter one more integer."))

if int1<=int2 and int1<=int3:
    sort1 = int1
elif int2<=int1 and int2<=int3:
    sort1 = int2
elif int3<=int1 and int3<=int2:
    sort1 = int3

if sort1 == int1:
    if int2<=int3:
        sort2 = int2
    else:
        sort2 = int3
elif sort1 == int2:
    if int1<=int3:
        sort2 = int1
    else:
        sort2 = int3
elif sort1 == int3:
    if int1<=int2:
        sort2 = int1
    else:
        sort2 = int2

if sort1 == int1 and sort2 == int2:
    sort3 = int3
elif sort1 == int2 and sort2 == int3:
    sort3 = int1
elif sort1 == int3 and sort2 == int1:
    sort3 = int2
elif sort1 == int1 and sort2 == int3:
    sort3 = int2
elif sort1 == int2 and sort2 == int1:
    sort3 = int3
elif sort1 == int3 and sort2 == int2:
    sort3 = int1

print("Your integers in ascending order are "+str(sort1)+", "+str(sort2)+", "+str(sort3)+".")

