import re

words = open("words.txt","r")
def animalRegex():
    catRegex = re.compile(r"\w*cat\w*")
    dogRegex = re.compile(r"\w*dog\w*")
    results = []
    for line in words:
        match = catRegex.search(line)
        match2 = dogRegex.search(line)
        if match:
            results.append(match.group())
        elif match2:
            results.append(match2.group())
    return len(results)
#print(str(animalRegex())+" words with cat or dog")

def fourRegex():
    fourReg = re.compile(r"^\w{4}$")
    results = []
    for line in words:
        match = fourReg.search(line)
        if match:
            results.append(match.group())
    return len(results)
#print(str(fourRegex())+" four letters words")

def hunRegex():
    hunReg = re.compile(r"\w*hun\w*")
    results = []
    for line in words:
        match = hunReg.search(line)
        if match:
            results.append(match.group())
    return len(results)
#print(str(hunRegex())+" words with \"hun\" in them")

def ingOrIon():
    ingRegex = re.compile(r"\w*ing\b")
    ionRegex = re.compile(r"\w*ion\b")
    resIng = []
    resIon = []
    for line in words:
        matchIng = ingRegex.search(line)
        matchIon = ionRegex.search(line)
        if matchIng:
            resIng.append(matchIng.group())
        elif matchIon:
            resIon.append(matchIon.group())
    if len(resIng) > len(resIon):
        return("There are more -ing words with "+str(len(resIng))+" matches.")
    elif len(resIng) < len(resIon):
        return("There are more -ion words with "+str(len(resIon))+" matches.")
    else:
        return("They have the same amount of matches!")
#print(ingOrIon())

def qNotU():
    noURegex = re.compile(r"\w*q[a-tv-zA-TV-Z]*\b")
    results = []
    for line in words:
        match = noURegex.search(line)
        if match:
            results.append(match.group())
    print(results)
    return(len(results))
#print("There are "+str(qNotU())+" words that don't have a \"u\" following a \"q\".")

def noVowels():
    noVowelReg = re.compile(r"^[^aeiouAEIOU\n]+$")
    results = []
    for line in words:
        match = noVowelReg.search(line)
        if match:
            results.append(match.group())
    return(len(results))
#print(str(noVowels())+" words with no vowels")

def allVowels():
    allVowelReg = re.compile(r"^[aeiouAEIOU]+$")
    results = []
    for line in words:
        match = allVowelReg.search(line)
        if match:
            results.append(match.group())
    return(len(results))
#print(str(allVowels())+" word with only vowels")

def contraction():
    contractReg = re.compile(r"\w+'nt$")
    results = []
    for line in words:
        match = contractReg.search(line)
        if match:
            results.append(match.group())
    return(len(results))
#print(str(contraction())+" words are contracted with \"not\"")

def twoVowelsRow():
    twoVowelReg = re.compile(r"\b.*[aeiouAEIOU]{2}.*\b")
    results = []
    for line in words:
        match = twoVowelReg.search(line)
        if match:
            results.append(match.group())
    return(len(results))
#print(str(twoVowelsRow())+" words with two vowels in a row")

def twoVowels():
    twoVowelReg = re.compile(r"[^\saeiouAEIOU]*[aeiouAEIOU][^\saeiouAEIOU]*[aeiouAEIOU].*")
    results = []
    for line in words:
        match = twoVowelReg.search(line)
        if match:
            results.append(match.group())
    return(len(results))
#print(str(twoVowels())+" words have at least 2 vowels")


"""
What is the difference between.*and.*? ?
The difference lies in the level of "greed"
.* will match 0 or more of all characters except white space
.*? will match 0 or more, but ere on the smaller side,
    essentially matching for the smallest amount of characters
    between the preceding and proceeding characters
"""

def nakamoto(string):
    nakaReg = re.compile(r"^[A-Z][^.,]* Nakamoto")
    match = nakaReg.search(string)
    if match:
        return True
    else:
        return False
#print(nakamoto("satoshi Nakamoto"))

def numberReg(string):
    numReg = re.compile(r"^(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-?(one|two|three|four|five|six|seven|eight|nine)?$")
    match = numReg.search(string)
    if match:
        return True
    else:
        return False
#print(numberReg("sixty-six"))

def dollarReg(string):
    dollarRegex = re.compile(r"^\$[1-9]\,?\d{1,2}(\,\d{3})*(\.\d\d)?$")
    match = dollarRegex.search(string)
    if match:
        return True
    else:
        return False
#print(dollarReg("$100.00"))


def strongPass(password):
    upperSearch = re.compile(r"^.*[A-Z].*$")
    lowerSearch = re.compile(r"^.*[a-z].*$")
    numSearch = re.compile(r"^.*[0-9].*$")
    match = upperSearch.search(password)
    if match:
        match2 = lowerSearch.search(password)
        if match2:
            match3 = numSearch.search(password)
            if match3:
                if len(password) >= 8:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

print(strongPass("a#B#c$1#2#3"))

import random
def passwordGen():
    data = open("words.txt","r").readlines()
    random.shuffle(data)
    newPass = data[0:4]
    for i in range(4):
        newPass[i] = newPass[i].rstrip()
    password = newPass[0]+newPass[1]+newPass[2]+newPass[3]
    return password

print(passwordGen())





    




