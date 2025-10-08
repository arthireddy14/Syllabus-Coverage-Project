from src.dao.topic_dao import TopicDAO

# class TopicService:
#     def __init__(self):
#         self.dao = TopicDAO()

#     def mark_topic_status(self, tpid: int, status: str):
#         """
#         Wrapper for updating topic status.
#         """
#         result = self.dao.update_topic_status(tpid, status)
#         if result:
#             print(f"✅ Topic {tpid} marked as '{status}' successfully.")
#         else:
#             print(f"⚠️ No topic found with ID {tpid}.")
#         return result
class TopicService:
    def __init__(self):
        self.dao = TopicDAO()

    def mark_topic_status(self, tpid: int, status: str):
        """
        Wrapper for updating topic status.
        """
        result = self.dao.update_topic_status(tpid, status)
        if result:
            print(f"✅ Topic {tpid} marked as '{status}' successfully.")
        else:
            print(f"⚠️ No topic found with ID {tpid}.")
        return result
