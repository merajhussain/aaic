#from collections import deque
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings-

# you can free to change all these codes/structure
def curve_smoothing(string):
    print(string)
    delimited=string.split(',')
    #print(delimited)
    i=0
    k=0
    avg=0
    #stack = deque()
    start=0
    end=0
    while i < len(delimited):
        start=end
        end=0
        count=0
        if delimited[i] == '_':
            k=i
            while k < len(delimited):
                if delimited[k]!='_':
                    break
                #stack.append(delimited[k])
                count +=1
                k += 1
        else:
            count=0
            #stack.clear()
            i +=1
            continue
        
        
        if count > 0:
            if delimited[i-1] !='_':
                if start==0 and i!=0:
                    start=int(delimited[i-1])
            if k < len(delimited) and delimited[k] !='_' :
                end=int(delimited[k])
                
        tc=count+(1 if start !=0 else 0)+(1 if end!=0 else 0)
        avg = 0
        if tc !=0:
            avg=(start+end)/tc
        #print(stack)
        #print(avg)
        #print(start)
        #print(end)
        #print(tc)
        #print(i)
        #print(k)
        l=i-1
        h=k
        if i==0:
            l=i
        if k==len(delimited):
            h=k-1
        ri=l
        #print(l)
        #print(h)
        while ri <= h:
            delimited[ri]=avg
            ri +=1
        #stack.clear()
        #print(delimited)
        if k !=0:
            i=k
        else:
            i +=1




           
        
    return delimited


    
#S=  "_,_,30,_,_,_,50,_,_"
#S="_,_,_,24"
#S="80,_,_,_,_"
#S="40,_,_,_,60"
#S="_"
S=input("enter the string to be smoothed:")
smoothed_values= curve_smoothing(S)
string=""
i=0
while i<len(smoothed_values):
    string +=str(smoothed_values[i])
    i +=1
    if i < len(smoothed_values):
        string +=","
   

print(string)