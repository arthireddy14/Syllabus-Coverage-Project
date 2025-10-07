import os
from supabase import create_client
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)
class StudentDAO:
    def add_student(self,sid:int,sname:str,course:Optional[str]):
        payload={"sid":sid,"sname":sname,"course":course}
        resp=sb.table("students").insert(payload).execute()
        return resp.data
    def search_student(self,sid:int):
        resp=sb.table("students").select("*").eq("sid",sid).execute()
        return resp.data[0] if resp.data else None
    def update_details(self,sid:int,details:dict):
        resp=sb.table("students").update(details).eq("sid",sid).execute()
        return resp.data
        