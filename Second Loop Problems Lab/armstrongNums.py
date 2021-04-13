
def armstrong(n):
    first, second, third = str(n)
    if (int(first)**3)+(int(second)**3)+(int(third)**3)==n:
        answer = True
    else:
        answer = False
    return(answer)
print(str(armstrong(int(input("Choose a three digit number"))))+". Your number is an Armstrong Number.")
