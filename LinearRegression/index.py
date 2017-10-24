import pandas as pd
import linear_classifier as classifier
import math
data_frame = pd.read_csv('train.csv')
data_types = []
string_data_values = []
epsilon = 3.883
classifier = classifier.MyLinearClassifier(80)

for index, row in data_frame.iteritems():
    data_types.append(row.dtype)
for i in range(0, len(data_types)):
    string_data_values.append([])
for i in range(0, 100):
    epoch_error = 0
    for index, row in data_frame.iterrows():
        train_data = []
        for j in range(0,  80):
            if data_types[j] == object:
                if not string_data_values[j].__contains__(row[j]):
                    string_data_values[j].append(row[j])
                data_index = string_data_values[j].index(row[j])
                train_data.append(data_index*100+epsilon)
            else:
                train_data.append(row[j])
        result = row[80]
        epoch_error += math.fabs(classifier.get_error(train_data, result)/result)
        classifier.apply(train_data, result)
    print(epoch_error/data_frame.size)
print(len(data_types))
