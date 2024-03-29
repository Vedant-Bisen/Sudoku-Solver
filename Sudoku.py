import time
board = [
    [0,0,0,0,0,6,0,4,0],
    [4,0,0,0,9,7,1,0,0],
    [0,2,7,5,4,0,0,8,0],
    [7,3,0,0,6,2,0,0,0],
    [1,0,2,0,0,0,0,7,0],
    [0,0,0,7,0,3,9,2,0],
    [0,1,0,0,0,0,4,0,8],
    [9,7,3,1,8,4,0,0,0],
    [0,4,0,0,0,0,0,0,0]
]


def print_board(bo):
    for i in range(0,len(bo)):
        if i % 3 == 0 and i != 0:
            print("_______________________")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ",end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ",end="")

def if_valid(bo,num,pos):

    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y * 3, box_y * 3 +3 ):
        for j in range(box_x * 3, box_x * 3 +3 ):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def empty(bo):  

    #check for empty or those row, col with 0 in them
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None

def solve(bo):

    #If no more empty exit reccur
    find = empty(bo)
    if not find:
        return True
    else:
        row,col = find

    #Check all digits one by one
    for i in range(1,10):
        if if_valid(bo,i,(row,col)):
            bo[row][col] = i

            
            if solve(bo):
                return True
            
            #Backtrack
            bo[row][col] = 0
        
    return False


print_board(board)
a = time.time()
solve(board)
b = time.time()
print("--------------------------------------")
print_board(board)
print(b-a)