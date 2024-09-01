import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split

class Data:
    def __init__(self) -> None:
        self._x = np.empty((0, 1), dtype=float)
        self._y = np.empty((0,), dtype=float)
        self._length: int = 0

    def set_length(self, length=None) -> int:
        if length:
            self._length = length
            return self._length
        message = "Please enter how many points you would like to input: "
        self._length = self._get_positive_interger(message)
        return self._length
    
    def insert_data(self, array1=None, array2=None) -> None:
        if array1 is not None and array2 is not None:
            self._x = array1
            self._y = array2
            return

        self._x = np.empty((self._length, 1), dtype=float)
        self._y = np.empty((self._length, ), dtype=float)

        for i in range(self._length):
            self._x[i] = self._get_float(f"Please enter the x of point #{i + 1}: ")
            self._y[i] = self._get_nonnegative_interger(f"Please enter the y of point #{i + 1}: ")
    
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
    def _get_nonnegative_interger(message: str) -> int:
        while True:
            try:
                value = int(input(message))
                if value >= 0:
                    return value
                else:
                    print("Please enter a non negative integer.")
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
    X_train = X_test = y_train = y_test = None
    
    """
    # dataset for testing
    dataset_size = 1000
    test_size = 0.25

    X = np.random.uniform(-100, 100, dataset_size).reshape(dataset_size, 1)
    y = np.random.randint(0, 2, dataset_size)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    """

    # input training data
    train_set = Data()
    train_set_length = train_set.set_length()
    train_set.insert_data(X_train, y_train)

    # input test data
    test_set = Data()
    test_set_length = test_set.set_length()
    test_set.insert_data(X_test, y_test)

    parameters = {'n_neighbors': list(range(1, 10))}        
    knn = KNeighborsClassifier()

    # parameter cv=5 might cause ValueError when the dataset is small.
    clf = GridSearchCV(knn, parameters, scoring='accuracy', cv=5) 

    clf.fit(train_set.get_x(), train_set.get_y())

    best_k = clf.best_params_['n_neighbors']
    train_set_accuracy = clf.score(train_set.get_x(), train_set.get_y())
    test_set_accuracy = clf.score(test_set.get_x(), test_set.get_y())

    print(f"The best k for KNN Clissification method: {best_k}")
    print(f"Training set accuracy: {train_set_accuracy}")
    print(f"Test set accuracy: {test_set_accuracy}")

if __name__ == "__main__":
    main()

