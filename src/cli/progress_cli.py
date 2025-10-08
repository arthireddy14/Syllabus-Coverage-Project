# src/cli/progress_cli.py
from src.services.progress_service import ProgressService

class ProgressCLI:
    def __init__(self):
        self.service = ProgressService()

    def menu(self):
        while True:
            print("\n--- Progress Menu ---")
            print("1. Add/Update progress")
            print("2. View student progress")
            print("3. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                sid = int(input("Enter student id: "))
                tpid = int(input("Enter topic id: "))
                # completion_per = int(input("Enter completion % (0-100): "))
                lastupdate = input("Enter date (YYYY-MM-DD) [optional]: ") or None
                res = self.service.mark_topic_progress(sid, tpid, lastupdate)
                print("Progress updated:", res)

            elif choice == 2:
                sid = int(input("Enter student id: "))
                res = self.service.get_student_progress(sid)
                print("Progress:", res)

            elif choice == 3:
                break
            else:
                print("Invalid choice, try again.")
