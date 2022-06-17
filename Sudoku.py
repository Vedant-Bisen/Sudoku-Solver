import numpy as np




def print_board(bo):
    for i in range(0,len(bo)):
        if i % 3 == 0 and i != 0:
            print("_______________________")

        for j in range(0,len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ",end="")

def if_valid(bo,k,n,m):
    valid = True

    for i in range(0,9):
        if bo[i][n] == k:
            valid = False

    for i in range(0,9):
        if bo[i][m] == k:
            valid = False
    
    return valid

def checker(bo):
    for i in range(0,8):
        for j in range(0,8):
            pass




board = np.array([
    [0,0,4,0,5,0,0,0,0],
    [9,0,0,7,3,4,6,0,0],
    [0,0,3,0,2,1,0,4,9],
    [0,3,5,0,9,0,4,8,0],
    [0,9,0,0,0,0,0,3,0],
    [0,7,6,0,1,0,9,2,0],
    [3,1,0,9,7,0,2,0,0],
    [0,0,9,1,8,2,0,0,3],
    [0,0,0,0,6,0,1,0,0]
    ])

print_board(board)
checker(board)
print("--------------------------------------------")
print_board(board)
