# src/services/progress_service.py
from src.dao.progress_dao import ProgressDAO

class ProgressService:
    def __init__(self):
        self.dao = ProgressDAO()

    def mark_topic_progress(self, sid: int, tpid: int, completion_per: int, lastupdate: str = None):
        # Check if progress exists
        existing = self.dao.get_progress_by_student(sid)
        for p in existing:
            if p['tpid'] == tpid:
                return self.dao.update_progress(sid, tpid, completion_per, lastupdate)
        # If not exists, add new
        return self.dao.add_progress(sid, tpid, completion_per, lastupdate)

    def get_student_progress(self, sid: int):
        return self.dao.get_progress_by_student(sid)
