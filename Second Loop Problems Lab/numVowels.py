def numVowels():
    string = input("Enter a string")
    numberVowels = 0
    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            numberVowels += 1
    return(numberVowels)
print("There are "+str(numVowels())+" vowels in your string.")
