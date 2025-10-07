# from src.dao.student_dao import StudentDAO
# from typing import Optional
# class StudentService:
#     def __init__(self):
#         self.dao=StudentDAO()
#         pass
#     def register_stu(self,sid:int,sname:str,course:Optional[str]|None):
#         return self.dao.add_student(sid,sname,course)
#     def get_student(self,sid:int):
#         stu1=self.dao.search_student(sid)
#         if not stu1:
#             return f"Not found student of id {sid}"
#         return stu1
#     def update_sdetails(self,sid:int,details:dict):
#         return self.dao.update_details(sid,details)
    
    
    
# src/services/student_service.py
from src.dao.student_dao import StudentDAO

class StudentService:
    def __init__(self):
        self.dao = StudentDAO()

    def register_stu(self, sid: int, name: str, course: str):
        # Call DAO to insert student
        return self.dao.add_student(sid, name, course)

    def get_student(self, sid: int):
        # Call DAO to search student
        return self.dao.search_student(sid)

    def update_sdetails(self, sid: int, details: dict):
        # Call DAO to update details
        return self.dao.update_details(sid, details)

        