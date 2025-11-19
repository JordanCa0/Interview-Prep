import json

"""
A teacher has 30 students in a class. Each student has a list of 5 exam scores. 
Write a program to calculate and display the average score of each student.
"""

with open('students.json', 'r') as file:
    data = json.load(file)

students = data["class"]["students"]

for student in students:
    id = student["id"]
    name = student["name"]
    score = student["scores"]
    avg = sum(score) / len(score)
    print(f"Avg: {avg:.2f}")

