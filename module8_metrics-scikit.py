import numpy as np
from sklearn.metrics import recall_score, precision_score
print("Execute data")
print("Execute data")
class Data:
    def __init__(self) -> None:
        self._x = np.empty((0, 1), dtype=float)
        self._y = np.empty((0,), dtype=float)
        self._length: int = 0

    def set_length(self) -> int:
        message = "Please enter how many points you would like to input: "
        self._length = self._get_positive_interger(message)
        return self._length
    
    def insert_data(self) -> None:
        self._x = np.empty((self._length, 1), dtype=float)
        self._y = np.empty((self._length, ), dtype=float)

        for i in range(self._length):
            self._x[i] = self._get_float(f"Please enter the x of point #{i + 1}: ")
            self._y[i] = self._get_float(f"Please enter the y of point #{i + 1}: ")
    
    def get_length(self) -> int:
        return self._length

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

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
    dataset = Data()
    dataset.set_length()

    # enter data points
    dataset.insert_data()

    recall = recall_score(dataset.get_x(), dataset.get_y())
    print(f"Recall: {recall}")

    precision = precision_score(dataset.get_x(), dataset.get_y())
    print(f"Precision: {precision}")

if __name__ == "__main__":
    main()

