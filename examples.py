import matrixops as mops

test_ip = [[2, 0], [0,4]]
# test_ip = [[1,2,3], [4,5,6], [7,8,9]]

mo = mops.matrix_ops(test_ip)

print(mo.shape)

# square
print(mo.square())

# transpose
print(mo.transpose(test_ip))

# # concatenate
conca_m = [[9,9]]
conca_o = mops.matrix_ops(conca_m)
print(mo.concatenate(conca_o))

# special matrices

print(mo.ones((1,3)))
print(mo.zeros((3,4)))
print(mo.identity(4))

# cartesian

mult_m = [[1,2], [3,4]]
mult_o = mops.matrix_ops(mult_m)

print(mo.inner(mult_o))
print(mo.outer(mult_o))