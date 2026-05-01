class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows= [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):

                ch = board[i][j]

                if ch == ".":
                    continue

                var = ord(ch)- ord('1')

                mask = 1 << var   

                b = (i//3 * 3) + j//3

                if rows[i] & mask or cols[j] & mask or boxes[b] & mask:
                    return False

                rows[i] |= mask
                cols[j] |= mask
                boxes[b] |= mask

        return True

        