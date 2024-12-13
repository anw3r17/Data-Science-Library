import numpy as np

# Define matrix A
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 1. Calculate the determinant of matrix A
determinant_A = np.linalg.det(A)
print("Determinant of matrix A:", determinant_A)

# 2. Find the eigenvalues and eigenvectors of matrix A
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of matrix A:", eigenvalues)
print("Eigenvectors of matrix A:", eigenvectors)

# 3. Compute the matrix inverse of A
A_inverse = np.linalg.inv(A)
print("Inverse of matrix A:")
print(A_inverse)

# 4. Perform a matrix multiplication between matrix A and its transpose
A_transpose = np.transpose(A)
A_times_A_transpose = np.matmul(A, A_transpose)
print("Matrix multiplication between A and its transpose:")
print(A_times_A_transpose)

# 5. Solve the system of linear equations Ax = b, where b = [1, 2, 3]
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)
print("Solution of the system of linear equations Ax = b:", x)
