def breedingCandidates(file):
    data = open(file,"r").readlines()
    data = data[1:]
    suitable = []
    for line in data:
        line = line.split(",")
        name = line[0]
        kids = line[1]
        age = line[2]
        if (age < 25) and (kids < 5):
            suitable.append(name)
    return suitable

import re
def turtleCheck(filename):
    data = open(filename,"r").readlines()
    turtRegex = re.compile(r"[frlb] \d+\.?\d*")
    for line in data:
        match = turtRegex.search(line)
        if not match:
            return False
    return True

import turtle

def turtleFromFile(filename):
    chet = turtle.Turtle()
    data = open(filename,"r").readlines()
    for line in data:
        line = line.split()
        line[1] = float(line[1])
        if line[0] == "f":
            chet.fd(line[1])
        if line[0] == "b":
            chet.bk(line[1])
        if line[0] == "l":
            chet.left(line[1])
        if line[0] == "r":
            chet.right(line[1])

def wubalub(n):
    for num in range(1,n+1):
        if (num % 5) == 0:
            if (num % 7) == 0:
                print("wubalub")
            else:
                print("wuba")
        elif (num % 7) == 0:
            print("lub")
        else:
            print(num)
import random
def queensGame():
    cards = ["Q","Q","K","K","J","J"]
    wins = 0
    for games in range(100000):
        newDeck = random.sample(cards,6)
        top2 = [newDeck[0],newDeck[1]]
        if "Q" not in top2:
            wins += 1
    winChance = wins/100000
    winChancePercent = winChance*100
    return "You have a "+str(winChancePercent)+"% chance of winning each game."

def uniqueWords(filename):
    data = open(filename,"r").read()
    data = data.split()
    uniqueWords = set()
    for word in data:
        uniqueWords.add(word)
    return len(uniqueWords)
print(uniqueWords("words.txt"))




            
