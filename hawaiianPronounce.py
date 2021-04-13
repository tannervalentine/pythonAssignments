characters = ["a","e","i","o","u","p","k","h","l","m","n","w"," ","'"]
vowels = ["a","e","i","o","u"]
consonants = ["p","k","h","l","m","n","w"]
def checkChar(word):
    for character in word:
        if character not in characters:
            return(False)
        else:
            pass
    return(True)
def badChar(word):
    for character in word:
        if character not in characters:
            return(character)
def changeWord(word):
    newWord = ""
    word = word.lower()
    index = 0
    while index < len(word):
        if index != 0:
            if index < len(word)-1:
                let = word[index]
                nextLet = word[index+1]
                lastLet = word[index-1]
            else:
                let = word[index]
                nextLet = ""
                lastLet = word[index-1]
        else:
            let = word[index]
            nextLet = word[index+1]
            lastLet = ""
        if let in vowels:
            if let == "a":
                if nextLet == "i":
                    newWord += "eye"
                    index += 1
                elif nextLet == "e":
                    newWord += "eye"
                    index += 1
                elif nextLet == "o":
                    newWord += "ow"
                    index += 1
                elif nextLet == "u":
                    newWord += "ow"
                    index += 1
                else:
                    newWord += "ah"
            elif let == "e":
                if nextLet == "i":
                    newWord += "ay"
                    index += 1
                elif nextLet == "u":
                    newWord += "eh-oo"
                    index += 1
                else:
                    newWord += "eh"
            elif let == "i":
                if nextLet == "u":
                    newWord += "ew"
                    index += 1
                else:
                    newWord += "ee"
            elif let == "o":
                if nextLet == "i":
                    newWord += "oyo"
                    index += 1
                elif nextLet == "u":
                    newWord += "ow"
                    index += 1
                else:
                    newWord += "oh"
            elif let == "u":
                if nextLet == "i":
                    newWord += "ooey"
                    index += 1
                else:
                    newWord += "oo"
        if let in consonants:
            if let == "w":
                if index == 0:
                    newWord += let
                elif lastLet == "a":
                    newWord += let
                elif lastLet == "i" or lastLet == "e":
                    newWord += "v"
                elif lastLet == "u" or lastLet == "o":
                    newWord += let
            else:
                newWord += let
        if let == " " or let == "'":
            newWord += let
        if let in vowels:
            newWord += "-"
        index += 1
    newWord = newWord[0: -1]
    newWord = newWord.capitalize()
    return(newWord)
def main():
    print("This program gives the Hawaiian pronounciation of words.")
    done = False
    while not done:
        word = input("Enter a word to pronounce")
        if checkChar(word) == True:
            print(word.upper()+" is pronounced "+changeWord(word))
        else:
            print(badChar(word)+" is not a valid character.")
        answer = input("Do you want to enter a word? (Y/YES/N/NO) -->")
        if answer.lower() == "n" or answer.lower() == "no":
            done = True
        elif answer.lower() == "y" or answer.lower() == "yes":
            done = False
main()
