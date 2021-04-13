import random
#Professor Rosen if you see this I'm sorry for not using many functions inside of functions. This is a WALL of text
def rollDice():
    num = random.randint(1,6)
    return(num)

def holdAt20():
    total = 0
    done = False
    while not done:
        roll = rollDice()
        total += roll
        if roll == 1:
            total = 0
            done = True
        if total >= 20:
            done = True
        print("Roll: "+str(roll))
    print("Turn total: "+str(total))
#holdAt20()
def holdAt20Outcomes():
    scores = {}
    simulations = int(input("Hold-at-20 turn simulations?"))
    for turn in range(simulations):
        total = 0
        done = False
        while not done:
            roll = rollDice()
            total += roll
            if roll == 1:
                total = 0
                done = True
            if total >= 20:
                done = True
        if total not in scores:
            scores[total] = 1
        else:
            scores[total] += 1
    print("Score    Estimated Probability")
    for score in sorted(scores.keys()):
        print(str(score),(scores[score]/simulations*100), sep = "       ")
#holdAt20Outcomes()
def holdAtXOutcomes():
    hold = int(input("What is the hold value?"))
    scores = {}
    simulations = int(input("Hold-at-"+str(hold)+" turn simulations?"))
    for turn in range(simulations):
        total = 0
        done = False
        while not done:
            roll = rollDice()
            total += roll
            if roll == 1:
                total = 0
                done = True
            if total >= hold:
                done = True
        if total not in scores:
            scores[total] = 1
        else:
            scores[total] += 1
    print("Score    Estimated Probability")
    for score in sorted(scores.keys()):
        print(str(score),(scores[score]/simulations*100), sep = "       ") 
holdAtXOutcomes()
def holdAt20OrGoal():
    baseScore = int(input("What is the starting score?"))
    total = 0
    done = False
    while not done:
        roll = rollDice()
        total += roll
        if roll == 1:
            total = 0
            done = True
        if total >= 20:
            done = True
        if total+baseScore >= 100:
            done = True
        print("Roll: "+str(roll))
    print("Turn total: "+str(total))
    print("New Score: "+str(total+baseScore))
#holdAt20OrGoal()
def holdAt20OrGoalGame():
    score = 0
    doneScore = False
    while not doneScore:
        total = 0
        done = False
        while not done:
            roll = rollDice()
            total += roll
            if roll == 1:
                total = 0
                done = True
            if total >= 20:
                done = True
            print("Roll: "+str(roll))
        print("Turn total: "+str(total))
        score += total
        print("New Score: "+str(score))
        if score >= 100:
            doneScore = True
#holdAt20OrGoalGame()    
def avgPigTurns():
    games = int(input("How many games?"))
    turns = 0
    for i in range(games):
        score = 0
        doneScore = False
        while not doneScore:
            turns += 1
            total = 0
            done = False
            while not done:
                roll = rollDice()
                total += roll
                if roll == 1:
                    total = 0
                    done = True
                if total >= 20:
                    done = True
            score += total
            if score >= 100:
                doneScore = True
    print("Average Turns: "+str(turns/games))
#avgPigTurns()
def twoPlayerPig():
    doneGame = False
    player = 0
    score1=0
    score2=0
    while not doneGame:
        if player%2==0:
            print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
            print("It is Player 1's turn")
            total1 = 0
            done1 = False
            while not done1:
                roll = rollDice()
                total1 += roll
                if roll == 1:
                    total1 = 0
                    done1 = True
                if total1 >= 20:
                    done1 = True
                print("Roll: "+str(roll))
            print("Turn total for Player 1: "+str(total1))
            score1 += total1
            print("New Score for Player 1: "+str(score1))
            if score1 >= 100:
                doneGame = True
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("Player 1 wins!")
            player += 1
        elif player%2 == 1:
            print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
            print("It is Player 2's turn")
            total2 = 0
            done2 = False
            while not done2:
                roll = rollDice()
                total2 += roll
                if roll == 1:
                    total2 = 0
                    done2 = True
                if total2 >= 20:
                    done2 = True
                print("Roll: "+str(roll))
            print("Turn total for Player 2: "+str(total2))
            score2 += total2
            print("New Score for Player 2: "+str(score2))
            if score2 >= 100:
                doneGame = True
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("Player 2 wins!")
            player += 1
#twoPlayerPig()          
def pigGame():
    playerPick = random.randint(1,2)
    if playerPick == 1:
        print("You are Player 1")
        doneGame = False
        player = 0
        score1=0
        score2=0
        while not doneGame:
            if player%2==0:
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("It is Player 1's turn")
                total1 = 0
                done1 = False
                while not done1:
                    roll = rollDice()
                    total1 += roll
                    if roll == 1:
                        total1 = 0
                        done1 = True
                    print("Roll: "+str(roll))
                    if total1 != 0:
                        if input("Turn total: "+str(total1)+" Hold? (Y/N)").upper() == "Y":
                            done1 = True
                print("Turn total for Player 1: "+str(total1))
                score1 += total1
                print("New Score for Player 1: "+str(score1))
                print("----------")
                if score1 >= 100:
                    doneGame = True
                    print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                    print("Player 1 wins!")
                player += 1
            elif player%2 == 1:
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("It is Player 2's turn")
                total2 = 0
                done2 = False
                while not done2:
                    roll = rollDice()
                    total2 += roll
                    if roll == 1:
                        total2 = 0
                        done2 = True
                    if total2 >= 20:
                        done2 = True
                    print("Roll: "+str(roll))
                print("Turn total for Player 2: "+str(total2))
                score2 += total2
                print("New Score for Player 2: "+str(score2))
                print("----------")
                if score2 >= 100:
                    doneGame = True
                    print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                    print("Player 2 wins!")
                player += 1
    else:
        print("You are Player 2")
        doneGame = False
        player = 0
        score1=0
        score2=0
        while not doneGame:
            if player%2==0:
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("It is Player 1's turn")
                total1 = 0
                done1 = False
                while not done1:
                    roll = rollDice()
                    total1 += roll
                    if roll == 1:
                        total1 = 0
                        done1 = True
                    if total1 >= 20:
                        done1 = True
                    print("Roll: "+str(roll))
                print("Turn total for Player 1: "+str(total1))
                score1 += total1
                print("New Score for Player 1: "+str(score1))
                print("--------------------")
                if score1 >= 100:
                    doneGame = True
                    print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                    print("Player 2 wins!")
                player += 1
            elif player%2 == 1:
                print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                print("It is Player 2's turn")
                total2 = 0
                done2 = False
                while not done2:
                    roll = rollDice()
                    total2 += roll
                    if roll == 1:
                        total2 = 0
                        done2 = True
                    print("Roll: "+str(roll))
                    if total2 != 0:
                        if input("Turn total: "+str(total2)+" Hold? (Y/N)").upper() == "Y":
                            done2 = True
                print("Turn total for Player 2: "+str(total2))
                score2 += total2
                print("New Score for Player 2: "+str(score2))
                print("--------------------")
                if score2 >= 100:
                    doneGame = True
                    print("Player 1 score: "+str(score1)+"\n"+"Player 2 score: "+str(score2))
                    print("Player 2 wins!")
                player += 1
#pigGame()
