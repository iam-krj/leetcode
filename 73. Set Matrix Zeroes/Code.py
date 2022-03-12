class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==0:
                    row.add(i)
                    col.add(j)
        for k in row:
            for i in range(n):
                matrix[k][i] = 0
        for k in col:
            for i in range(m):
                matrix[i][k]=0
        return matrix