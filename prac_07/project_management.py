"""
Project Management
Estimated Time: 35mins
Real Time:
"""

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""

import datetime
from project import Project


def main():
    print("Welcome to Project Manager")
    projects = load_projects(DEFAULT_FILENAME)
    for project in projects:  # testing output
        print(project)

    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        choice = input(">>>").upper()


def load_projects(filename):
    """Load projects from file"""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # remove header line
        for line in in_file:
            # file format: Name	Start Date	Priority	Cost Estimate	Completion Percentage
            parts = line.strip().split("\t")
            # print(parts[1])
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percentage = int(parts[4])
            # print(start_date)
            projects.append(Project(name, start_date, priority, cost_estimate, percentage))
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


main()
