# src/dao/pastpapers_dao.py
import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

class PastPapersDAO:
    def add_paper(self, syid: int,tpid:int, title: str, year: int,marks:int, file_url: str = None):
        payload = {"syid": syid,"tpid":tpid, "title": title, "year": year,"marks":marks, "file_url": file_url}
        resp = sb.table("pastpapers3").insert(payload).execute()
        return resp.data

    def get_papers_by_syllabus(self, syid: int):
        resp = sb.table("pastpapers3").select("*").eq("syid", syid).execute()
        return resp.data

    def delete_paper(self, pid: int):
        resp = sb.table("pastpapers3").delete().eq("pid", pid).execute()
        return resp.data
