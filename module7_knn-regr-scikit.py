import numpy as np
from sklearn.neighbors import KNeighborsClassifier
    
class Data:
    def __init__(self) -> None:
        self.x = np.empty((0, 1), dtype=float)
        self.y = np.empty((0,), dtype=float)
        self.length: int = 0

    def set_length(self) -> int:
        message = "Please enter how many points you would like to input: "
        self.length = self._get_positive_interger(message)
        return self.length
    
    def insert_data(self) -> None:
        self.x = np.empty((self.length, 1), dtype=float)
        self.y = np.empty((self.length, ), dtype=float)

        for i in range(self.length):
            self.x[i] = self._get_float(f"Please enter the x of point #{i + 1}: ")
            self.y[i] = self._get_float(f"Please enter the y of point #{i + 1}: ")
    
    def get_length(self) -> int:
        return self.length
    
    @staticmethod
    def _get_positive_interger(message: str) -> int:
        while True:
            try:
                value = int(input(message))
                if value > 0:
                    return value
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a valid integer.")

    @staticmethod    
    def _get_float(message: str) -> float:
        while True:
            try:
                value = float(input(message))
                return value
            except ValueError:
                print("Please enter a valid number")

def main():

    # enter n
    train_set = Data()
    length = train_set.set_length()

    # enter data points
    train_set.insert_data()

    # enter k
    while True:
        k = Data._get_positive_interger("Please enter K: ")
        if k > length:
            print(f"K must be smaller or equal to {length}")
        else:
            break
        
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(train_set.x, train_set.y)

    # predict y
    x = Data._get_float("Please enter x for prediction:")
    pred_y = knn.predict(np.array([[x]]))
    print(f"predicted y: {pred_y}" )

    # return var
    var = np.var(train_set.y)
    print(f"The variance of labels in the training dataset is {var}")

if __name__ == "__main__":
    main()

