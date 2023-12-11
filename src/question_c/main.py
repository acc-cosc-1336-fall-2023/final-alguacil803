import question_c #Stock List
question_c.stock_file("stocklist.txt")
stock_dict = question_c.get_stock_list("stocklist.txt")
while True:
    print("\tMenu")
    print("1 - stock purchase history")
    print("2 - Exit")
    option = str(input("Select 1 or 2: "))
    while option not in ('1','2'):
        option = str(input("Please, Select option 1 or 2: "))
    if option == '1':
        print("\nStock Purchase History")
        print("Stock\t      Report")
        for symbol, stocks in stock_dict.items():
            print(f"{str(stocks.get_company_name()).ljust(14)}{stocks.get_symbol()}")
        print("")
    elif option == '2':
        print("Exiting")
        break
