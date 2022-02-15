import CellPhoneClass as cp

def main():



    m = input("Who is the manufacturer?")
    mod = input("What is the model?")
    rp = input("What is the retail price?")

    phone = cp.CellPhone(m,mod,rp)


    print("The manufacturer is: ", phone.get_manufact())
    print("The model is: ", phone.get_model())
    print("The price is:", phone.get_retail_price())

main()