import numpy as np
import math


class MyLinearClassifier:
    def __init__(self, size):
        self.period = 1
        self.size = size+1
        self.grad_step = 10
        self.params = np.random.randint(-1, 1, size=size+1)

    def fit(self, data, result):
        for i in range(0, len(data)):
            # prepend 1 to array of X values for easy computations
            full_data = [1, data[i]]
            self.apply(full_data, result[i])

    def apply(self, row_data, row_result):
        deltas = []
        full_data = [1]
        for i in range(0, len(row_data)):
            full_data.append(row_data[i])
        # find out classifier's errors
        for i in range(0, self.size):
            deltas.append(full_data[i]*(1 / (4 * self.period * self.grad_step*self.size)) *
                          (np.sum(np.multiply(self.params, full_data)) - row_result))
        self.period += 1
        # apply the errors
        for i in range(0, self.size):
            self.params[i] -= deltas[i]

    # returns MSE of current classifier according to input values
    def get_error(self, row_data, row_result):
        math_row_data = [1]
        for i in range(0, len(row_data)):
            math_row_data.append(row_data[i])
        return math.pow((np.sum(np.multiply(self.params, math_row_data)) - row_result), 2) / len(row_data)

    def predict(self, row_data):
        return np.sum(np.multiply(self.params, row_data))
