from src.services.student_service import StudentService
class StudentCLI:
    def __init__(self):
        self.s1=StudentService()
        pass
    def menu(self):
        while True:
            print("1.Register student")
            print("2.Get student by id")
            print("3.Update student by id")
            print("4.Exit")
            ch=int(input("Enter your choice "))
            if(ch==1):
                sid=int(input("Enter the id "))
                n=input("Enter the name ")
                c=input("Enter the course ")
                res=self.s1.register_stu(sid,n,c)
                print("Registered ",res)
            elif(ch==2):
                sid=int(input("Enter student id for viewing "))
                res=self.s1.get_student(sid)
                print("Student details ",res)
            elif(ch==3):
                sid=int(input("Enter student id for viewing "))
                f=input("Enter field to update(sname/course) ")
                v=input()
                res=self.s1.update_sdetails(sid,{f:v})
                print("Updated ",res)
            elif(ch==4):
                print("Exiting...")
                break
            else:
                print("Invalid choice,try again")
        