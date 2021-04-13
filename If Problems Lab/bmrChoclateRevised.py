gender = input("What's your gender? (male/female)").upper()
weight = float(input("What's your weight in pounds?"))
age = float(input("What's your age in years?"))
height = float(input("What's your height in inches?"))

def calc():
    print("Your base metabolic rate is "+str(bmr)+" calories a day.")
    bars = bmr/214
    print("You can eat "+str(bars)+" chocolate bars a day as a "+gender.lower()+".")

if gender == "MALE":
    bmr = 66+(6.2*weight)+(12.7*height)-(6.76*age)
    calc()
elif gender == "FEMALE":
    bmr = 655.1+(4.35*weight)+(4.7*height)-(4.7*age)
    calc()
else:    
    print("Sorry that input is invalid.")


