from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, grids = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                value = board[r][c]
                if value == ".":
                    continue
                if (value in rows[r] or
                    value in cols[c] or
                    value in grids[(r//3,c//3)]):
                    return False
                rows[r].add(value)
                cols[c].add(value)
                grids[((r//3,c//3))].add(value)
        return True