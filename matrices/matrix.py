import math
from math import sqrt
import numbers

'''

matrix.py
Author: Yadiel F. Cabrera Alvarado 

This is a class that contains operations
you can do with matrices, such as calculating the determinant, inverse,
transpose, etc.

'''

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here

         # For 1 x 1 Matrix
        if self.h == 1:
            return self.g[0]

        # For 2 x 2 Matrix:
        if self.h == 2:
            return self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here t
        # When t = 0
        for i in range(self.w):
            t += self.g[i][i]
        return t

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here

        if self.w == 1:
            return Matrix(1/self.g[0][0])
        if self.w == 2:
            invMat = zeroes(self.w, self.h)
            invMat[0][0] = self.g[1][1] * (1/self.determinant())
            invMat[0][1] = -self.g[0][1] * (1/self.determinant())
            invMat[1][0] = -self.g[1][0] * (1/self.determinant())
            invMat[1][1] = self.g[0][0] * (1/self.determinant())

            return invMat

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # Creates a matrix of zeroes
        grid = zeroes(self.w, self.h)

        # Traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                grid[c][r] = self.g[r][c]
        return grid

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #
        # TODO - your code here
        #

         # Create a matrix of zeroes
        grid = zeroes(self.h, self.w)

        # Go through each element in the matrix
        for r in range(self.h):
            for c in range(self.w):
                grid[r][c] = self.g[r][c] + other.g[r][c] # add the elements
        return grid


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        # Creates matrix of zeroes
        mat = zeroes(self.h, self.w)

        # Traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                 mat[r][c] = self.g[r][c]*-1.0
        return mat

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
          # creates a self.h x self.w matrix of zeroes
        mat = zeroes(self.h, self.w)

        # traverse each element in matrix
        for r in range(self.h):
            for c in range(self.w):
                mat[r][c] = self.g[r][c]-other.g[r][c]
        return mat

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # Creates a matrix of zeroes
        # mat will have the result
        mat = zeroes(self.h, other.w)

        for x in range(self.h):
            for y in range(other.w):
                for z in range(other.h):
                    mat[x][y] += self.g[x][z] * other.g[z][y]
        return mat

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            mat = self
            for r in range(self.h):
                for c in range(self.w):
                    mat[r][c] *= other
            return mat
