import CarClass as c

def main():

    model= input("What is the model?")
    make= input("What is the make?")
    car= c.Car(model,make)

    for i in range(5):
        car.accelerate()
        print("The current speed is ", car.get_speed())

    for j in range(5):
        car.brake()
        print("The current speed is ", car.get_speed())
       
main()