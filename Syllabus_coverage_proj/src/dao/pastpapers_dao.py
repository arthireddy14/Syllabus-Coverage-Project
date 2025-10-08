# src/dao/pastpapers_dao.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in project root

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in .env file")

sb: Client = create_client(url, key)


class PastPapersDAO:
    def add_paper(self, syid: int,tpid:int, title: str, year: int,marks:int, file_url: str = None):
        payload = {"syid": syid,"tpid":tpid, "title": title, "year": year,"marks":marks, "file_url": file_url}
        resp = sb.table("pastpapers4").insert(payload).execute()
        return resp.data

    def get_papers_by_syllabus(self, syid: int):
        resp = sb.table("pastpapers4").select("*").eq("syid", syid).execute()
        return resp.data

    def delete_paper(self, paper_id: int):
        resp = sb.table("pastpapers4").delete().eq("paper_id", paper_id).execute()
        return resp.data
