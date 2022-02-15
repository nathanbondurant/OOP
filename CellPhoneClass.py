
class CellPhone:

    def __init__(self,m,mod,rp):
        self.__manufact = m
        self.__model = mod
        self.__retail_price = rp
    


    def get_manufact(self):
        return self.__manufact
    def get_model(self):
        return self.__model
    def get_retail_price(self):
        return self.__retail_price


