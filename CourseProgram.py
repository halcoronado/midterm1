'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left 
for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''

from distutils import core
import CourseClass as cc

def main():

    name = 'MIS 4322 - Advanced Python'
    crn = '250309'
    seats = 4
    status = 'open'
    students = ['John','James','Jill','Jack','Joanne']
    course_obj = cc.Course(name, crn, seats,status)

    for x in students:
       reg_obj = cc.Register(x,crn)

       if course_obj.get_seats() > 0:
         print ("Student Name:", reg_obj.get_name())
         print("Course Name:", course_obj.get_name())
         print ("CRN: ", course_obj.get_crn())
         course_obj.update_seat_count()
         print ("Seats left:", course_obj.get_seats())
       else:
         print("Sorry ",reg_obj.get_name(),", registration is closed for ", course_obj.get_name() , sep="")
       

    
main()



        
    
    
