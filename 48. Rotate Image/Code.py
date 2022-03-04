class Solution(object):
    def rotate(self, m):
        n = len(m)
        for j in range(n):
            for i in range(n//2):
                m[i][j], m[n-1-i][j] = m[n-1-i][j], m[i][j]
        for i in range(n):
            for j in range(i+1,n):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        return m