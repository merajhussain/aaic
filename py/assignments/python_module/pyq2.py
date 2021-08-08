from random import uniform
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples


# you can free to change all these codes/structure
def pick_a_number_from_list(A):
    s= sum(A)
    weights=[]
    for val in A:
        weights.append(val/s)
    #print(weights)

    #the below logic is taken from stackoverflow
    cummulativeSum=[0 for i in range(len(weights))]
    cummulativeSum[0]=0
    for val in range(len(weights)-1):
        cummulativeSum[val+1]=cummulativeSum[val]+weights[val+1]

    rnum = uniform(0.0,1.0)
    number =0
    for i in range(len(cummulativeSum)):
        if(rnum<=cummulativeSum[i]):
            number=A[i]
            break

    return number

def sampling_based_on_magnitued(A):
    for i in range(1,100):
        number = pick_a_number_from_list(A)
        print(number)

A=[int(val) for val in input().split()]
sampling_based_on_magnitued(A)