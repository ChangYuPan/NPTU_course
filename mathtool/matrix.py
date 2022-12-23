# A module contains some matrix operation
# where matrix is a 2-d list

def is_mtx(func):
    '''
    Decorator. Check if the inputs of a function are matrices or not.
    '''
    def warp(*args, **kwargs):
        matrices = list(args) + list(kwargs.values())
        for mtx in matrices:
            if not isinstance(mtx, list):
                print('[NotAMatrixError] Must be a 2-d list.')
                return False
            for i, row in enumerate(mtx):
                if not isinstance(row, list):
                    print('[NotAMatrixError] Each row must be a list.')
                    return False
                for ele in row:
                    if not isinstance(ele, (float, int)):
                        print('[NotAMatrixError] Each element must be a number.')
                        return False
                if i == 0:
                    n_col = len(row)
                else:
                    if n_col != len(row):
                        print('[NotAMatrixError] The length of each row must be equal.')
                        return False
        result = func(*args, **kwargs)
        return result
    return warp

@is_mtx
def get_size(mtx):
    '''
    Get size of a matrix where matrix is a 2-d list
    ---
    @param
        mtx: matrix.
    @return
        (m, n): tuple. means (n_row, n_col)
    ---
    '''
    # n_row
    m = len(mtx)
    # n_col
    n = len(mtx[0])
    return (m, n)
    
@is_mtx
def get_min(mtx):
    '''
    Get minimum element of a matrix where matrix is a 2-d list
    ---
    @param
        mtx: matrix.
    @return
        m: number. Minimum of the matrix
    ---
    '''
    m = mtx[0][0]
    for row in mtx:
        for ele in row:
            if ele < m:
                m = ele
    return m
    
@is_mtx
def get_max(mtx):
    '''
    Get maximum element of a matrix where matrix is a 2-d list
    ---
    @param
        mtx: matrix.
    @return
        M: number. Maximum of the matrix.
    ---
    '''
    M = mtx[0][0]
    for row in mtx:
        for ele in row:
            if ele > M:
                M = ele
    return M
    
@is_mtx
def mtx_transpose(mtx):
    '''
    Get transpose of a matrix where matrix is a 2-d list
    ---
    @param
        mtx: matrix.
    @return
        mtx_T: matrix. Transpose of the matrix
    ---
    '''
    m, n = get_size(mtx)
    mtx_T = [[mtx[j][i] for j in range(m)] for i in range(n)]
    return mtx_T
    
@is_mtx
def mtx_add(mtx1, mtx2):
    '''
    Element-wise of two matrices where each matrix is a 2-d list and have the same size.
    ---
    @param
        mtx1: matrix.
        mtx2: matrix.
    @return
        mtx_new: matrix. Summation of the two matrices
    ---
    '''
    m1, n1 = get_size(mtx1)
    m2, n2 = get_size(mtx2)
    if (m1 != m2) or (n1 != n2):
        print('[MatrixSizeError] Two matrices must have same size.')
        return False
    mtx_new = [[ele1 + ele2 for ele1, ele2 in zip(row1, row2)] for row1, row2 in zip(mtx1, mtx2)]
    return mtx_new
    
@is_mtx
def mtx_mul(mtx1, mtx2):
    '''
    Multiplication of two matrices where each matrix is a 2-d list and the col number of mtx1 must equal to the row number of mtx2.
    ---
    @param
        mtx1: matrix.
        mtx2: matrix.
    @return
        mtx_new: matrix. Product of the two matrices with mtx1 times mtx2
    ---
    '''
    m1, n1 = get_size(mtx1)
    m2, n2 = get_size(mtx2)
    if n1 != m2:
        print('[MatrixSizeError] The column numbrer of mtx1 must equal to the row number of mtx2.')
        return False
    mtx_new = [[0 for j in range(n2)] for i in range(m1)]
    for i in range(m1):
        for j in range(n2):
            for k in range(n1): # m2 either
                mtx_new[i][j] += mtx1[i][k] * mtx2[k][j]
    return mtx_new    



# class Matirx

from itertools import chain
class NotAMatrixError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

class Matrix:
    def __init__(self, data):
        self.data = self._is_matrix(data)
        
    def _is_matrix(self, data):
        if not isinstance(data, list):
            raise NotAMatrixError('Must be a 2-d list.')
        for i, row in enumerate(data):
            if not isinstance(row, list):
                raise NotAMatrixError('Each row must be a list.')
            for ele in row:
                if not isinstance(ele, (float, int)):
                    raise NotAMatrixError('Each element must be a number.')
            if i == 0:
                n_col = len(row)
            else:
                if n_col != len(row):
                    raise NotAMatrixError('The length of each row must be equal.')
        return data
    
    def size(self):
        # n_row
        m = len(self.data)
        # n_col
        n = len(self.data[0])
        return (m, n)
    
    def min(self):
        m = self.data[0][0]
        for row in self.data:
            for ele in row:
                if ele < m:
                    m = ele
        return m
    
    def max(self):
        M = self.data[0][0]
        for row in self.data:
            for ele in row:
                if ele > M:
                    M = ele
        return M
    
    def T(self):
        '''Return transpose matrix'''
        m, n = self.size()
        data = [[self.data[j][i] for j in range(m)] for i in range(n)]
        return Matrix(data)
    
    def __str__(self):
        m, n = self.size()
        extent_data = list(chain(*self.data))
        width = max(map(lambda x: len(str(x)), extent_data))
        is_float = any(map(lambda x: isinstance(x, float), extent_data))
        extent_data = list(map(str, extent_data))
        empty_space = ' ' * ((width+2) * n)
        ele_templ = f' {{:>{width}s}} ' * n
        empty_line = f'|{empty_space}|'
        ele_line = f'|{ele_templ}|'
        fmt = [empty_line] + [ele_line for _ in range(m)] + [empty_line]
        fmt = '\n'.join(fmt)
        return fmt.format(*extent_data)
    
    def __repr__(self):
        return self.__str__()
    
    def __getitem__(self, idx):
        '''Return the idx-th column as a nx1 matrix'''
        data = []
        for r in self.data:
            tmp = [r[idx]]
            data.append(tmp)
        return Vector(data)
    
    def __add__(self, other):
        m1, n1 = self.size()
        m2, n2 = other.size()
        if (m1 != m2) or (n1 != n2):
            raise MatrixSizeError('Two matrices must have same size.')
        data = [[ele1 + ele2 for ele1, ele2 in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)]
        return Matrix(data)
    
    def __sub__(self, other):
        m1, n1 = self.size()
        m2, n2 = other.size()
        if (m1 != m2) or (n1 != n2):
            raise MatrixSizeError('Two matrices must have same size.')
        data = [[ele1 - ele2 for ele1, ele2 in zip(row1, row2)] for row1, row2 in zip(self.data, other.data)]
        return Matrix(data)
    
    def __mul__(self, other):
        m1, n1 = self.size()
        m2, n2 = other.size()
        if n1 != m2:
            raise MatrixSizeError('The column numbrer of mtx1 must equal to the row number of mtx2.')
        data = [[0 for j in range(n2)] for i in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(n1): # m2 either
                    data[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(data)
    
    
class Vector(Matrix):    
    def __init__(self, data):
        super().__init__(data=data)
        
    def _is_matrix(self, data):
        if len(data) != 1 and len(data[0]) != 1:
            raise NotAVectorError('Must be a 2-d list with shape (1, n) or (m, 1).')
        return super()._is_matrix(data)
    
    def __getitem__(self, idx):
        '''Return the idx-th element'''
        return self.data[idx]