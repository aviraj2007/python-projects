import streamlit as st
import csv

# Define the path to the CSV file
CSV_FILE = "tasks.csv"

# Define the main function
def main():
    # Set the title of the web app
    st.title("To-Do List")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?cs=srgb&dl=pexels-adrien-olichon-2387793.jpg&fm=jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    # Load the tasks from the CSV file
    task_list = load_tasks()

    # Add a form to input new tasks
    task_input = st.text_input("Add a new task:")
    if st.button("Add"):
        if task_input != "":
            # Add the new task to the list and save it to the CSV file
            task_list.append(task_input)
            save_tasks(task_list)
            task_input = ""
            display(task_list)

    

    # Add a button to clear the task list
    if st.button("Clear all tasks"):
        # Clear the task list and save the changes to the CSV file
        task_list.clear()
        save_tasks(task_list)
        display(task_list)        

def load_tasks():
    """
    Load the tasks from the CSV file.
    """
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            task_list = [row[0] for row in reader]
    except FileNotFoundError:
        task_list = []
    return task_list
def display(task_list):
    # Display the current tasks
    if len(task_list) == 0:
        st.write("No tasks added yet.")
    else:
        st.write("Current tasks:")
        for i, task in enumerate(task_list):
            st.write(f"{i+1}. {task}")
def save_tasks(task_list):
    """
    Save the tasks to the CSV file.
    """
    with open(CSV_FILE, "w", newline="") as f:
        f.truncate(0)
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

# Run the app
if __name__ == "__main__":
    main()
