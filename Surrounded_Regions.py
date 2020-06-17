'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X
Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''
#Solution: Using FloodFill Algorithm

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """       
        def floodFill(b, x, y, dash , o): 
            if (x < 0 or x >= M or y < 0 or y >= N): 
                return 
            if (b[x][y] != dash): 
                return 
    
            b[x][y] = o;
        
            #Recur for north, east, south and west 
            floodFill(b, x+1, y, dash, o) 
            floodFill(b, x-1, y, dash, o)
            floodFill(b, x, y+1, dash, o)
            floodFill(b, x, y-1, dash, o)
   
  
    
        M=len(board)
        if(M<=2):
            return board
        N=len(board[0])
        if(N<=2):
            return board
        
        #Step 1: Replace all 'O'  with '-' 
        for i in range(M): 
            for j in range(N):
                if board[i][j] == 'O': 
                    board[i][j] = '-'
        #Call floodFill for all '-' lying on edges             
        for i in range(M):    
            if (board[i][0] == '-'):
                floodFill(board, i, 0, '-', 'O'); 
        for i in range(M):   
            if (board[i][N-1] == '-'): 
                floodFill(board, i, N-1, '-', 'O'); 
        for i in range(N):    
            if (board[0][i] == '-'): 
                floodFill(board, 0, i, '-', 'O'); 
        for i in range(N):  
            if (board[M-1][i] == '-'): 
                floodFill(board, M-1, i, '-', 'O'); 
                
        #Step 3: Replace all '-' with 'X'        
        for i in range(M): 
            for j in range(N):
                if board[i][j] == '-': 
                    board[i][j] = 'X'
        
        return board
        
        
        
        
        
