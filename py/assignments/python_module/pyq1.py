

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
    print('''Error:number of columns in first matrix should be
             equal to rows in second matrix''')
    quit()

matrix1 = []
matrix2 = []

if readMatrix(m1rows,m1cols,matrix1) == False or readMatrix(m2rows,m2cols,matrix2) == False:
    quit()

 
product=[]

for i in range(m1rows):
    row=[]
    res=0
    for j in range(m2cols):
        res=0
        for k in range(m2rows):
            res += matrix1[i][k]*matrix2[k][j]
            if k == m2rows-1:
                row.append(res)
                #print(res)
                #print(row)
                #res=0
    product.append(row)



print(product)