class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name


def get_stock_list():
    return [
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]


def main():
    stock_list = get_stock_list()

    while True:
        print("\nStock Report")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nCompany        Symbol")
            for stock in stock_list:
                print(stock.get_company_name(), stock.get_symbol())
        elif choice == "2":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
