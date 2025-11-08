"""
Project Management
Estimated Time: 35mins
Real Time:
"""
from yt_dlp.utils import process_communicate_or_kill

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

    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects.extend(load_projects(filename))
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(sorted(projects))
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid input")
        print(MENU)
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


def save_projects(projects, filename):
    with open(filename, "w") as out_file:
        for project in projects:
            # print(project)
            start_date_string = project.start_date.strftime('%d/%m/%Y')
            print(f"{project.name}\t{start_date_string}\t{project.priority}"
                  f"\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    print("Incomplete projects:")
    for project in incomplete_projects:
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(f"\t{project.name}, start: {start_date_string}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    print("Completed projects:")
    for project in completed_projects:
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(f"\t{project.name}, start: {start_date_string}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

main()
