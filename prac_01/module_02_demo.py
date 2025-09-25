def print_grid(number_of_rows, number_of_columns):
    # version 2
    print(f"{"*" * number_of_columns}\n" * number_of_rows)

    # version 1
    # for i in range(number_of_rows):
    #     print("*" * number_of_columns)


print_grid(3, 4)
