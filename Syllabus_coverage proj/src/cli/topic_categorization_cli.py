# src/cli/topic_categorization_cli.py
from src.services.topic_categorization_service import TopicCategorizationService

class TopicCategorizationCLI:
    def __init__(self):
        self.service = TopicCategorizationService()

    # def menu(self):
    #     while True:
    #         print("\n--- Topic Categorization Menu ---")
    #         print("1. Categorize topic")
    #         print("2. View categories for a topic")
    #         print("3. Exit")

    #         choice = int(input("Enter choice: "))

    #         if choice == 1:
    #             tpid = int(input("Enter topic id: "))
    #             cid = int(input("Enter category id: "))
    #             res = self.service.categorize_topic(tpid, cid)
    #             print("Topic categorized:", res)

    #         elif choice == 2:
    #             tpid = int(input("Enter topic id: "))
    #             res = self.service.get_topic_categories(tpid)
    #             print("Categories:", res)

    #         elif choice == 3:
    #             break
    #         else:
    #             print("Invalid choice, try again.")
    def menu(self):
        print("--- Topic Categorization Menu ---")
        print("1. Auto-categorize based on past papers")
        print("2. View topic categories")
        ch = int(input("Enter choice: "))
    
        if ch == 1:
            sid = int(input("Enter syllabus id: "))
            res = self.service.categorize_topics_based_on_past_papers(sid)
            print("\n--- Categorization Completed ---")
            print(f"{'Topic ID':<10}{'Difficulty':<10}{'Count':<6}{'Expected':<8}")
            for r in res:
                print(f"{r['tpid']:<10}{r['difficulty']:<10}{r['count']:<6}{r['expected']}")


