# from src.cli.student_cli import StudentCLI
# if __name__=="__main__":
#     scli=StudentCLI()
#     scli.menu()
    
# src/cli/main.py
from src.cli.student_cli import StudentCLI
from src.cli.syllabus_cli import SyllabusCLI
from src.cli.pastpapers_cli import PastPapersCLI
from src.cli.topic_categorization_cli import TopicCategorizationCLI
from src.cli.progress_cli import ProgressCLI

class MainCLI:
    def __init__(self):
        self.student_cli = StudentCLI()
        self.syllabus_cli = SyllabusCLI()
        self.pastpapers_cli = PastPapersCLI()
        self.topic_cat_cli = TopicCategorizationCLI()
        self.progress_cli = ProgressCLI()

    def menu(self):
        while True:
            print("\n==== Main Menu ====")
            print("1. Student Management")
            print("2. Syllabus Management")
            print("3. Past Papers Management")
            print("4. Topic Categorization")
            print("5. Progress Tracking")
            print("6. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.student_cli.menu()
            elif choice == 2:
                self.syllabus_cli.menu()
            elif choice == 3:
                self.pastpapers_cli.menu()
            elif choice == 4:
                self.topic_cat_cli.menu()
            elif choice == 5:
                self.progress_cli.menu()
            elif choice == 6:
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    app = MainCLI()
    app.menu()
