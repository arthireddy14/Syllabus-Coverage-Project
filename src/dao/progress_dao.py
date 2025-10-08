# # src/dao/progress_dao.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in project root

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in .env file")

sb: Client = create_client(url, key)


# class ProgressDAO:
#     def add_progress(self, sid: int, tpid: int, completion_per: int, lastupdate: str = None):
#         payload = {"sid": sid, "tpid": tpid, "completion_per": completion_per, "lastupdate": lastupdate}
#         resp = sb.table("progress2").insert(payload).execute()
#         return resp.data

#     def update_progress(self, sid: int, tpid: int, completion_per: int, lastupdate: str = None):
#         resp = sb.table("progress2").update({"completion_per": completion_per, "lastupdate": lastupdate}) \
#                  .eq("sid", sid).eq("tpid", tpid).execute()
#         return resp.data

#     def get_progress_by_student(self, sid: int):
#         resp = sb.table("progress2").select("*").eq("sid", sid).execute()
#         return resp.data
from datetime import datetime

class ProgressDAO:
    def calculate_completion_percentage(self, sid: int):
        """Compute % of completed topics for given student."""
        # change sid -> syid based on DB column name
        all_topics = sb.table("topics1").select("status").eq("syid", sid).execute().data

        if not all_topics:
            return 0

        total = len(all_topics)
        completed = sum(1 for t in all_topics if t["status"].lower() == "completed")

        return int((completed / total) * 100)


    def add_progress(self, sid: int, tpid: int, lastupdate: str = None):
        completion_per = self.calculate_completion_percentage(sid)
        if not lastupdate:
            lastupdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        payload = {"sid": sid, "tpid": tpid, "completion_per": completion_per, "lastupdate": lastupdate}
        resp = sb.table("progress2").insert(payload).execute()
        return resp.data

    def update_progress(self, sid: int, tpid: int, lastupdate: str = None):
        completion_per = self.calculate_completion_percentage(sid)
        if not lastupdate:
            lastupdate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        resp = sb.table("progress2").update(
            {"completion_per": completion_per, "lastupdate": lastupdate}
        ).eq("sid", sid).eq("tpid", tpid).execute()

        return resp.data

    def get_progress_by_student(self, sid: int):
        resp = sb.table("progress2").select("*").eq("sid", sid).execute()
        return resp.data
