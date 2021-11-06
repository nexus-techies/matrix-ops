import numpy as np

class matrix_ops():
    def __init__(self, inputlist):
        self.inputlist = inputlist
        self.matrix = np.array(inputlist)

        _elem_map = list(map(lambda x:len(self.inputlist[x]), range(0, len(self.inputlist))))
        if _elem_map.count(_elem_map[0]) == len(_elem_map):
            self.is_valid_matrix = True
        else:
            self.is_valid_matrix = False
        
        self.shape = self.get_shape()


    def get_shape(self):
        if self.is_valid_matrix:
            return (len(self.inputlist), len(self.inputlist[0]))
        else:
            raise ValueError("Rows of matrix having different dimentions")


    def square(self):
        result_mat = []
        for row in self.inputlist:
            _temp = []
            for value in row:
                _temp.append(value**2)
            result_mat.append(_temp)
        
        return result_mat


    def transpose(self, matrix=None):
        if matrix:
            # assert type(matrix) == "np.ndarray"
            if type(matrix) == "np.ndarray":
                matrix = matrix.tolist()

            return list(map(list, zip(*self.matrix)))
    
    def rotate_matrix(self, matrix=None):
        return
        # if not len(mat):
        #     return
        # top = 0
        # bottom = len(mat)-1
        # left = 0
        # right = len(mat[0])-1
        # while(left < right and top < bottom):
        #     prev = mat[top+1][left]
        #     for i in range(left, right+1):
        #         curr = mat[top][i]
        #         mat[top][i] = prev
        #         prev = curr
        #     top += 1
        #     for i in range(top, bottom+1):
        #         curr = mat[i][right]
        #         mat[i][right] = prev
        #         prev = curr
        #     right -= 1
        #     for i in range(right, left-1, -1):
        #         curr = mat[bottom][i]
        #         mat[bottom][i] = prev
        #         prev = curr
        #     bottom -= 1
        #     for i in range(bottom, top-1, -1):
        #         curr = mat[i][left]
        #         mat[i][left] = prev
        #         prev = curr
        #     left += 1
        # return mat


    def is_square(self):
        if self.shape[0] == self.shape[1]:
            return True
        else:
            return False
   
    def concatenate(self, concact_mat):
        if type(concact_mat.inputlist) == "np.ndarray":
            concact_mat = concact_mat.tolist()

        if self.shape[1] != concact_mat.shape[1]:
            raise TypeError(f"Two matrices are having different shapes, \
{self.shape} and {concact_mat.shape} respectively.")

        first_mat = list(self.inputlist)
        first_mat.append(list(concact_mat.inputlist))

        return first_mat
    
    def get_uniform_mats(self, digit, shape):
        return [[digit]*shape[1]] * shape[0]
    
    def validate_shape(self, shape):
        if isinstance(shape, int):
            if shape < 1:
                raise ValueError("Invalide shape dimentions")
            self.size = (1, shape)
        else:
            if len(shape) < 1:
                raise ValueError("Invalide shape dimentions")
            self.size = tuple(shape)

    def zeros(self, shape):
        self.validate_shape(shape)        
        return self.get_uniform_mats(0, shape)
    
    def ones(self, shape):
        self.validate_shape(shape)        
        return self.get_uniform_mats(1, shape)
        
    def identity(self, shape):
        if not isinstance(shape, int):
            raise TypeError("Shape of Identity matrix must be an integer")
        
        base = [] # self.zeros((shape, shape))
        for loc in range(shape):
            _temp = [0]*shape
            _temp[loc] = 1
            base.append(_temp)
        return base
    
    def inner(self, mult_matrix):
        if self.shape != mult_matrix.shape:
            raise ValueError("Matrix shape isn't matching")
        
        if self.shape[0] == mult_matrix.shape[0] == 1:
            return sum([a*b for a,b in zip(self.inputlist[0],mult_matrix.inputlist[0])])

        if not self.is_square() or not mult_matrix.is_square():
            raise ValueError("Matrix is not a square matrix")
        else:
            prod_mat = []
            for row in self.inputlist:
                _row_data = []
                for row_2 in mult_matrix.inputlist:
                    _row_data.append(sum([a*b for a,b in zip(row,row_2)]))
                
                prod_mat.append(_row_data) 
            return prod_mat

    def outer(self, mult_matrix):      
        if self.shape[0] == mult_matrix.shape[0] == 1:
            return None
        if not self.is_square() or not mult_matrix.is_square():
            raise ValueError("Matrix is not a square matrix")
        else:
            prod_mat = []
            for row in self.inputlist:
                for num in row:
                    if not num:
                        _a = mult_matrix.shape
                        prod_mat.append([0]*_a[0]*_a[1])
                        continue

                    _row_data = []
                    for row_2 in mult_matrix.inputlist:
                        for num_2 in row_2:
                            _row_data.append(num*num_2)
                    
                    prod_mat.append(_row_data)
        
            return prod_mat

