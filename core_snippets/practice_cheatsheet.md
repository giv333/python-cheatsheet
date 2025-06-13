# Beginner Python Cheatsheet by DeboX

## 📘 Dictionary Practice
```python
# Create a dictionary of students and their grades
students = {
    "Jude": 85,
    "Sarah": 80,
    "Mariam": 90,
    "Mike": 75
}

# Remove one student
students.pop("Mariam")

# Add a new student
students["John"] = 99

# Print all students and grades
print(students)
```

## 💻 Class Practice: Laptop Showcase
```python
class Laptop:
    def __init__(self, brand, RAM, price):
        self.brand = brand
        self.RAM = RAM
        self.price = price

    def introduce(self):
        print(f"Brand: {self.brand}, RAM: {self.RAM}, Price: {self.price}")

# Create laptop objects
describe1 = Laptop("Dell", "16GB", 50000)
describe2 = Laptop("HP", "8GB", 40000)

# Describe each laptop
describe1.introduce()
describe2.introduce()
```

## 📋 List Practice: To-Do App
```python
# Create list of tasks
tasks = ["Study Python", "Do laundry", "Buy food", "Call friend"]

# Remove completed task
tasks.remove("Do laundry")

# Add more tasks
tasks.append("Appointment")
tasks.append("Meeting")
tasks.append("Learning")
tasks.append("Gym")

# Print all tasks
print(f"My to-do stuffs for today is {tasks}")

