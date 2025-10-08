
# class SyllabusDAO:
#     def sb(self):
#         return get_supabase()
#     def add_syllabus(self,syid:int,title:str,sid:int):
#         payload={"syid":syid,"title":title,"sid":sid}
#         resp=sb.table("syllabus").insert(payload).execute()
#         return resp
#     def add_topic(self,syid:int,title:str,status="Pending"):
#         resp=sb.table("topics").insert({'syid':syid,'title':title,'status':status}).execute()
#         return resp.data
#     def update_status(self,tid:int,status:str):
#         resp=sb.table("topics").update({'status':status}).eq("tid",tid).execute()
#         return resp.data
    
# src/dao/syllabus_dao.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in project root

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in .env file")

sb: Client = create_client(url, key)

class SyllabusDAO:
    def add_syllabus(self, syid: int, title: str, sid: int):
        payload = {"syid": syid, "title": title, "sid": sid}
        resp = sb.table("syllabus").insert(payload).execute()
        return resp.data

    def add_topic(self, syid: int, title: str, status: str = "Pending"):
        payload = {"syid": syid, "title": title, "status": status}
        resp = sb.table("topics1").insert(payload).execute()
        return resp.data

    def update_status(self, tpid: int, status: str):
        resp = sb.table("topics1").update({"status": status}).eq("tpid", tpid).execute()
        return resp.data

    def get_syllabus(self, syid: int):
        resp = sb.table("syllabus").select("*").eq("syid", syid).execute()
        return resp.data[0] if resp.data else None

    def get_topics(self, syid: int):
        resp = sb.table("topics1").select("*").eq("syid", syid).execute()
        return resp.data

    