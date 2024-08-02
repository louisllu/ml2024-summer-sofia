from module5_oop import Data

def data_processing():
    data = Data()
    n = input("Please enter a positive integer N:")
    data.initialize(n)

    for _ in range(data.length):
        x = input("Please enter a number you would like to input:")
        data.insert(x)

    target = input("Please enter the number you would like to search:")
    return data.search(target)



