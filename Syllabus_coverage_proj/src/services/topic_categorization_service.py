# src/services/topic_categorization_service.py
from src.dao.topic_categorization_dao import TopicCategorizationDAO

from src.dao.topic_categorization_dao import TopicCategorizationDAO
# import requests
# import re

class TopicCategorizationService:
    def __init__(self):
        self.dao = TopicCategorizationDAO()

    def extract_topics_from_text(self, text, topics):
        """Simple keyword matching to find which topics appear in text."""
        found = {}
        for topic in topics:
            name = topic["tname"].lower()
            if re.search(rf"\b{name}\b", text.lower()):
                tpid = topic["tpid"]
                found[tpid] = found.get(tpid, 0) + 1
        return found

    def categorize_topics_based_on_past_papers(self, syllabus_id):
        topics = self.dao.get_topics_by_syllabus(syllabus_id)
        past_counts = self.dao.get_past_paper_counts(syllabus_id)  # Table-only counts

        categorized = []
        for topic in topics:
            tpid = topic["tpid"]
            count = past_counts.get(tpid, 0)
            if count >= 4:
                cname = "Easy"
            elif count >= 2:
                cname = "Medium"
            else:
                cname = "Difficult"
            expected = count >= 2
            cid = self.dao.get_category_id(cname)
            self.dao.upsert_topic_category(tpid, cid, count, expected)
            categorized.append({
                "tpid": tpid,
                "difficulty": cname,
                "count": count,
                "expected": expected
            })
        return categorized


    def view_categorized_topics(self):
        return self.dao.view_categorized_topics()
