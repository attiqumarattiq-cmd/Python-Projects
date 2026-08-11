import json
import os

# ---------------------------------------------------------
# CONSTANTS & SETUP
# ---------------------------------------------------------
DATABASE_FILE = "my_tasks.json"


# ---------------------------------------------------------
# STEP 1: PERSISTENCE FUNCTIONS (SAVING & LOADING)
# ---------------------------------------------------------

def load_tasks_from_disk():
    """Reads tasks from a JSON file on your hard drive."""
    if os.path.exists(DATABASE_FILE):
        try:
            with open(DATABASE_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []



def save_tasks_to_disk(tasks_list):
    """Saves Python list to a text file on disk permanently."""
    with open(DATABASE_FILE, "w") as file:
        json.dump(tasks_list, file, indent=4)


# ---------------------------------------------------------
# STEP 2: DATA LOGIC (ADDING & DELETING TASKS)
# ---------------------------------------------------------

def create_new_task(tasks_list, task_text):
    """Creates a task dictionary and appends it to the list."""
    new_id = len(tasks_list) + 1 
    task_dictionary = {
        "id": new_id,
        "title": task_text
    }
    tasks_list.append(task_dictionary)
    save_tasks_to_disk(tasks_list)
    return task_dictionary


def delete_task_by_index(tasks_list, display_index):
    """
    Deletes a task using its list number (1-based index).
    Re-indexes remaining items and saves the updated list.
    """
    # Convert display index (1, 2, 3...) to zero-based list index (0, 1, 2...)
    actual_index = display_index - 1
    
    # Remove item from list and store deleted item for confirmation message
    removed_task = tasks_list.pop(actual_index)
    
    # Re-index all remaining task IDs so they stay clean (1, 2, 3...)
    for index, task in enumerate(tasks_list, start=1):
        task["id"] = index
        
    # Save modified list back to disk storage
    save_tasks_to_disk(tasks_list)
    
    return removed_task


# ---------------------------------------------------------
# STEP 3: USER INTERFACE (DISPLAYING DATA)
# ---------------------------------------------------------

def display_all_tasks(tasks_list):
    """Prints all saved tasks neatly to the terminal."""
    if len(tasks_list) == 0:
        print("\n----------------------------------")
        print("Your task list is currently empty!")
        print("----------------------------------")
        return False

    print("\n==================================")
    print("         YOUR TO-DO LIST          ")
    print("==================================")
    
    
    for display_number, task in enumerate(tasks_list, start=1):
        task_id = task["id"]
        task_title = task["title"]
        print(f"{display_number}. [DB-ID: {task_id}] {task_title}")
        
    print("==================================")
    return True


# ---------------------------------------------------------
# STEP 4: MAIN CONTROL LOOP
# ---------------------------------------------------------

def main():
    """Main engine loop running the menu system."""
    tasks_database = load_tasks_from_disk()

    while True:
        print("\n=== DECODELABS TASK ENGINE ===")
        print("1. View All Tasks")
        print("2. Add a New Task")
        print("3. Delete a Task")
        print("4. Exit Program")
        
        user_choice = input("\nEnter choice (1-4): ").strip()

        if user_choice == "1":
            display_all_tasks(tasks_database)
            
            
        elif user_choice == "2":
            new_title = input("\nEnter task description: ").strip()
            if new_title != "":
                added_item = create_new_task(tasks_database, new_title)
                print(f"✓ Success: '{added_item['title']}' saved to database!")
            else:
                print("⚠ Warning: Task description cannot be left blank.")

        elif user_choice == "3":
            # Display current list first so user knows which number to select
            has_items = display_all_tasks(tasks_database)
            if has_items:
                user_input = input("\nEnter the Task Number to delete: ").strip()
                
                # Check if input is a valid number
                if user_input.isdigit():
                    task_num = int(user_input)
                    
                    # Validate if task number exists inside list range
                    if 1 <= task_num <= len(tasks_database):
                        deleted_item = delete_task_by_index(tasks_database, task_num)
                        print(f"✓ Task '{deleted_item['title']}' deleted successfully!")
                    else:
                        print("⚠ Error: Task number out of range.")
                else:
                    print("⚠ Error: Please enter a valid number.")

        elif user_choice == "4":
            print("\nShutting down engine... All data safely saved!")
            break

        else:
            print("⚠ Invalid input! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()