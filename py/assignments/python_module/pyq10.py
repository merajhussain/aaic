import math
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings


# you can free to change all these codes/structure
def compute_log_loss(A):
    # your code
    sum = 0.0
    for row in A:
        try:
          sum += (abs(row[0])*math.log10(row[1]))+(abs(1-row[0])*math.log10(abs(1-row[1])))
        except:
            pass
      
    loss = (-1*sum)/len(A)
    return loss

#A = [[1, 0.4], [0, 0.5], [0, 0.9], [0, 0.3], [0, 0.6], [1, 0.1], [1, 0.9], [1, 0.8]]
nrows=int(input("enter number of rows:"))
A=[]
for row in range(nrows):
    rowvals=[float(vals) for vals in input().split()]
    if(len(rowvals)) !=2:
        print("only 2 values allowed in a row")
        quit()
    A.append(rowvals)


print(A)
loss = compute_log_loss(A)
print(loss)