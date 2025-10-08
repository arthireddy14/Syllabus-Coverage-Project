# src/cli/pastpapers_cli.py
from src.services.pastpapers_service import PastPapersService

class PastPapersCLI:
    def __init__(self):
        self.service = PastPapersService()

    def menu(self):
        while True:
            print("\n--- Past Papers Menu ---")
            print("1. Upload paper")
            print("2. View papers by syllabus")
            print("3. Delete paper")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                syid = int(input("Enter syllabus id: "))
                tpid=int(input("Enter topic id: "))
                title = input("Enter paper title: ")
                year = int(input("Enter year: "))
                marks=int(input("Enter marks: "))
                file_url = input("Enter file URL (optional): ")
                res = self.service.upload_paper(syid,tpid, title, year,marks, file_url)
                print("Paper added:", res)

            elif choice == 2:
                syid = int(input("Enter syllabus id: "))
                res = self.service.list_papers(syid)
                print("Papers:", res)

            elif choice == 3:
                pid = int(input("Enter paper id to delete: "))
                res = self.service.remove_paper(pid)
                print("Paper deleted:", res)

            elif choice == 4:
                break
            else:
                print("Invalid choice, try again.")
