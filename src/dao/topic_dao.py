# import os
# from supabase import create_client
# from dotenv import load_dotenv

# load_dotenv()
# url = os.getenv("SUPABASE_URL")
# key = os.getenv("SUPABASE_KEY")
# sb = create_client(url, key)
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()  # Load from .env file in project root

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or Key not found in .env file")

sb: Client = create_client(url, key)


class TopicDAO:
    def update_topic_status(self, tpid: int, new_status: str):
        """
        Update the status of a topic manually (e.g., completed or pending).
        """
        try:
            response = sb.table("topics1") \
                         .update({"status": new_status}) \
                         .eq("tpid", tpid) \
                         .execute()
            
            return response.data if response.data else []
        except Exception as e:
            print("❌ Error updating topic status:", e)
            return None