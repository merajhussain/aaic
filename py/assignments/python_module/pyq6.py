import math
import re
# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input strings

def getCoeffs(line):
    #taken below line from stackoverflow
    #https://stackoverflow.com/questions/56948506/how-to-extract-coefficients-from-a-line-equation-in-python-without-using-numpy
    coeffs= [float(i) for i in re.split('[xy]', line)]
    return coeffs[0],coeffs[1],coeffs[2]


def isAboveLine(x,y,line):
    a,b,c=getCoeffs(line)
    if ((x*a)+(b*y)+(c)) > 0 and b > 0:
        return True
    if ((x*a)+(b*y)+(c)) < 0 and b < 0:
        return True

    return False 
# you can free to change all these codes/structure
def i_am_the_one(red,blue,line):
    
    rabove=0
    rbelow=0
    for r in red:
        if isAboveLine(r[0],r[1],line):
            rabove += 1
        else:
            rbelow += 1
    
    babove=0
    bbelow=0
    for b in blue:
        if isAboveLine(b[0],b[1],line):
            babove += 1
        else:
            bbelow += 1
    
    if bbelow > 0 and babove > 0:
        return "NO"
    if rbelow > 0 and rbelow > 0:
        return "NO"

    if rabove == len(red) and bbelow == len(blue):
        return "YES"
    if rbelow == len(red) and babove == len(blue):
        return "YES"

    # your code
    return "NO"

#Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
##Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
#Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

nr=int(input("enter number of points for red:"))
Red=[]
for i in range(nr):
    x=float(input("enter x coordinate for point "+str(i+1)+":"))
    y=float(input("enter y coordinate for point "+str(i+1)+":"))
    Red.append((x,y))

nb=int(input("enter number of points for blue:"))
Blue=[]
for i in range(nb):
    x=float(input("enter x coordinate for point "+str(i+1)+":"))
    y=float(input("enter y coordinate for point "+str(i+1)+":"))
    Blue.append((x,y))

Lines=[]
nl=int(input("enter number of lines:"))
for i in range(nl):
    line=input("enter equation for line"+str(i+1)+":")
    Lines.append(line)


for i in Lines:
    yes_or_no = i_am_the_one(Red, Blue, i)
    print(yes_or_no) # the returned value