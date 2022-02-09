import InsectClass as i

def main():

    my_insect = i.Insect(2,4)
    for value in range(10):
        my_insect.length_flight()
        print("Amount of miles the insect can fly: ", my_insect.get_flight())
main()


