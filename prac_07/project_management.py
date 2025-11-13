"""
Project Management
Estimate: 120 minutes
Actual:   200 minutes
"""
from datetime import datetime
from operator import attrgetter

from prac_07.project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
FILENAME = "projects.txt"


def main():
    """Run project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects.append(load_projects(input("Filename: ")))
        elif choice == "S":
            new_file = input("Filename to save to: ")
            out_file = open(new_file, "w")
            save_files(out_file, projects)
        elif choice == "D":
            print("Incomplete projects:")
            sorted_projects = sorted(projects)
            display_projects(sorted_projects, True)
            print("Completed projects:")
            display_projects(sorted_projects, False)
        elif choice == "F":
            given_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            given_date = datetime.strptime(given_date_string, "%d/%m/%Y").date()
            after_date_projects = []
            for project in projects:
                project.start_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
                if project.start_date >= given_date:
                    after_date_projects.append(project)
            after_date_projects.sort(key=attrgetter("start_date"))
            for project in after_date_projects:
                project.start_date = project.start_date.strftime("%d/%m/%Y")
                print(project)
            for project in projects:
                if project.start_date is str:
                    project.start_date = project.start_date.strftime("%d/%m/%Y")
        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            list_projects(projects)
            project_number = get_valid_project_number(projects)
            print(projects[project_number])
            new_percentage = get_valid_percentage_number()
            projects[project_number].completion_percentage = new_percentage
            get_new_priority(project_number, projects)

        print(MENU)
        choice = input(">>> ").upper()
    save_filename = input(f"Would you like to save to {FILENAME}").title()
    if save_filename == "" or save_filename == "Yes":
        out_file = open(FILENAME, 'w')
    else:
        out_file = open(save_filename, "w")
    save_files(out_file, projects)
    print("Thank you for using custom-built project management software.")


def save_files(out_file, projects: list):
    """Save the files to the outfile in a tab delimited format."""
    for project in projects:
        print(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
            file=out_file)
    out_file.close()


def get_new_priority(project_number: int, projects: list):
    """Get a new priority integer from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            new_priority = int(input("New Priority: "))
            if new_priority != "":
                projects[project_number].priority = new_priority
            is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")


def list_projects(projects: list):
    """List projects with a number next to them."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")


def get_valid_project_number(projects: list) -> int:
    """Get a valid project number from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            project_number = int(input("Project choice: "))
            if project_number < 0:
                print("Number must be >= 0")
            elif project_number > len(projects):
                print("Invalid project number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return project_number


def get_valid_percentage_number() -> int:
    """Get a valid percentage from the user."""
    is_valid_input = False
    while not is_valid_input:
        try:
            percentage_number = int(input("New Percentage: "))
            if percentage_number < 0:
                print("Number must be >= 0")
            elif percentage_number > 100:
                print("Invalid percentage")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")
    return percentage_number


def display_projects(sorted_projects: list, incomplete):
    """Display the projects."""
    for project in sorted_projects:
        if project.is_incomplete() and incomplete:
            print(f"\t{project}")
        elif not project.is_incomplete() and not incomplete:
            print(f"\t{project}")


def add_new_project(projects: list):
    """Get a new project from the user."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: ")[1:])
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def load_projects(filename):
    """Load the projects into a list of Project objects."""
    projects = []
    with open(filename, "r") as infile:
        infile.readline()  # skip file header
        for line in infile:
            parts = line.strip().split("\t")
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


main()
