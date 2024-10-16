import json

# Task class definition
class Task:
    def _init_(self, title, description, completed=False):
        self.title = title  # Title of the task
        self.description = description  # Description of the task
        self.completed = completed  # Completion status (True or False)

    def _str_(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}: {self.description}"  # String representation of the task

# List to store all tasks
task_list = []

# Function to create a new task
def create_task(title, description):
    new_task = Task(title, description)  # Create a new task with title and description
    task_list.append(new_task)  # Add the new task to the task_list
    print(f"Added task: {title}")

# Function to display all tasks
def display_tasks():
    if not task_list:  # Check if there are no tasks
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for task in task_list:  # Loop through and print each task
        print(task)

# Function to remove a task by its title
def remove_task(title):
    global task_list
    task_list = [task for task in task_list if task.title != title]  # Remove the task with the specified title
    print(f"Task '{title}' has been removed.")

# Function to mark a task as completed by its title
def complete_task(title):
    for task in task_list:
        if task.title == title:
            task.completed = True  # Mark the task as completed
            print(f"Task '{task.title}' has been marked as completed.")
            return
    print(f"No task found with title '{title}'.")

# Function to print tasks as JSON
def print_tasks_as_json():
    print(json.dumps([task._dict_ for task in task_list], indent=4))  # Convert task_list to JSON and print it

# Function to save tasks to a JSON file
def save_to_file(filename="tasks.json"):
    with open(filename, 'w') as file:
        json.dump([task._dict_ for task in task_list], file, indent=4)  # Save tasks as JSON to a file
    print(f"Tasks saved to {filename}.")

# Function to load tasks from a JSON file
def load_from_file(filename="tasks.json"):
    global task_list
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            task_list[:] = [Task(task['title'], task['description'], task['completed']) for task in tasks_data]  # Create Task objects from JSON data
            print(f"Loaded {len(task_list)} tasks from {filename}.")
    except FileNotFoundError:
        print(f"No existing tasks found, starting fresh.")

# Main function to run the CLI interface
def run_task_manager():
    load_from_file()  # Load tasks from the file at the start

    while True:
        print("\nTask Manager CLI")
        print("1. Create a New Task")
        print("2. View All Tasks")
        print("3. Delete a Task")
        print("4. Mark Task as Complete")
        print("5. Print Tasks as JSON")
        print("6. Save and Exit")

        selection = input("Please select an option: ")

        if selection == '1':
            task_title = input("Enter task title: ")
            task_description = input("Enter task description: ")
            create_task(task_title, task_description)  # Create a new task with title and description
        elif selection == '2':
            display_tasks()  # Display all tasks
        elif selection == '3':
            task_title = input("Enter task title to delete: ")
            remove_task(task_title)  # Remove the task by title
        elif selection == '4':
            task_title = input("Enter task title to mark as complete: ")
            complete_task(task_title)  # Mark the task as complete by title
        elif selection == '5':
            print_tasks_as_json()  # Print tasks as JSON
        elif selection == '6':
            save_to_file()  # Save tasks to the file and exit
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid selection. Please try again.")

# Entry point
if __name__ == "_main_":
    run_task_manager()  # Start the task manager program