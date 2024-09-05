print("Name:Steffi Antony")
print("Reg no:SJC23MCA-2054")
import numpy as np;
arr_id = np.array([1,2,3,4,5])
diagonal_matrix = np.diag(arr_id)
print("1D array:")
print(arr_id)
print("\nDiagonal_matrix:")
print(diagonal_matrix)
arr_2d_square = np.array([[1,2,3],[4,5,6],[7,8,9]])
diagonal_element = np.diag(arr_2d_square)
print("\n2D square matrix:")
print(arr_2d_square)
print("\n Diagonal Elements:")
print(diagonal_element )
arr_2d_non_square = np.array([[1,2,3],
                              [4,5,6],
                              [7,8,9]])
diagonal_elements_non_square = np.diag(arr_2d_non_square)
print("\n2D Non-square matrix:")
print(arr_2d_non_square)
print("\n Diagonal Elements(Non-square):")
print(diagonal_elements_non_square)




