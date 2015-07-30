import unittest
from a1_design import *


class TestMatrixMethods(unittest.TestCase):
    '''Unittests for matrix class methods'''
    def setUp(self):
        ''' Objects to use for tests'''
        self.matrix1 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
        self.matrix2 = Matrix(2, 3, [6, 5, 4, 3, 2, 1])
        self.matrix3 = Matrix(2, 1, [1, 2])
        self.matrix4 = Matrix(1, 2, [2, 3])
        self.matrix5 = Matrix(1, 2, [2, 'a'])
        self.matrix6 = Matrix(3, 2)
        self.matrix7 = Matrix(2, 3)
        self.matrix8 = Matrix(1, 2, ['a', 'a'])
        self.matrix9 = Matrix(1, 2, ['b', 'b'])
        self.matrix10 = Matrix(3, 2)

    def test_matrix_init(self):
        ''' Test matrix initialization'''
        # test init of zero matrix
        actual_result1 = str(self.matrix6)
        expected_result1 = '[0, 0]\n[0, 0]\n[0, 0]'
        self.assertEqual(actual_result1, expected_result1,
                         'Test if zero matrix is created')

        # test init of filled matrix
        actual_result2 = str(self.matrix1)
        expected_result2 = '[1, 2, 3]\n[4, 5, 6]'
        self.assertEqual(actual_result2, expected_result2,
                         'Test if filled matrix is created')

        # test if matrices are different with the same contents, but
        # different dimensions
        actual_result3 = self.matrix6 == self.matrix7
        expected_result3 = False
        self.assertEqual(actual_result3, expected_result3,
                         'Test if dimensions are different')

        # test if raises error with incorrect number of values inputted
        with self.assertRaises(MatrixError):
            Matrix(1, 2, [2, 'a', 'b'])

    def test_matrix_str(self):
        '''Test matrix string'''
        actual_result = str(self.matrix1)
        expected_result = '[1, 2, 3]\n[4, 5, 6]'
        self.assertEqual(actual_result, expected_result,
                         'Test if matrix string is printed')

    def test_matrix_dimensions(self):
        '''Test matrix dimensions'''
        # test for dimensions
        actual_result = self.matrix1.dimensions()
        expected_result = (2, 3)
        self.assertEqual(actual_result, expected_result,
                         'Test if dimensions are correct')

    def test_matrix_eq(self):
        '''Test matrix equality'''
        # test for equality when equal
        actual_result1 = self.matrix6 == self.matrix10
        expected_result1 = True
        self.assertEqual(actual_result1, expected_result1,
                         'Test if true when equal')

        # test for equality when unequal
        actual_result2 = self.matrix6 == self.matrix7
        expected_result2 = False
        self.assertEqual(actual_result2, expected_result2,
                         'Test if true when unequal')

    def test_matrix_add(self):
        '''Test matrix addition '''
        # test for correct addition of numbers
        actual_result1 = self.matrix1 + self.matrix2
        expected_result1 = Matrix(2, 3, [7, 7, 7, 7, 7, 7])
        self.assertEqual(actual_result1, expected_result1,
                         'Test matrix addition of numbers')

        # test for correct addition of strings
        actual_result2 = self.matrix8 + self.matrix9
        expected_result2 = Matrix(1, 2, ['ab', 'ab'])
        self.assertEqual(actual_result2, expected_result2,
                         'Test matrix addition of strings')

        # test if raises error when adding matrices with different dimensions
        with self.assertRaises(MatrixError):
            self.matrix1 + self.matrix3

        # test if raises error when adding matrix with strings to matrix
        # with numbers
        with self.assertRaises(MatrixError):
            self.matrix4 + self.matrix8

    def test_matrix_sub(self):
        '''Test matrix subtraction'''
        # test for correct subtraction
        actual_result = self.matrix2 - self.matrix1
        expected_result = Matrix(2, 3, [5, 3, 1, -1, -3, -5])
        self.assertEqual(actual_result, expected_result,
                         'Test matrix subtraction')

        # test if raises error when subtracting with strings as elements
        with self.assertRaises(MatrixError):
            self.matrix4 - self.matrix5
        with self.assertRaises(MatrixError):
            self.matrix5 - self.matrix4

        # test if raises error when subtracting with different dimensions
        with self.assertRaises(MatrixError):
            self.matrix1 - self.matrix3

    def test_matrix_mul(self):
        '''Test matrix multiplication'''
        # test correct matrix with scalar multiplication
        actual_result1 = self.matrix1 * 2
        expected_result1 = Matrix(2, 3, [2, 4, 6, 8, 10, 12])
        self.assertEqual(actual_result1, expected_result1,
                         'Test scalar matrix multiplication')

        # test correct matrix with matrix multiplication
        actual_result2 = self.matrix3 * self.matrix4
        expected_result2 = Matrix(2, 2, [2, 3, 4, 6])
        self.assertEqual(actual_result2, expected_result2,
                         'Test matrix multiplication')

        # test if raises error when multiplying with strings as elements
        with self.assertRaises(MatrixError):
            self.matrix3 * self.matrix5
        with self.assertRaises(MatrixError):
            self.matrix5 * self.matrix3

        # test if raises error when multipying with different dimensions
        with self.assertRaises(MatrixError):
            self.matrix1 * self.matrix3

    def test_matrix_get(self):
        '''Test getting elements from matrix'''
        # test getting single element
        actual_result1 = self.matrix1[1, 2]
        expected_result1 = 6
        self.assertEqual(actual_result1, expected_result1,
                         'Test matrix single element get')

        # test getting row
        actual_result2 = self.matrix1[1, :]
        expected_result2 = [4, 5, 6]
        self.assertEqual(actual_result2, expected_result2,
                         'Test matrix row get')

        # test getting col
        actual_result3 = self.matrix1[:, 1]
        expected_result3 = [2, 5]
        self.assertEqual(actual_result3, expected_result3,
                         'Test matrix col get')

        # test if raises error when index out of range
        with self.assertRaises(IndexError):
            self.matrix1[1, 5]
        with self.assertRaises(IndexError):
            self.matrix1[5, 1]

    def test_matrix_set(self):
        '''Test setting elements in matrix'''
        # test setting single element
        self.matrix1[1, 2] = 10
        actual_result1 = self.matrix1[1, 2]
        expected_result1 = 10
        self.assertEqual(actual_result1, expected_result1,
                         'Test matrix single element set')

        # test setting row
        self.matrix1[1, :] = [7, 8, 9]
        actual_result2 = self.matrix1[1, :]
        expected_result2 = [7, 8, 9]
        self.assertEqual(actual_result2, expected_result2,
                         'Test matrix row set')

        # test setting col
        self.matrix1[:, 1] = [9, 10]
        actual_result3 = self.matrix1[:, 1]
        expected_result3 = [9, 10]
        self.assertEqual(actual_result3, expected_result3,
                         'Test matrix col set')

        # test if raises error when number of values is not equal to number of
        # elements in the index
        with self.assertRaises(MatrixError):
            self.matrix1[1, 1] = [1, 2]
        with self.assertRaises(MatrixError):
            self.matrix1[1, :] = [1, 2, 3, 4]

    def test_matrix_swap_rows(self):
        '''Test matrix row swap'''
        # test correct row swap
        self.matrix1.swap_rows(0, 1)
        actual_result = self.matrix1
        expected_result = Matrix(2, 3, [4, 5, 6, 1, 2, 3])
        self.assertEqual(actual_result, expected_result, 'Test row swap')

        # test if raises error with invalid row input
        with self.assertRaises(MatrixError):
            self.matrix1.swap_rows(1, 5)

    def test_matrix_swap_cols(self):
        '''Test matrix col swap'''
        # test correct col swap
        self.matrix1.swap_cols(0, 1)
        actual_result = self.matrix1
        expected_result = Matrix(2, 3, [2, 1, 3, 5, 4, 6])
        self.assertEqual(actual_result, expected_result, 'Test col swap')

        # test if raises error with invalid col input
        with self.assertRaises(MatrixError):
            self.matrix1.swap_cols(1, 5)

    def test_matrix_transpose(self):
        '''Test matrix transpose'''
        actual_result = self.matrix1.transpose()
        expected_result = Matrix(3, 2, [1, 4, 2, 5, 3, 6])
        self.assertEqual(actual_result, expected_result,
                         'Test matrix transpose')

    def test_matrix_all_numbers(self):
        '''Test if all numbers in matrix'''
        # test if all numbers when matrix has all numbers
        actual_result1 = self.matrix1.all_numbers()
        expected_result1 = True
        self.assertEqual(actual_result1, expected_result1,
                         'Test if true when matrix has all numbers')

        # test if all numbers when matrix has a string
        actual_result2 = self.matrix5.all_numbers()
        expected_result2 = False
        self.assertEqual(actual_result2, expected_result2,
                         'Test if false when matrix has a string')

    def test_matrix_all_strings(self):
        '''Test if all strings in matrix'''
        # test if all strings when matrix has all strings
        actual_result1 = self.matrix8.all_strings()
        expected_result1 = True
        self.assertEqual(actual_result1, expected_result1,
                         'Test if true when matrix has all strings')

        # test if all strings when matrix has a number
        actual_result2 = self.matrix1.all_strings()
        expected_result2 = False
        self.assertEqual(actual_result2, expected_result2,
                         'Test if false when matrix has a number')


