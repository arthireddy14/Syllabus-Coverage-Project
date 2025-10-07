# src/cli/syllabus_cli.py
from src.services.syllabus_service import SyllabusService

class SyllabusCLI:
    def __init__(self):
        self.service = SyllabusService()

    def menu(self):
        while True:
            print("\n--- Syllabus Menu ---")
            print("1. Add syllabus")
            print("2. View syllabus by id")
            print("3. Add topic to syllabus")
            print("4. View topics of a syllabus")
            print("5. Update topic status")
            print("6. Exit")

            ch = int(input("Enter choice: "))

            if ch == 1:
                syid = int(input("Enter syllabus id: "))
                title = input("Enter syllabus title: ")
                sid = int(input("Enter student id: "))
                res = self.service.create_syllabus(syid, title, sid)
                print("Syllabus added:", res)

            elif ch == 2:
                syid = int(input("Enter syllabus id: "))
                res = self.service.fetch_syllabus(syid)
                print("Syllabus details:", res)

            elif ch == 3:
                syid = int(input("Enter syllabus id: "))
                title = input("Enter topic title: ")
                res = self.service.add_topic_to_syllabus(syid, title)
                print("Topic added:", res)

            elif ch == 4:
                syid = int(input("Enter syllabus id: "))
                res = self.service.fetch_topics(syid)
                print("Topics:", res)

            elif ch == 5:
                tpid = int(input("Enter topic id(tpid): "))
                status = input("Enter new status (Pending/Completed): ")
                res = self.service.change_topic_status(tpid, status)
                print("Topic updated:", res)

            elif ch == 6:
                print("Exiting syllabus CLI...")
                break

            else:
                print("Invalid choice, try again")
