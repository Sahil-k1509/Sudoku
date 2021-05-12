# board = [
#     ['.', '7', '.',   '.', '.', '.',   '.', '.', '9'],
#     ['5', '1', '.',   '4', '2', '.',   '6', '.', '.'],
#     ['.', '8', '.',   '3', '.', '.',   '7', '.', '.'],
    
#     ['.', '.', '8',   '.', '.', '1',   '3', '7', '.'],
#     ['.', '2', '3',   '.', '8', '.',   '.', '4', '.'],
#     ['4', '.', '.',   '9', '.', '.',   '1', '.', '.'],
    
#     ['9', '6', '2',   '8', '.', '.',   '.', '3', '.'],
#     ['.', '.', '.',   '.', '1', '.',   '4', '.', '.'],
#     ['7', '.', '.',   '2', '.', '3',   '.', '9', '6'],
# ]

def solve(board):
    # print_board(board)
    
    empty_cell = find_empty(board)
    if empty_cell == (-1, -1): 
        return True
    else:
        row, col = empty_cell
        
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                # print_board(board)
                return True
            
            board[row][col] = 0
            
    return False
                


def valid(board, num, pos):
    n = len(board)
    
    for i in range(n):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    for i in range(n):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    box_x, box_y = pos[1] // 3, pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True


def find_empty(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0: 
                return (i, j) # (row, col)
    return (-1, -1)  
            
    
def print_board(board):
    n = len(board)
    print()
    for i in range(n):
        if i % 3 == 0 and i > 0:
            print("-----------------------------")
        for j in range(n//3):
            print(" ", *board[i][3*j:3*j+3], end=' ')
        
            if j != n//3-1: print(" |", end='')
        print()
    print()      
            
            
# print_board(board) 
# solve(board)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print_board(board)