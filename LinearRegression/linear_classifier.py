import numpy as np
import math


class MyLinearClassifier:
    def __init__(self, size):
        self.period = 1
        self.size = size + 1
        self.grad_step = 0.00000001
        self.params = np.random.random_sample(size=size + 1)
        for i in range(0, size+1):
            self.params[i] += np.random.randint(-5, 5)

    def fit(self, data, result):
        full_data = [1]

        for i in range(0, len(data)):
            # prepend 1 to array of X values for easy computations
            full_data = [1, data[i]]
            self.apply(full_data, result[i])

    def apply(self, row_data, row_result):

        full_data = [1]
        for i in range(0, len(row_data)):
            full_data.append(row_data[i])
        deltas = []
        # find out classifier's errors
        predicted_value = self.predict(full_data)
        for i in range(0, self.size):
            self.params[i] = self.params[i] - full_data[i] * ((predicted_value - row_result) * self.grad_step / self.period)
        self.period += 1

    # returns MSE of current classifier according to input values
    def get_error(self, row_data, row_result):
        math_row_data = [1]
        for i in range(0, len(row_data)):
            math_row_data.append(row_data[i])
        return self.predict(math_row_data) - row_result

    def predict(self, row_data):
        for i in range(0, len(row_data)):
            if np.isnan(row_data[i]):
                row_data[i] = 1
        return np.sum(np.multiply(self.params, row_data))
