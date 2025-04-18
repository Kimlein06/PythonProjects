def organize_tasks():
    # Initialize empty lists
    checklist = []
    completed_tasks = []
    incomplete_tasks = []
    
    # Function to add tasks to the checklist
    def add_task():
        print("\n--- Add Tasks to Your Checklist ---")
        while True:
            task = input("Enter a task (or press Enter to finish adding tasks): ")
            if task == "":
                break
            checklist.append(task)
            print(f"Added: {task}")
    
    # Function to review tasks at the end of the day
    def review_tasks():
        print("\n--- Review Your Tasks ---")
        if not checklist:
            print("Your checklist is empty.")
            return
        
        print("Mark each task as completed (c) or incomplete (i):")
        for task in checklist:
            while True:
                status = input(f"Task: '{task}' - Completed or Incomplete? (c/i): ").lower()
                if status == 'c':
                    completed_tasks.append(task)
                    break
                elif status == 'i':
                    incomplete_tasks.append(task)
                    break
                else:
                    print("Please enter 'c' for completed or 'i' for incomplete.")
    
    # Function to display task summary
    def display_summary():
        print("\n====== TASK SUMMARY ======")
        print(f"Total tasks: {len(checklist)}")
        print(f"Completed tasks: {len(completed_tasks)}")
        print(f"Incomplete tasks: {len(incomplete_tasks)}")
        
        print("\n--- Completed Tasks ---")
        if completed_tasks:
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No completed tasks.")
            
        print("\n--- Incomplete Tasks ---")
        if incomplete_tasks:
            for i, task in enumerate(incomplete_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No incomplete tasks.")
    
    # Main program flow
    print("Welcome to your Daily Task Organizer!")
    add_task()
    if checklist:
        print("\nYour checklist for today:")
        for i, task in enumerate(checklist, 1):
            print(f"{i}. {task}")
        
        input("\nPress Enter when you're ready to review your tasks at the end of the day...")
        review_tasks()
        display_summary()
    else:
        print("You didn't add any tasks today.")

# Run the program
if __name__ == "__main__":
    organize_tasks()