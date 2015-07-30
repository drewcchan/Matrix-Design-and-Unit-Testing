class MatrixError(Exception):
    # An exception to throw for the Matrix class and subclasses
    pass


class Matrix():
    ''' A General Matrix Class '''
    def __init__(self, rows, cols, values=None):
        ''' (Matrix, int, int, list) -> NoneType
        Initializes a matrix with specified rows and cols. A list of values
        can create the matrix in row major order, else a zero matrix is formed
        REQ: values is empty or length is equal to total number of elements
        '''

    def __str__(self):
        ''' (Matrix) -> str
        Prints a string representation of the matrix as a list of lists with
        each row on a separate line
        '''

    def dimensions(self):
        ''' (Matrix) -> tuple of ints
        Returns dimensions of matrix as row, col
        '''

    def __eq__(self, other_matrix):
        ''' (Matrix, Matrix) -> bool
        Returns if 2 matrices are equal to each other
        '''

    def __add__(self, other_matrix):
        ''' (Matrix, Matrix, ...) -> Matrix
        Returns the sum of 2 or more Matrices as a Matrix using matrix addition
        If strings, will add the 2nd matrix elements to the end of the 1st
        REQ: matrices must be the same dimensions and either contain all
        numbers or contain all letters
        '''

    def __sub__(self, other_matrix):
        ''' (Matrix, Matrix, ...) -> Matrix
        Returns the difference of 2 or more Matrices as a Matrix using
        matrix subtraction
        REQ: matrices must be the same dimensions and contain only numbers
        '''

    def __mul__(self, other):
        '''(Matrix, Matrix or int or float, ...) -> Matrix
        Returns the product of multiple matrices using matrix multiplication or
        multiplies an int or float with the matrix using scalar multiplication
        REQ: matrices contain only numbers and the multiplier must be a matrix
        with the same dimensions as the original or be a scalar
        '''

    def __getitem__(self, index):
        ''' (Matrix[tuple]) -> list or str or int or float
        Returns the specified value, row, or column depending on the index
        If a specified value is desired, an int, float or str is returned
        If a row or column is specified, a list is returned
        The index is a tuple specified as [row, col]
        If the entire row or col is desired, : can be used
        REQ: index is within the range of the matrix dimensions
        '''

    def __setitem__(self, index, values):
        ''' (Matrix[tuple], list) -> NoneType
        Sets the value, row, or column depending on the index
        REQ: number of values is equal to number of elements in index
        '''

    def swap_rows(self, row1, row2):
        ''' (Matrix, int, int) -> NoneType
        Swaps 2 rows in the matrix starting at index 0
        REQ: row indices are within the matrix dimensions
        '''

    def swap_cols(self, col1, col2):
        ''' (Matrix, int, int) -> NoneType
        Swaps 2 cols in the matrix starting at index 0
        REQ: col indices are within the matrix dimensions
        '''

    def transpose(self):
        ''' (Matrix) -> Matrix
        Returns the transpose of the matrix
        '''

    def all_numbers(self):
        ''' (Matrix) -> bool
        Returns if all elements in the matrix are numbers
        '''

    def all_strings(self):
        ''' (Matrix) -> bool
        Returns if all elements in the matrix are strings
        '''


class OneDMatrix(Matrix):
    ''' A class for a 1 dimensional matrix '''
    def __init__(self, length, style='row', values=None):
        ''' (OneDMatrix, int, str, list) -> NoneType
        Creates a one dimensional matrix as a vector
        Length indicates the number of elements in the vector
        Style specifies if a row or col vector is created (row is default)
        If list of values excluded, a zero vector will be created
        REQ: values is empty or length of list is equal to length
        '''

    def __getitem__(self, index):
        ''' (OneDMatrix[int or slice]) -> str or int or float or list
        If 1 element entered, will return str, int or float
        If entire vector requested, will return a list
        The symbol : can be used to retrieve the entire list
        The index is a int starting at 0
        REQ: index must be within matrix dimensions
        '''

    def __setitem__(self, index, values):
        ''' (OneDMatrix[int or slice], list) -> NoneType
        Sets the value, row, or column depending on the index
        REQ: length of values must equal length of elements in index
        '''

    def transpose(self):
        ''' (OneDMatrix) -> OneDMatrix
        Returns the transpose of a one d matrix
        '''


class SquareMatrix(Matrix):

    def __init__(self, rows, values=None):
        ''' (SquareMatrix, int, list) -> NoneType
        Creates a square matrix with the dimensions being the number of rows
        multiplied by the number of rows
        If list of values excluded, a zero square matrix will be created
        REQ: list of values is empty or equal to total number of elements
        '''

    def get_diagonal(self):
        ''' (SquareMatrix) -> list
        Returns the diagonal of the square matrix starting from the top left
        corner and ending in the bottom right corner
        '''

    def set_diagonal(self, values):
        ''' (SquareMatrix, list) -> NoneType
        Sets the diagonal of the square matrix starting from the top left
        corner and ending in the bottom right corner
        REQ: length of values equals number of elements in diagonal
        '''

    def determinant(self):
        ''' (SquareMatrix) -> int or float
        Returns the determinant of a 2x2 matrix
        The determinant is the product of the top left and bottom right
        elements minus the product of the top right and bottom left elements
        REQ: all numbers in matrix and matrix dimensions is 2x2
        '''

    def transpose(self):
        ''' (SquareMatrix) -> SquareMatrix
        Returns the transpose of a square matrix
        '''


class IdentityMatrix(SquareMatrix):
    ''' A class for an identity matrix '''
    def __init__(self, rows, value=1):
        ''' (IdentityMatrix, int, int or str or float) -> NoneType
        Creates an identity matrix with specified values
        The default identity matrix is with value 1
        The diagonal of the identity matrix has the same value with 0
        everywhere else
        '''

    def transpose(self):
        ''' (IdentityMatrix) -> IdentityMatrix
        Returns the transpose of identity matrix, which is itself
        '''

    def set_diagonal(self, value):
        ''' (IdentityMatrix, int or float or str) -> NoneType
        Sets the diagonal of the identity matrix starting from the top left
        corner and ending in the bottom right corner
        An Identity Matrix has the same values in the diagonal
        '''

    def __setitem__(self, index=None, values=None):
        ''' (IdentityMatrix[tuple], list) -> MatrixError
        Raises error if altering individual element, row or column as identity
        matrix can only have values in the diagonal
        '''


class SymmetricMatrix(SquareMatrix):
    ''' A class for a symmetric matrix '''
    def __init__(self, rows):
        ''' (SymmetricMatrix, int) -> NoneType
        A symmetric matrix of size rows by rows is created with zeros in
        all locations
        Changing values will change the values mirrored across the diagonal
        '''

    def __setitem__(self, index, values):
        ''' (SymmetricMatrix[tuple], list or int or str or float) -> NoneType
        Sets the value, row, or column depending on the index
        Will also set the mirrored values along the diagonal to the same values
        REQ: length of values is equal to number of elements in index
        '''

    def transpose(self):
        ''' (SymmetricMatrix) -> SymmetricMatrix
        Returns the transpose of symmetric matrix, which is itself
        '''
