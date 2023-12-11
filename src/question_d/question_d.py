#write functions here, don't add input('') statements here!
class Stock():
    __symbol = None
    __company_name = None
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stockA= Stock('APPL', 'Apple Inc')
    stockB = Stock('CAT', 'Caterpillar')
    stockC = Stock('EK', 'Eastman Kodak')
    stockD = Stock('GOOG', 'Google')
    stockE = Stock('MSFT','Microsoft')

    stock_dictionary = {stockA.get_symbol():stockA.get_company_name(), 
                        stockB.get_symbol():stockB.get_company_name(), 
                        stockC.get_symbol():stockC.get_company_name(),
                        stockD.get_symbol():stockD.get_company_name(),
                        stockE.get_symbol():stockE.get_company_name()}
    
    print("\nStock purchase History")
    print("Symbol\tCompany Name")
    for symbol, company in stock_dictionary.items():
        print(symbol.ljust(7), company)
