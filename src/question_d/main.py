import question_d #Stock Purchase History

while True:
    print("Stock Menu")
    print("1 - stock purchase history")
    print("2 - Exit")
    option = str(input("Select 1 or 2: "))
    while option not in ('1','2'):
        option = str(input("please, Select option 1 or 2: "))
    
    if option == '1':
        question_d.stock_purchase_history()

    elif option == '2':
        print("Exiting")
        break