class TestOneDMatrixMethods(unittest.TestCase):
    '''Unittests for 1 dimension matrix class methods'''
    def setUp(self):
        ''' Objects to use for tests'''
        self.onedmatrix1 = OneDMatrix(3, 'row', [1, 2, 3])
        self.onedmatrix2 = OneDMatrix(3, 'col', [1, 2, 3])
        self.onedmatrix3 = OneDMatrix(3)

    def test_one_d_matrix_init(self):
        '''Test one d matrix initialization'''
        # test init of one d matrix as a row vector
        actual_result1 = str(self.onedmatrix1)
        expected_result1 = '[1, 2, 3]'
        self.assertEqual(actual_result1, expected_result1,
                         'Test if row vector is created')

        # test init of one d matrix as a col vector
        actual_result2 = str(self.onedmatrix2)
        expected_result2 = '[1]\n[2]\n[3]'
        self.assertEqual(actual_result2, expected_result2,
                         'Test if col vector is created')

        # test init of one d matrix as a zero row vector
        actual_result3 = str(self.onedmatrix3)
        expected_result3 = '[0, 0, 0]'
        self.assertEqual(actual_result3, expected_result3,
                         'Test if zero row vector is created')

        # test if raises error with incorrect number of values
        with self.assertRaises(MatrixError):
            OneDMatrix(2, 'row', [2, 'a', 'b'])

    def test_one_d_matrix_get(self):
        '''Test getting elements from one d matrix'''
        # test if able to get element from 1D matrix as a row vector
        actual_result1 = self.onedmatrix1[1]
        expected_result1 = 2
        self.assertEqual(actual_result1, expected_result1,
                         'Test if proper element retrieved')

        # test if able to get element from 1D matrix as a col vector
        actual_result2 = self.onedmatrix2[1]
        expected_result2 = 2
        self.assertEqual(actual_result2, expected_result2,
                         'Test if proper element retrieved')

        # test if able to get entire row vector
        actual_result3 = self.onedmatrix1[:]
        expected_result3 = [1, 2, 3]
        self.assertEqual(actual_result3, expected_result3,
                         'Test if entire vector retrieved')

        # test if error raised when index is out of range
        with self.assertRaises(IndexError):
            self.onedmatrix1[4]
        with self.assertRaises(IndexError):
            self.onedmatrix2[4]

    def test_one_d_matrix_set(self):
        '''Test setting elements in one d matrix'''
        # test setting single element
        self.onedmatrix1[1] = 10
        actual_result1 = self.onedmatrix1[1]
        expected_result1 = 10
        self.assertEqual(actual_result1, expected_result1,
                         'Test one d matrix single element set')

        # test setting entire row
        self.onedmatrix1[:] = [7, 8, 9]
        actual_result2 = self.onedmatrix1[:]
        expected_result2 = [7, 8, 9]
        self.assertEqual(actual_result2, expected_result2,
                         'Test one d matrix row set')

        # test setting entire col
        self.onedmatrix2[:] = [7, 8, 9]
        actual_result3 = self.onedmatrix2[:]
        expected_result3 = [7, 8, 9]
        self.assertEqual(actual_result3, expected_result3,
                         'Test one d matrix col set')

        # test if raises error when list of values is not equal to index
        with self.assertRaises(MatrixError):
            self.onedmatrix1[1] = [1, 2]
        with self.assertRaises(MatrixError):
            self.onedmatrix1[:] = [1, 2, 3, 4]

    def test_one_d_matrix_transpose(self):
        '''Test transpose for one d matrix'''
        # test transposing row vector
        actual_result1 = self.onedmatrix1.transpose()
        expected_result1 = OneDMatrix(3, 'col', [1, 2, 3])
        self.assertEqual(actual_result1, expected_result1,
                         'Test one d matrix row vector transpose')

        # test transposing col vector
        actual_result2 = self.onedmatrix2.transpose()
        expected_result2 = OneDMatrix(3, 'row', [1, 2, 3])
        self.assertEqual(actual_result2, expected_result2,
                         'Test one d matrix col vector transpose')


