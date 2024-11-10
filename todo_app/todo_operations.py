# List to store to-do items
todos = []

def add_todo(item):
    """Adds a new to-do item to the list."""
    todos.append(item)
    print(f"'{item}' has been added to the to-do list.")

def view_todos():
    """Displays all to-do items."""
    if not todos:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item}")

def delete_todo(index):
    """Deletes a to-do item by its index (1-based)."""
    try:
        item = todos.pop(index - 1)
        print(f"'{item}' has been removed from the to-do list.")
    except IndexError:
        print("Invalid index. Please try again.")
