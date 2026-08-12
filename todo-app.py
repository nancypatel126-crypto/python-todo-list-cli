"""
====================================================
   SIMPLE TO-DO LIST CLI APPLICATION (Beginner Friendly)
====================================================
This program lets you:
  1. Add a new task
  2. View all tasks
  3. Remove a task
  4. Exit (and save your tasks to a file)

Tasks are stored in a Python list while the program runs,
and saved to/loaded from "tasks.txt" so you don't lose them
when you close the program.
"""

import os

# Name of the file where tasks will be saved
FILE_NAME = "tasks.txt"


# ---------------------------------------------------
# FUNCTION: load_tasks
# Reads tasks from the .txt file (if it exists) and
# returns them as a list. This runs once at startup.
# ---------------------------------------------------
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()  # remove newline/whitespace
                if task:  # ignore empty lines
                    tasks.append(task)
    return tasks


# ---------------------------------------------------
# FUNCTION: save_tasks
# Writes the current list of tasks to the .txt file.
# Called every time the list changes, and on exit.
# ---------------------------------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


# ---------------------------------------------------
# FUNCTION: add_task
# Asks the user for a task description and adds it
# to the tasks list.
# ---------------------------------------------------
def add_task(tasks):
    task = input("Enter the new task: ").strip()

    if task == "":
        print("⚠️  Task cannot be empty. Please try again.\n")
        return

    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: \"{task}\"\n")


# ---------------------------------------------------
# FUNCTION: view_tasks
# Displays all current tasks as a numbered list.
# ---------------------------------------------------
def view_tasks(tasks):
    print("\n----------- YOUR TO-DO LIST -----------")
    if not tasks:  # empty list check
        print("  (No tasks yet. Add one!)")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"  {index}. {task}")
    print("----------------------------------------\n")


# ---------------------------------------------------
# FUNCTION: remove_task
# Asks the user which task number to remove, then
# deletes it from the list (with input validation).
# ---------------------------------------------------
def remove_task(tasks):
    if not tasks:
        print("⚠️  There are no tasks to remove.\n")
        return

    view_tasks(tasks)
    choice = input("Enter the task number to remove: ").strip()

    # Make sure the input is a valid number
    if not choice.isdigit():
        print("⚠️  Please enter a valid number.\n")
        return

    task_number = int(choice)

    # Make sure the number is within range of the list
    if task_number < 1 or task_number > len(tasks):
        print("⚠️  That task number doesn't exist.\n")
        return

    removed = tasks.pop(task_number - 1)  # -1 because list index starts at 0
    save_tasks(tasks)
    print(f"🗑️  Removed task: \"{removed}\"\n")


# ---------------------------------------------------
# FUNCTION: show_menu
# Displays the main menu options to the user.
# ---------------------------------------------------
def show_menu():
    print("========== TO-DO LIST MENU ==========")
    print("  1. Add a task")
    print("  2. View all tasks")
    print("  3. Remove a task")
    print("  4. Exit")
    print("======================================")


# ---------------------------------------------------
# FUNCTION: main
# Runs the main program loop: shows the menu, gets
# the user's choice, and calls the right function.
# ---------------------------------------------------
def main():
    tasks = load_tasks()  # load saved tasks when program starts

    print("\nWelcome to your Python To-Do List! 📝\n")

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)  # save one last time before closing
            print("\n👋 Goodbye! Your tasks have been saved to tasks.txt")
            break  # exits the while loop, ending the program
        else:
            print("⚠️  Invalid choice. Please enter a number from 1 to 4.\n")


# ---------------------------------------------------
# This makes sure main() only runs when this file is
# executed directly (not when imported elsewhere).
# ---------------------------------------------------
if __name__ == "__main__":
    main()