from pathlib import Path

# Ask user for folder
folder_name = input("Enter a folder name: ")

# Convert to Path object
path = Path(folder_name)

# Check folder existence
if path.exists() and path.is_dir():
    count = 0
    print("\nPython files found (including subfolders):")
    
    # Recursively search .py files
    for file in path.rglob("*.py"):
        print(f" {file.relative_to(path)}")
        count += 1

    print(f"\nTotal Python files: {count}")
else:
    print("Folder not found. Please check the name and try again.")
