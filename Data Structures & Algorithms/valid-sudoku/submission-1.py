def check_valid(lst):
    cnt = [v for k, v in Counter(lst).items() if k.isdigit()]
    if any([x > 1 for x in cnt]):
        return False
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            
            # check rows
            row = board[i] # ith row
            if not check_valid(row):
                return False

            # check columns
            col = [row[i] for row in board] # ith column
            if not check_valid(col):
                return False

            # check sub-box
            j, k = i//3*3, i%3*3 # get the top left row and column of each box
            box = [r[k:k+3] for r in board[j:j+3]] # get the box
            box_list = [x for row in box for x in row] # convert the box to a list
            if not check_valid(box_list):
                return False

        return True