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


    def transpose(self, matrix=None):
        if matrix:
            # assert type(matrix) == "np.ndarray"
            if type(matrix) == "np.ndarray":
                matrix = matrix.tolist()

            return list(map(list, zip(*self.matrix)))
    
    def rotate_matrix(self, matrix=None):
        return

    def get_shape(self):
        if self.is_valid_matrix:
            return (len(self.inputlist), len(self.inputlist[0]))
        else:
            raise ValueError("Rows of matrix having different dimentions")

    def is_square(self):
        print(self.shape)
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
    
    def get_uniform_mats(self, digit):
        return [[digit]*self.shape[1]] * self.shape[0]
    
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
        return self.get_uniform_mats(0)
    
    def ones(self, shape):
        self.validate_shape(shape)        
        return self.get_uniform_mats(1)
        
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


# test_ip = [[1,2,3], [4,5,6], [7,8,9]]
# mult_m = [[11,12,13], [14,15,16], [17,18,19]]

test_ip = [[1, 0], [0,1]]
conca_m = [[9,9]]
mult_m = [[1,2], [3,4]]
mo = matrix_ops(test_ip)
mult_o = matrix_ops(mult_m)
conca_o = matrix_ops(conca_m)

print(mo.shape)
print(mo.transpose(test_ip))
print(mo.concatenate(conca_o))
print(mo.ones((3,4)))

print(mo.identity(4))
print(mo.outer(mult_o))