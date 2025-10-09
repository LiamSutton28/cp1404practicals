"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    records = load_data(FILENAME)
    print_subject_details(records)


def print_subject_details(records: list):
    for record in records:
        print(f"{record[0]} is taught by {record[1]} and has {record[2]} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    records = []
    for line in input_file:
        parts = line.strip().split(',')  # Remove the \n
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        records.append(parts)
    input_file.close()
    return records


main()
