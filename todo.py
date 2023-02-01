import db_helper


def main():
    r = 1
    db_helper.create_table()
    while (r):
        print("1. Insert New Task")
        print("2. View a Task")
        print("3. Delete a Task")
        print("4. Exit")
        x = input("Choose any option: ")
        print()

        if x == "1":
            task = str(input("Enter the Task: "))
            db_helper.data_entry(task)
        elif x == "2":
            db_helper.printData()
        elif x == "3":
            index = int(input("Enter the task index: "))
            db_helper.deleteTask(index)
        elif x == "4":
            r = 0
        else:
            print("Enter values between 1 to 4 ")

    db_helper.closeCursor()


if __name__ == "__main__":
    main()
