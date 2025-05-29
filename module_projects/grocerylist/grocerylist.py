groceries = []

def add_items(item):
    groceries.append(item)
    print(f"Item added: {item}")

def remove_items(item):
    if item in groceries:
        groceries.remove(item)
        print(f"Item removed: {item}")
    else:
        print(f"Item '{item}' not found.")

def view_items():
    if groceries:
        print("Current items:")
        for i, item in enumerate(groceries, start=1):
            print(f"{i}. {item}")
    else:
        print("No item to show.")
