def firstVowel(string):
    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            return(string.index(letter))
        
def numVowels(string):
    numberVowels = 0
    for letter in string:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            numberVowels += 1
    return(numberVowels)

def pigLatin(string):
    if string[0]=="a" or string[0]=="e" or string[0]=="i" or string[0]=="o" or string[0]=="u":
        return(string[1:]+string[0]+"way")
    elif numVowels(string) != 0:
        return(string[firstVowel(string):]+string[0:firstVowel(string)]+"ay")
    else:
        return(string)

def rot13(string):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    rotated = ""
    for letter in string:
        newIndex = alphabet.index(letter)+13
        rotated += alphabet[newIndex]
    return(rotated)

def main():
    done = False
    while not done:
        word = input("Enter a word (type 'done' to quit)").lower()
        print(pigLatin(word), word[::-1], rot13(word))
        if word == "done":
            done = True
main()
        
