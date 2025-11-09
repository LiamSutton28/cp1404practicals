"""
Project Management
Estimate: 120 minutes
Actual:   TODO minutes
"""
from datetime import datetime
from operator import attrgetter

from prac_03.capitalist_conrad import out_file
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
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            print("Incomplete projects:")
            sorted_projects = sorted(projects)
            for project in sorted_projects:
                if project.is_incomplete():
                    print(f"\t{project}")
            print("Completed projects:")
            for project in sorted_projects:
                if project.is_complete():
                    print(f"\t{project}")
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
                if type(project.start_date) != str:
                    project.start_date = project.start_date.strftime("%d/%m/%Y")

        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_number = int(input("Project choice: "))
            print(projects[project_number])
            new_percentage = int(input("New Percentage: "))
            if new_percentage != "":
                projects[project_number].completion_percentage = new_percentage
            try:
                new_priority = int(input("New Priority: "))
                if new_priority != "":
                    projects[project_number].priority = new_priority
            except ValueError:
                pass

        print(MENU)
        choice = input(">>> ").upper()
    save_filename = input(f"Would you like to save to {FILENAME}")
    if save_filename != "":
        out_file = open(save_filename, "w")
    else:
        out_file = open(FILENAME, 'w')
        for project in projects:
            print(
                f"{project.name}, {project.start_date}, {project.priority}, {project.cost_estimate}, {project.completion_percentage}",
                file=out_file)
    out_file.close()
    print("Thank you for using custom-built project management software.")


def add_new_project(projects: list):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: ")[1:])
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def load_projects():
    projects = []
    with open(FILENAME, "r") as infile:
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