class TestSquareMatrixMethods(unittest.TestCase):
    '''Unittests for square matrix class methods'''
    def setUp(self):
        '''Object to use for tests'''
        self.squarematrix1 = SquareMatrix(2)
        self.squarematrix2 = SquareMatrix(2, [1, 2, 3, 4])
        self.squarematrix3 = SquareMatrix(2, ['a', 2, 3, 'b'])
        self.squarematrix4 = SquareMatrix(3)

    def test_square_matrix_init(self):
        '''Test square matrix initialization'''
        # test init of zero square matrix
        actual_result1 = str(self.squarematrix1)
        expected_result1 = '[0, 0]\n[0, 0]'
        self.assertEqual(actual_result1, expected_result1,
                         'Test if zero square matrix is created')

        # test init of filled square matrix
        actual_result2 = str(self.squarematrix2)
        expected_result2 = '[1, 2]\n[3, 4]'
        self.assertEqual(actual_result2, expected_result2,
                         'Test if filled square matrix is created')

        # test if raises error with incorrect number of values inputted
        with self.assertRaises(MatrixError):
            SquareMatrix(2, [2, 'a', 'b'])

    def test_square_matrix_get_diagonal(self):
        '''Test retrieving diagonal'''
        # test getting diagonal from zero square matrix
        actual_result1 = self.squarematrix1.get_diagonal()
        expected_result1 = [0, 0]
        self.assertEqual(actual_result1, expected_result1,
                         'Test get diagonal for zero square matrix')

        # test getting diagonal from filled square matrix
        actual_result2 = self.squarematrix2.get_diagonal()
        expected_result2 = [1, 4]
        self.assertEqual(actual_result2, expected_result2,
                         'Test get diagonal for filled square matrix')

        # test getting diagonal from filled square matrix containing strings
        actual_result3 = self.squarematrix3.get_diagonal()
        expected_result3 = ['a', 'b']
        self.assertEqual(actual_result3, expected_result3,
                         'Test get diagonal for square matrix with strings')

    def test_square_matrix_set_diagonal(self):
        '''Test setting diagonal'''
        # test setting diagonal in zero square matrix
        self.squarematrix1.set_diagonal([1, 2])
        actual_result1 = self.squarematrix1.get_diagonal()
        expected_result1 = [1, 2]
        self.assertEqual(actual_result1, expected_result1,
                         'Test set diagonal for zero square matrix')

        # test setting diagonal in filled square matrix
        self.squarematrix2.set_diagonal([5, 5])
        actual_result2 = self.squarematrix2.get_diagonal()
        expected_result2 = [5, 5]
        self.assertEqual(actual_result2, expected_result2,
                         'Test set diagonal for filled square matrix')

        # test if raises error when number of values is not equal to diagonal
        # length
        with self.assertRaises(MatrixError):
            self.squarematrix1.set_diagonal([1, 2, 3])

    def test_square_matrix_determinant(self):
        '''Test determinant'''
        # test if determinant obtained for 2x2 matrix with only numbers
        actual_result1 = self.squarematrix2.determinant()
        expected_result1 = -2
        self.assertEqual(actual_result1, expected_result1, 'Test determinant')

        # test if raises error with strings in matrix
        with self.assertRaises(MatrixError):
            self.squarematrix3.determinant()

        # test if raises error when not a 2x2 matrix
        with self.assertRaises(MatrixError):
            self.squarematrix4.determinant()

    def test_square_matrix_transpose(self):
        '''Test transpose for square matrix'''
        actual_result = self.squarematrix2.transpose()
        expected_result = SquareMatrix(2, [1, 3, 2, 4])
        self.assertEqual(actual_result, expected_result,
                         'Test square matrix transpose')


