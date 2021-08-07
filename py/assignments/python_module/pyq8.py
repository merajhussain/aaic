# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings
def printProbablity(index,f1,s1,prob1,f2,s2,prob2,f3,s3,prob3):
    p1str="{0}. P(F=={1}|S=={2})={3}), "
    p2str="P(F=={4}|S=={5})={6}), "
    p3str="P(F=={7}|S=={8})={9})"
    finalstr=p1str+p2str+p3str
    print(finalstr.format(index,f1,s1,prob1,
                                  f2,s2,prob2,
                                   f3,s3,prob3 ))

def Probability(f,s,A,flist,slist):
    f1count=flist.count(f)
    s1count=slist.count(s)
    f1s1count= countFS(f,s,A)
    op=str(f1s1count)+'/'+str(s1count)
    return op

def countFS(f,s,A):
    count=0
    for i in A:
        if i[0]==f and i[1]==s:
            count +=1
    
    return count
# you can free to change all these codes/structure
def compute_conditional_probabilites(A):
    f=[]
    s=[]
    #print(A)
    nr=len(A)
    for i in A:
        f.append(str(i[0]))
        s.append(str(i[1]))
    
    #print(f)
    #print(s)
    #logic: p(a/b)=p(a&b)/p(b)
    #p(F==F1|S==S1)
    printProbablity('a','F1','S1',Probability('F1','S1',A,f,s),
                          'F1','S2',Probability('F1','S2',A,f,s),
                          'F1','S3',Probability('F1','S3',A,f,s))
    
    printProbablity('b','F2','S1',Probability('F2','S1',A,f,s),
                          'F2','S2',Probability('F2','S2',A,f,s),
                          'F2','S3',Probability('F2','S3',A,f,s))

    printProbablity('c','F3','S1',Probability('F3','S1',A,f,s),
                          'F3','S2',Probability('F3','S2',A,f,s),
                          'F3','S3',Probability('F3','S3',A,f,s))
    
    printProbablity('d','F4','S1',Probability('F4','S1',A,f,s),
                          'F4','S2',Probability('F4','S2',A,f,s),
                          'F4','S3',Probability('F4','S3',A,f,s))
    
    printProbablity('e','F5','S1',Probability('F5','S1',A,f,s),
                          'F5','S2',Probability('F5','S2',A,f,s),
                          'F5','S3',Probability('F5','S3',A,f,s))
    

    

    #p(F==F1|S==S2)


    # your code
    # print the output as per the instructions
    return

def readInput():
    rows=[]
    nr=int(input("enter number of rows:"))
    for i in range(nr):
        rowVals=[vals.upper() for vals in input().split() ]
        if len(rowVals)!=2:
            print("Error: input only two elements per row")
            quit()
        rows.append(rowVals)
    return rows


#A = [['F1','S1'],['F2','S2'],['F3','S3'],['F1','S2'],['F2','S3'],['F3','S2'],['F2','S1'],['F4','S1'],['F4','S3'],['F5','S1']]
A= readInput()
compute_conditional_probabilites(A)