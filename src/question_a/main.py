def create_multiplication_table():
    table = []

    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)

    return table


def display_multiplication_table(table):
    for row in table:
        for value in row:
            print(value, end=" ")
        print()


def main():
    while True:
        table = create_multiplication_table()
        display_multiplication_table(table)

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != "y":
            break


if __name__ == "__main__":
    main()
