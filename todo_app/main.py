# main.py

from todo_operations import add_todo, view_todos, delete_todo
from utils import clear_screen, get_user_input

def display_menu():
    """Displays the main menu."""
    print("\nTo-Do List Application")
    print("1. Add a new to-do item")
    print("2. View all to-do items")
    print("3. Delete a to-do item")
    print("4. Exit")

def main():
    while True:
        clear_screen()
        display_menu()
        choice = get_user_input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Add a new to-do item
            item = get_user_input("Enter the new to-do item: ")
            add_todo(item)

        elif choice == '2':
            # View all to-do items
            view_todos()
            get_user_input("Press Enter to return to the menu.")

        elif choice == '3':
            # Delete a to-do item
            view_todos()
            try:
                index = int(get_user_input("Enter the index of the item to delete: "))
                delete_todo(index)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
