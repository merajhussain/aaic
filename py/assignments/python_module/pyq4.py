import operator
 


# you can free to change all these codes/structure
def display_dash_board(students, marks):
    #print(len(students))
    #print(len(marks))

    markList = dict()
    
    
    mLen = len(students)

    if mLen < 5:
        print("Warning: Number of students is less than 5 so only top "
              +str(mLen)+" and bottom "+str(mLen)+" students marks will be displayed")
    
      

    #build the dictionary with students and marks data
    for i in range(len(students)):
        markList[students[i]]=marks[i]
    mlPairs = dict(sorted(markList.items(),key=operator.itemgetter(1)));  
    mlPairsRev = dict(sorted(markList.items(),key=operator.itemgetter(1),reverse=True));  
     
   # write code for computing top top 5 and least 5 students
    top_5_students = dict()
    least_5_students = dict()

    index=0
    for pair in mlPairs.items():
        if  index  <  5:
            least_5_students[pair[0]]=pair[1]
        index +=1
    
    index =0
    for pair in mlPairsRev.items():
        if  index  <  5:
            top_5_students[pair[0]]=pair[1]
        index +=1

     
   
    # write code for computing students between 25 and 75
    #filter out students marks > 25 and then filter out
    #students with marks < 75
    students_gt_25 = {student:score for student,score in markList.items() if score>25} 
    students_within_25_and_75 = {student:score for student,score in students_gt_25.items() if score<75} 
    

    
    return top_5_students, least_5_students, students_within_25_and_75

 

#driver code below
print("enter student name seperated by space:")

#input reading logic taken from stackoverflow
#https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
students = [str(student) for student in input().split()]

print("enter marks name seperated by space:")

Marks = [int(marks) for marks in input().split()]

if len(students) != len(Marks):
        print("Error:count of studends and marks should be equal")
        quit()

top_5_students, least_5_students, students_within_25_and_75 = display_dash_board(students, Marks)
print("top 5 students:")
print(top_5_students)
print("least 5 students:")
print(least_5_students)
print("students who between scored 25 and 75 marks:")
print(students_within_25_and_75)