class TestIdentityMatrixMethods(unittest.TestCase):
    '''Unittests for identity matrix class methods'''
    def setUp(self):
        '''Objects to use for tests'''
        self.identitymatrix1 = IdentityMatrix(2)
        self.identitymatrix2 = IdentityMatrix(2, 5)

    def test_identity_matrix_init(self):
        '''Test identity matrix initialization'''
        # test init of zero identity matrix
        actual_result1 = str(self.identitymatrix1)
        expected_result1 = '[1, 0]\n[0, 1]'
        self.assertEqual(actual_result1, expected_result1,
                         'Test if identity matrix with 1 is created')

        # test init of filled identity matrix
        actual_result2 = str(self.identitymatrix2)
        expected_result2 = '[5, 0]\n[0, 5]'
        self.assertEqual(actual_result2, expected_result2,
                         'Test if identity matrix with value is created')

    def test_identity_matrix_transpose(self):
        '''Test transpose for identity matrix'''
        actual_result = self.identitymatrix2.transpose()
        expected_result = self.identitymatrix2
        self.assertEqual(actual_result, expected_result,
                         'Test identity matrix transpose')

    def test_identity_matrix_set_diagonal(self):
        '''Test setting diagonal'''
        # test setting diagonal in identity matrix
        self.identitymatrix1.set_diagonal(3)
        actual_result1 = self.identitymatrix1.get_diagonal()
        expected_result1 = [3, 3]
        self.assertEqual(actual_result1, expected_result1,
                         'Test set diagonal for identity matrix')

        # test if raises error when value is not an int, float or str
        with self.assertRaises(MatrixError):
            self.identitymatrix1.set_diagonal([1, 2])

    def test_identity_matrix_set(self):
        '''Test raising error if setting individual value, row or col'''
        with self.assertRaises(MatrixError):
            self.identitymatrix1[0, :] = [1, 2]


