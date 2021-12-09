import random
# variable
num = int(input())
max_num = int(input())
def showGrid():
    for row in grid:
        for ele in row:
            print(ele, end="\t")
        print()
    print()

def generateRandomNumber():
    global numFreeCell
    randomCell = random.randint(1, numFreeCell)
    randomNumber = random.randint(1, 2) * 2
    freeCount = 0
    for i in range(num):
        for j in range(num):
            if grid[i][j] == 0:
                freeCount += 1
            if freeCount == randomCell:
                grid[i][j] = randomNumber
                numFreeCell -= 1
                return

def checkGameIsFinished():
    if maxVal >= max_num:
        print("Congratulations!!! You have won the game")
        return True
    if numFreeCell == 0:
        print("You lose the game. Try Again!!!")
        return True
    return False

def moveLeft():
    for i in range(num):
        for j in range(num):
            count = num - j
            while grid[i][j] == 0 and count > 0:
                for k in range(j, num - 1):
                    grid[i][k] = grid[i][k + 1]
                grid[i][num - 1] = 0
                count -= 1

        for j in range(num - 1):
            while grid[i][j] == grid[i][j + 1] != 0:
                grid[i][j] = 2 * grid[i][j]
                for k in range(j + 1, num - 1):
                    grid[i][k] = grid[i][k + 1]
                grid[i][num - 1] = 0

def moveRight():
    for i in range(num):
        for j in range(num - 1, -1, -1):
            count = j
            while grid[i][j] == 0 and count > 0:
                for k in range(j, 0, -1):
                    grid[i][k] = grid[i][k - 1]
                grid[i][0] = 0
                count -= 1

        for j in range(num - 1, -1, -1):
            while grid[i][j] == grid[i][j - 1] != 0:
                grid[i][j] = 2 * grid[i][j]
                for k in range(j - 1, 0, -1):
                    grid[i][k] = grid[i][k - 1]
                grid[i][0] = 0

def moveUp():
    for j in range(num):
        for i in range(num):
            count = num - i
            while grid[i][j] == 0 and count > 0:
                for k in range(i, num - 1):
                    grid[k][j] = grid[k + 1][j]
                grid[num - 1][j] = 0
                count -= 1

        for i in range(num - 1):
            while grid[i][j] == grid[i + 1][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                for k in range(i + 1, num - 1):
                    grid[k][j] = grid[k + 1][j]
                grid[num - 1][j] = 0

def moveDown():
    for j in range(num):
        for i in range(num - 1, -1, -1):
            count = i
            while grid[i][j] == 0 and count > 0:
                for k in range(i, 0, -1):
                    grid[k][j] = grid[k - 1][j]
                grid[0][j] = 0
                count -= 1

        for i in range(num - 1, -1, -1):
            while grid[i][j] == grid[i - 1][j] != 0:
                grid[i][j] = 2 * grid[i][j]
                for k in range(i - 1, 0, -1):
                    grid[k][j] = grid[k - 1][j]
                grid[0][j] = 0
maxVal = 0
numFreeCell = num**2
grid = [[0 for _ in range(num)] for __ in range(num)]

for _ in range(2):
    generateRandomNumber()

while True:
    showGrid()
    move = input()
    if move == "a":
        moveLeft()
    elif move == "d":
        moveRight()
    elif move == "w":
        moveUp()
    elif move == "s":
        moveDown()
    else:
        print("Please enter valid input")
        continue

    if checkGameIsFinished():
        break
    generateRandomNumber()