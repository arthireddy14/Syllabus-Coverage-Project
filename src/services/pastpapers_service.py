# src/services/pastpapers_service.py
from src.dao.pastpapers_dao import PastPapersDAO

class PastPapersService:
    def __init__(self):
        self.dao = PastPapersDAO()

    def upload_paper(self, syid: int,tpid:int, title: str, year: int,marks:int, file_url: str = None):
        return self.dao.add_paper(syid,tpid, title, year,marks, file_url)

    def list_papers(self, syid: int):
        return self.dao.get_papers_by_syllabus(syid)

    def remove_paper(self, pid: int):
        return self.dao.delete_paper(pid)
