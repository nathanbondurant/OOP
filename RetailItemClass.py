class RetailItem:
    def __init__(self, item, inv, price):
        self.__itemdesc= item
        self.__inv= inv
        self.__price = price
    def get_item(self):
        return self.__itemdesc
    def get_inv(self):
        return self.__inv
    def get_price(self):
        return self.__price

