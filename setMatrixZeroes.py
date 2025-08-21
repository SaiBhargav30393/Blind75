class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r, c=len(matrix), len(matrix[0])
        colZero= False
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        colZero=True
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        if matrix[0][0]==0:
            for i in range(r):
                matrix[i][0]=0
        if colZero:
            for j in range(c):
                matrix[0][j]=0
        return matrix
                