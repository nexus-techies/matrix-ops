import matrixops as mops

test_ip = [[2, 3], [1,4]]
# test_ip = [[1,2,3], [4,5,6], [7,8,9]]

mo = mops.matrix_ops(test_ip)

print("shape of matrix: ", mo.shape)

# square
print("squared matrix: ", mo.square())

# transpose
print("\ntransposed matrix: ")
print(mo.transpose(test_ip))

# concatenate
conca_m = [[9,9]]
# conca_m = [[11,12,13], [23,24,25]]
conca_o = mops.matrix_ops(conca_m)
print(f"\nconcatenated matrix with {conca_m}: ")
print(mo.concatenate(conca_o))

# special matrices
print("\nspecial matrices:")
print(mo.ones((1,3)))
print(mo.zeros((3,4)))
print(mo.identity(4))

# cartesian
mult_m = [[1,2], [3,4]]
# mult_m = [[1,2,3], [4,5,6], [7,8,9]]
mult_o = mops.matrix_ops(mult_m)

print(f"\ninner product with {mult_m}: ")
print(mo.inner(mult_o))

print(f"\nouter product with {mult_m}:")
print(mo.outer(mult_o))