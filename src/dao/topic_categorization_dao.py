# src/dao/topic_categorization_dao.py
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in project root

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in .env file")

sb: Client = create_client(url, key)


class TopicCategorizationDAO:

    def get_topics_by_syllabus(self, syllabus_id):
        res = sb.table("topics1").select("*").eq("syid", syllabus_id).execute()
        return res.data if res.data else []

    def get_past_paper_counts(self, syllabus_id):
        res = sb.table("pastpapers4").select("tpid").eq("syid", syllabus_id).execute()
        counts = {}
        for row in res.data:
            tpid = row["tpid"]
            counts[tpid] = counts.get(tpid, 0) + 1
        return counts

    def get_past_papers_with_files(self, syllabus_id):
        """Get past papers that have uploaded file URLs."""
        res = sb.table("pastpapers4").select("paper_id, file_url").eq("syid", syllabus_id).execute()
        return [r for r in res.data if r.get("file_url")] if res.data else []

    def get_category_id(self, cname):
        res = sb.table("category2").select("cid").eq("cname", cname).execute()
        if res.data:
            return res.data[0]["cid"]
        else:
            return None

    def upsert_topic_category(self, tpid, cid, count, expected):
        payload = {
            "tpid": tpid,
            "cid": cid,
            "appear_count": count,
            "expected_in_next": expected
        }
        sb.table("topic_categorization2").upsert(payload, on_conflict="tpid").execute()

    def view_categorized_topics(self):
        res = sb.table("topic_categorization2").select("tpid, appear_count, expected_in_next, category2!inner(cname)").execute()
        return res.data if res.data else []
