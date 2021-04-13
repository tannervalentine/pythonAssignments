weight = input("What's your weight?")
age = input("What's your age?")
height = input("What's your height in inches?")
bmrMan = 66+(6.2*float(weight))+(12.7*float(height))-(6.76*float(age))
bmrWoman = 655.1+(4.35*float(weight))+(4.7*float(height))-(4.7*float(age))
print("Your base metabolic rate is "+str(bmrMan)+" for a man and "+str(bmrWoman)+" for a woman.")
chocMan = bmrMan/214
chocWoman = bmrWoman/214
print("You can eat "+str(chocMan)+" chocolate bars as a man or "+str(chocWoman)+" chocolate bars as a woman to maintain your weight.")

