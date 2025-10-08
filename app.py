import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


# # Import CLI classes (which internally call service methods)
# from cli.student_cli import StudentCLI
# from cli.syllabus_cli import SyllabusCLI
# from cli.pastpapers_cli import PastPapersCLI
# from cli.topic_categorization_cli import TopicCategorizationCLI
# from cli.progress_cli import ProgressCLI

# # Initialize CLI instances
# student_cli = StudentCLI()
# syllabus_cli = SyllabusCLI()
# pastpapers_cli = PastPapersCLI()
# topic_cat_cli = TopicCategorizationCLI()
# progress_cli = ProgressCLI()
from services.student_service import StudentService

from services.student_service import StudentService
from services.syllabus_service import SyllabusService
from services.pastpapers_service import PastPapersService
from services.progress_service import ProgressService
from services.topic_categorization_service import TopicCategorizationService
from src.services.topic_service import TopicService



# Initialize service classes directly
student_service = StudentService()
syllabus_service = SyllabusService()
pastpapers_service = PastPapersService()
progress_service = ProgressService()
topic_cat_service = TopicCategorizationService()
topic_service = TopicService()
# ------------------ Topic Module ------------------
def topic_menu():
    while True:
        print("\n--- Topic Operations ---")
        print("1. Update Topic Status")
        print("2. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                tpid = int(input("Enter Topic ID (tpid): "))
                new_status = input("Enter new status (completed/pending): ").strip().lower()

                if new_status not in ["completed", "pending"]:
                    print("❌ Invalid status. Must be 'completed' or 'pending'.")
                else:
                    topic_service.mark_topic_status(tpid, new_status)

            except ValueError:
                print("❌ Please enter a valid numeric topic ID.")

        elif choice == "2":
            break  # back to main menu

        else:
            print("❌ Invalid choice. Please try again.")

# ---------------- Streamlit App -----------------
st.title("📚 Syllabus Coverage Planner")

menu = [
    "Student Management",
    "Syllabus Management",
    "Past Papers Management",
    "Topic Categorization",
    "Progress Tracking",
    # "Topic operations"
]

choice = st.sidebar.selectbox("Select Module", menu)

# ---------------- Student Management -----------------
if choice == "Student Management":
    st.header("Student Management")
    action = st.radio("Action", ["Register Student", "View Student", "Update Student"])
    
    if action == "Register Student":
        sid = st.number_input("Student ID", step=1)
        name = st.text_input("Name")
        course = st.text_input("Course")
        if st.button("Register Student"):
            student_service.register_stu(sid, name, course)
            st.success("Student registered successfully!")
    
    elif action == "View Student":
        sid = st.number_input("Student ID to view", step=1)
        if st.button("View"):
            student = student_service.get_student(sid)
            st.write(student)
    
    elif action == "Update Student":
        sid = st.number_input("Student ID to update", step=1)
        field = st.text_input("Field to update (name/course)")
        value = st.text_input("New value")
        if st.button("Update"):
            student_service.update_sdetails(sid, {field: value})
            st.success("Student updated successfully!")

# ---------------- Syllabus Management -----------------
elif choice == "Syllabus Management":
    st.header("Syllabus Management")
    action = st.radio("Action", ["Create Syllabus", "Add Topic", "View Syllabus", "View Topics"])
    
    if action == "Create Syllabus":
        syid = st.number_input("Syllabus ID", step=1)
        title = st.text_input("Syllabus Title")
        sid = st.number_input("Student ID", step=1)
        if st.button("Create Syllabus"):
            syllabus_service.create_syllabus(syid, title, sid)
            st.success("Syllabus created successfully!")
    
    elif action == "Add Topic":
        syid = st.number_input("Syllabus ID", step=1)
        title = st.text_input("Topic Title")
        if st.button("Add Topic"):
            syllabus_service.add_topic_to_syllabus(syid, title)
            st.success("Topic added successfully!")
    
    elif action == "View Syllabus":
        syid = st.number_input("Syllabus ID", step=1)
        if st.button("View Syllabus"):
            syllabus = syllabus_service.fetch_syllabus(syid)
            st.write(syllabus)
    
    elif action == "View Topics":
        syid = st.number_input("Syllabus ID", step=1)
        if st.button("View Topics"):
            topics = syllabus_service.fetch_topics(syid)
            st.write(topics)

# ---------------- Past Papers Management -----------------
elif choice == "Past Papers Management":
    st.header("Past Papers Management")
    action = st.radio("Action", ["Upload Paper", "List Papers", "Remove Paper"])
    
    if action == "Upload Paper":
        syid = st.number_input("Syllabus ID", step=1)
        tpid = st.number_input("Topic ID", step=1)
        title = st.text_input("Topic Title")
        year = st.number_input("Year", step=1)
        marks = st.number_input("Marks", step=1)
        file_url = st.text_input("File URL (optional)")
        if st.button("Upload Paper"):
            pastpapers_service.upload_paper(syid, tpid, title, year, marks, file_url)
            st.success("Paper uploaded successfully!")
    
    elif action == "List Papers":
        syid = st.number_input("Syllabus ID", step=1)
        if st.button("List Papers"):
            papers = pastpapers_service.list_papers(syid)
            st.write(papers)
    
    elif action == "Remove Paper":
        pid = st.number_input("Paper ID", step=1)
        if st.button("Remove Paper"):
            pastpapers_service.remove_paper(pid)
            st.success("Paper removed successfully!")

# ---------------- Topic Categorization -----------------
elif choice == "Topic Categorization":
    st.header("Topic Categorization")
    action = st.radio("Action", ["Auto-Categorize", "View Categorized Topics"])
    
    if action == "Auto-Categorize":
        syid = st.number_input("Syllabus ID", step=1)
        if st.button("Categorize"):
            result = topic_cat_service.categorize_topics_based_on_past_papers(syid)
            st.success("Topics categorized!")
            st.write(result)
    
    elif action == "View Categorized Topics":
        if st.button("View"):
            categories = topic_cat_service.view_categorized_topics()
            st.write(categories)

# ---------------- Progress Tracking -----------------
elif choice == "Progress Tracking":
    st.header("Progress Tracking")
    action = st.radio("Action", ["Mark Progress", "View Progress"])
    
    if action == "Mark Progress":
        sid = st.number_input("Student ID", step=1)
        tpid = st.number_input("Topic ID", step=1)
        # completion = st.slider("Completion %", 0, 100)
        lastupdate = st.date_input("Last Update")
        if st.button("Update Progress"):
            progress_service.mark_topic_progress(sid, tpid, str(lastupdate))
            st.success("Progress updated successfully!")
    
    elif action == "View Progress":
        sid = st.number_input("Student ID", step=1)
        if st.button("View Progress"):
            progress = progress_service.get_student_progress(sid)
            st.write(progress)
# elif choice == "Topic operations":
#             topic_menu()
            
