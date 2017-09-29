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
    print("Choose 6 numbers from 1 to 20")
    inputNumbers = []
    for i in range(6):
        inputNumbers.append(int(input()))

    global balance
    balance -= 50
    print("You have choosen numbers {} and USD 50 has been deducted from your balance".format(inputNumbers))
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
    print("Your balance is " + balance)
    print("Thanks you for being with us. See you again!!!")

def playAgainOrLeave():
    cmd = input("Do you want to [p]lay again or [l]eave the game?")
    if cmd == 'p' or cmd == 'P':
        checkCondition()
    elif cmd == 'l' or cmd == 'L':
        leaveGame()


checkCondition()