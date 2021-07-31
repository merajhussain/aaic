import numpy as np
from numpy.core.fromnumeric import prod


def readMatrix(rows,cols,matrix1):
    print("enter the matrix row by row:")
    
    for row in range(rows):
        rowVals = [int(marks) for marks in input().split()]
        if len(rowVals) != cols:
            print("Wrong column length,quitting the program")
            return False
        matrix1.append(rowVals)
    
    return True




m1rows = int(input("Enter the number of rows for matrix1:"))
m1cols = int(input("Enter the number of columns for maxtrix1:"))
  
m2rows = int(input("Enter the number of rows for matrix2:"))
m2cols = int(input("Enter the number of columns for maxtrix2:"))
 
if m1cols != m2rows:
    print('''Error:number of rows in first matrix should be
             equal to columns in second row''')
    quit()

matrix1 = []
matrix2 = []

if readMatrix(m1rows,m1cols,matrix1) == False or readMatrix(m2rows,m2cols,matrix2) == False:
    quit()

 
product = np.matmul(np.array(matrix1),np.array(matrix2)) 
print(product)
 




 



