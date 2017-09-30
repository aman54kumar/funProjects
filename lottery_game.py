import random

balance = 2000

def checkCondition():
    print("Welcome to the lottery store")
    myOption = str(input("Do you want to [b]uy, [c]heck balance or [l]eave?"))

    print("\n \n \n")
    while True:
        if myOption == "b" or myOption == "B":
            choosen = buyTicket()
            winning = winningTicket()
            wins = checkWins(choosen, winning)
            assignMoney(wins)
            playAgainOrLeave()
            break
        elif myOption == "c" or myOption == "C":
            checkBalance()
            playAgainOrLeave()
            break
        elif myOption == "l" or myOption == "L":
            leaveGame()
            break
        else:
            print("wrong value Entered. Please Try Again!!")
            checkCondition()



def buyTicket() -> list:
    """

    :rtype: list
    """
    inputNumbers = []
    inputNum = input("Choose 6 unique numbers from 1 to 20 separated by commas: ")
    inputNumbers = list(map(int, inputNum.split(',')))
    while len(inputNumbers) != 6:
        inputNumbers = checkDuplicate(inputNumbers)

        if len(inputNumbers) < 6:
            leftOverList = []
            leftOver = input("Please enter " + str(6 - len(inputNumbers)) + " more numbers: ")
            leftOverList = list(map(int, leftOver.split(',')))
            if len(leftOverList):
                inputNumbers = inputNumbers + leftOverList
                continue


        if len(inputNumbers) > 6:
            inputNumbers = inputNumbers[:6]

        checkNumberInRange(inputNumbers)


    global balance
    balance -= 50
    print("You have choosen numbers {} and USD 50 has been deducted from your balance".format(inputNumbers))
    return inputNumbers


def checkNumberInRange(inputNumbers):
    for i in inputNumbers:
        if i > 20 or i < 1:
            loc = inputNumbers.index(i)
            additional = input(str(i) + " is out of range. Please enter another number between 1-20: ")
            inputNumbers[loc] = additional


def checkDuplicate(inputNumbers):
    import collections
    inputNumbers = [item for item, count in collections.Counter(inputNumbers).items() if count == 1]
    return inputNumbers


def winningTicket():
    winningNumbers = random.sample(range(1, 20), 6)
    print("Winning numbers for this round are {}".format(winningNumbers))
    return winningNumbers

def checkWins(myInput, winInput):
    count = 0
    for i in myInput:
        for j in winInput:
            if i == j:
                count = count + 1
    return count




def assignMoney(count):
    prizes = [0, 10, 50, 400, 2000, 40000, 1000000]
    amountWon = prizes[count]
    global balance
    balance += amountWon
    if amountWon > 0:
        print("Congratulations!! You matched {} numbers and you won {} USD".format(count, amountWon))
    else:
        print("You didn't match any numbers. Hard Luck, try again!!")


def checkBalance():
    print("Your balance is {} USD".format(balance))

def leaveGame():
    print("Your balance is " + str(balance))
    print("Thanks you for being with us. See you again!!!")

def playAgainOrLeave():
    cmd = input("Do you want to [p]lay again or [l]eave the game?")
    if cmd == 'p' or cmd == 'P':
        checkCondition()
    elif cmd == 'l' or cmd == 'L':
        leaveGame()


checkCondition()