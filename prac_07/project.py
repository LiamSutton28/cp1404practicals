"""Project Class module"""


class Project:
    """Project class"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create a Project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def is_incomplete(self):
        return self.completion_percentage != 100

    def is_complete(self):
        return self.completion_percentage == 100


def run_tests():
    print("here")
    p1 = Project("Build Car Park", "12/09/2021", 2, 600000.0, 95)
    print(p1)
    print(p1.is_complete())

if __name__ == "__main__":
    run_tests()
