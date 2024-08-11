import numpy as np

class KNN:
    def __init__(self, length):
        self.points = None
        self.data_length = length
        self.k = 1

    def initialize(self, input):
        self.points = np.array(input)
    
    def insert(self, input):
        if self.points is None:
            self.initialize(input)
        else:
            self.points = np.vstack((self.points, input))
        
    def input_k(self, k):
        self.k = int(k)

    def predict(self, x):
        distances = np.abs(self.points[:, 0] - x)
        indices = np.argsort(distances)
        y_pred = np.mean(self.points[indices, 1][:self.k])
        return y_pred

        
def main():

    # enter n
    try:
        n = int(input("Please enter how many points you would like to input: "))
        assert n > 0, "n must larger than 0."
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    except ValueError as e:
        print("n must be a positive interger")

    # enter data points
    knn = KNN(length=n)
    try:
        for i in range(knn.data_length):
            x = float(input(f"Please enter the x of point #{i + 1}: "))
            y = float(input(f"Please enter the y of point #{i + 1}: "))
            knn.insert([x, y])
    except ValueError as e:
        print("x must be a number")

    # enter k
    try:
        k = float(input("Please enter K: "))
        assert k > 0, "K should be larger than 0."
        assert k.is_integer(), "K should be an integer."
        assert k <= knn.data_length, "K must be smaller or equal than n (the number of input points)."
        assert k is not None, "K should not be empty"
        knn.input_k(k)
    except AssertionError as e:
        print(f"Assertion Error: {e}")
    
    # predict y
    try:
        x = float(input("Please enter x for prediction:"))
        pred_y = knn.predict(x)
        print(f"predicted y: {pred_y}" )
    except ValueError as e:
        print("x must be a number")


if __name__ == "__main__":
    print("execute")
    main()

