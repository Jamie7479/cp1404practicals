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
- (Q)uit"""

import datetime
from project import Project


def main():
    """Manage and display projects"""
    print("Welcome to Project Manager")
    projects = load_projects(DEFAULT_FILENAME)
    # for project in projects:  # testing output
    #     print(project)

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            projects.extend(load_projects(filename))
        elif choice == "S":
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            date = get_valid_date("Show projects that start after date (d/m/yyyy): ")
            # print(date)
            display_projects_on_or_after_date(projects, date)
        elif choice == "A":
            projects.append(get_new_project())
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    if input(f"Would you like to save to {DEFAULT_FILENAME}? (y/n) ").upper() == "Y":
        save_projects(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


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
    """Save projects to file"""
    with open(filename, "w") as out_file:
        for project in projects:
            # print(project)
            start_date_string = project.start_date.strftime('%d/%m/%Y')
            print(f"{project.name}\t{start_date_string}\t{project.priority}"
                  f"\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects"""
    incomplete_projects = [project for project in sorted(projects) if not project.is_complete()]
    print("Incomplete projects:")
    completed_projects = [project for project in sorted(projects) if project.is_complete()]
    for project in incomplete_projects:
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(f"\t{project}")

    print("Completed projects:")
    for project in completed_projects:
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(f"\t{project}")


def get_valid_date(prompt):
    """Get valid date"""
    while True:
        try:
            date_string = input(prompt)
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return date
        except ValueError:
            print("Invalid date format")


def display_projects_on_or_after_date(projects, date):
    """Display all projects on or after date"""
    for project in [project for project in sorted(projects) if project.is_on_or_after(date)]:
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(f"\t{project}")


def get_valid_number(prompt):
    """Get valid date"""
    while True:
        try:
            number = int(input(prompt))
            if number >= 0:
                return number
        except ValueError:
            print("Invalid number")


def get_new_project():
    """Get new project object"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yyyy): ")
    priority = get_valid_number("Priority: ")
    cost_estimate = get_valid_number("Cost estimate: $")
    completion_percentage = get_valid_number("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion_percentage)


def update_project(projects):
    """Choose object and update completion and priority"""
    for i, project in enumerate(projects):
        start_date_string = project.start_date.strftime('%d/%m/%Y')
        print(
            f"{i} {project}%")
    choice = get_valid_number("Project choice: ")
    while choice > len(projects) - 1:
        print("Invalid choice")
        choice = get_valid_number("Project choice: ")
    project = projects[choice]
    start_date_string = project.start_date.strftime('%d/%m/%Y')
    print(project)
    project.completion_percentage = get_valid_number("New Percentage: ")
    project.priority = get_valid_number("New Priority: ")


main()
