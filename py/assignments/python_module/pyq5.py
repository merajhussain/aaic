import math
import operator

# write your python code here
# you can take the above example as sample input for your program to test
# it should work for any general input try not to hard code for only given input examples
# you can free to change all these codes/structure


# here S is list of tuples and P is a tuple ot len=2
def closest_points_to_p(S, P):
    distances =dict()
    # write your code here
    for i in range(len(S)):
        tup = S[i]
        numerator = P[0]*tup[0]+P[1]*tup[1]
        denominator= math.sqrt(tup[0]**2+tup[1]**2)*math.sqrt(P[0]**2+P[1]**2)
        distances[S[i]]=math.acos(numerator/denominator)


    sortedDistances=dict(sorted( distances.items(),key=operator.itemgetter(1)));  
    
    closestPoints = list(sortedDistances.keys())
    return closestPoints[0:5]

#S= [(1,2),(3,4),(-1,1),(6,-7),(0, 6),(-5,-8),(-1,-1)(6,0),(1,-1)]
#P= (3,-4)

S=[]
 
nps = int(input("enter number of points in s:"))

if nps<5:
    print("Number of points should be atleast 5")
    quit()

for i in range(nps):
    print("enter coordinates for point "+str(i+1))
    x=int(input("enter x coordinate:"))
    y=int(input("enter y coordinate:"))
    S.append((x,y))


px=int(input("enter x coordinate for point p:"))
py=int(input("enter y coordinate for point p:"))

P =(px,py)

 
points = closest_points_to_p(S, P)
print(points) #print the returned values