class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        
            
            
        first = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) in first:
                    return False
                first.add(int(board[i][j]))

            first.clear() 
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if int(board[j][i]) in first: 
                    return False
                first.add(int(board[j][i]))

            first.clear()   
            
        i = 0
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                first.clear() # Clear the set for each new 3x3 box
                
                # Loop through the 9 cells inside this specific box
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        
                        if val == ".":
                            continue
                            
                        if int(val) in first:
                            return False
                            
                        first.add(int(val))
                        
        return True
                    
            
        return True