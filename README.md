#  Beginner Python Cheatsheet by DeboX

Welcome to my beginner Python cheatsheet! This is a personal project created to practice and showcase the foundational building blocks of Python programming. The code examples inside are clean, beginner-friendly, and reflect my journey from zero to Python pro. 🚀

---

  Dictionary Practice


students = {
    "Jude": 85,
    "Sarah": 80,
    "Mariam": 90,
    "Mike": 75
}

students.pop("Mariam")
students["John"] = 99

print(students)




 Class Practice: Laptop Showcase

class Laptop:
    def __init__(self, brand, RAM, price):
        self.brand = brand
        self.RAM = RAM
        self.price = price

    def introduce(self):
        print(f"Brand: {self.brand}, RAM: {self.RAM}, Price: {self.price}")

describe1 = Laptop("Dell", "16GB", 50000)
describe2 = Laptop("HP", "8GB", 40000)

describe1.introduce()
describe2.introduce()



   List Practice: To-Do App

tasks = ["Study Python", "Do laundry", "Buy food", "Call friend"]

tasks.remove("Do laundry")
tasks.append("Appointment")
tasks.append("Meeting")
tasks.append("Learning")
tasks.append("Gym")

print(f"My to-do stuffs for today is {tasks}")



     What I'm Practicing
How to use dict for storing and updating info

Creating classes and working with objects in Python

Managing tasks and data using lists

Writing and organizing code cleanly for future reuse

Using Git and GitHub like a real developer

     About This Repository
This repository is a record of my hands-on journey into Python. It's made to:

Document what I’m learning

Help others just starting out

Track my growth from beginner to expert

Build confidence and momentum one project at a time

Feel free to clone, fork, or suggest improvements!
