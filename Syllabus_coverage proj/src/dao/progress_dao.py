# src/dao/progress_dao.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

class ProgressDAO:
    def add_progress(self, sid: int, tpid: int, completion_per: int, lastupdate: str = None):
        payload = {"sid": sid, "tpid": tpid, "completion_per": completion_per, "lastupdate": lastupdate}
        resp = sb.table("progress2").insert(payload).execute()
        return resp.data

    def update_progress(self, sid: int, tpid: int, completion_per: int, lastupdate: str = None):
        resp = sb.table("progress2").update({"completion_per": completion_per, "lastupdate": lastupdate}) \
                 .eq("sid", sid).eq("tpid", tpid).execute()
        return resp.data

    def get_progress_by_student(self, sid: int):
        resp = sb.table("progress2").select("*").eq("sid", sid).execute()
        return resp.data
