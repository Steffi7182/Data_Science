print("Name:Steffi Antony")
print("Reg no:SJC23MCA-2054")
import numpy as np
array_2d = np.array([ [4 + 6j, 3 + 8j, 4 + 6j], [7 + 8j, 7 + 10j,
         12 + 13j] ], dtype=complex)
print("2D Array:")
print(array_2d)
rows, columns = array_2d.shape
print("\nNumber of Rows:", rows)
print("Number of Columns:", columns)
dimensions = array_2d.ndim
print("\nDimensions of the Array:", dimensions)
reshaped_array = array_2d.reshape(3, 2)
print("\nReshaped Array (3x2):")
print(reshaped_array) 
