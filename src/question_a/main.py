import question_a #Multiplication

while True:
    print("\tMenu")
    print("1 - Multiplication Table")
    print("2 - Exit")
    option = str(input("Select 1 or 2: "))
    while option not in ('1','2'):
        option = input("Please, Select 1 or 2: ")
    if option == '1':
        while True:
            row = int(input("number of rows: "))
            column = int(input("number of columns: "))
            table = question_a.create_multiplication(row, column)
            question_a.display_table(table)
            exit_option = str(input("\nPress Y to continue: ")).lower()
            print("")
            if exit_option not in ('y','yes'):
                print("Exiting")
                break
        break
    if option == '2':
        print("Exiting")
        break