class TestSymmetricMatrixMethods(unittest.TestCase):
    '''Unittests for symmetric matrix class methods'''
    def setUp(self):
        '''Objects to use for tests'''
        self.symmetricmatrix1 = SymmetricMatrix(2)

    def test_symmetric_matrix_init(self):
        '''Test symmetric matrix initialization'''

        # test init of symmetric matrix
        actual_result1 = str(self.symmetricmatrix1)
        expected_result1 = '[0, 0]\n[0, 0]'
        self.assertEqual(actual_result1, expected_result1,
                         'Test if zero symmetric matrix is created')

    def test_symmetric_set(self):
        '''Test setting symmetric matrix'''
        # tests if changing an element in symmetric matrix also changes the
        # mirrored element along the diagonal
        self.symmetricmatrix1[1, 0] = 2
        actual_result = self.symmetricmatrix1[1, 0] == \
            self.symmetricmatrix1[0, 1]
        expected_result = True
        self.assertEqual(actual_result, expected_result,
                         'Test for symmetric element set')

        # test if raises error when number of values is not equal to number of
        # elements in the index
        with self.assertRaises(MatrixError):
            self.symmetricmatrix1[1, 1] = [1, 2]

    def test_symmetric_matrix_transpose(self):
        '''Test transpose for symmetric matrix'''
        self.symmetricmatrix1[1, 0] = 2
        actual_result = self.symmetricmatrix1.transpose()
        expected_result = self.symmetricmatrix1
        self.assertEqual(actual_result, expected_result,
                         'Test symmetric matrix transpose')

if __name__ == '__main__':
    unittest.main(exit=False)
