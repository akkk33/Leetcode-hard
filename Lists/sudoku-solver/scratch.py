"""
References

"""
"""
to understand it:
we have 9 squares inside each one there are 9 numbers
We'll call the top row of squares 'a': [a1,a2,a3]
the middle row will be 'b': [b1,b2,b3]
the bottom row will be 'c': [c1,c2,c3]
"""
from random import randint as rand


class Solution:
    def randomise(self, board):
        a1, a2, a3 = board[0], board[1], board[2]
        b1, b2, b3 = board[3], board[4], board[5]
        c1, c2, c3 = board[6], board[7], board[8]
        for cell in board:


    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.randomise(board)


test = Solution()
print(test.solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
