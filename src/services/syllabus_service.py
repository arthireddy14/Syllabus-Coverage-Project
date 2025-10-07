# src/services/syllabus_service.py
from src.dao.syllabus_dao import SyllabusDAO

class SyllabusService:
    def __init__(self):
        self.dao = SyllabusDAO()

    def create_syllabus(self, syid: int, title: str, sid: int):
        return self.dao.add_syllabus(syid, title, sid)

    def add_topic_to_syllabus(self, syid: int, title: str):
        return self.dao.add_topic(syid, title)

    def change_topic_status(self, tid: int, status: str):
        return self.dao.update_status(tid, status)

    def fetch_syllabus(self, syid: int):
        return self.dao.get_syllabus(syid)

    def fetch_topics(self, syid: int):
        return self.dao.get_topics(syid)
