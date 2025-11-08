"""
Project Management
Estimate: 120 minutes
Actual:   TODO minutes
"""
from prac_07.project import Project

MENU = """
- (L)oad projects  
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
            for project in projects:
                if project.is_incomplete():
                    print(project)
            print("Completed projects:")
            for project in projects:
                if project.is_complete():
                    print(project)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_number = int(input("Project choice: "))
            print(projects[project_number])
            new_percentage = int(input("New Percentage: "))
            if new_percentage != "":
                projects[project_number].completion_percentage = new_percentage
            new_priority = int(input("New Priority: "))
            if new_priority != "":
                projects[project_number].priority = new_priority
        print(MENU)
        choice = input(">>> ").upper()


def load_projects():
    projects = []
    with open(FILENAME, "r") as infile:
        infile.readline() #skip file header
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
