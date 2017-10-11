from data_loader import train_datasets, test_datasets
import matplotlib.pyplot as plt
from six.moves import cPickle as pickle

labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
labels_ticks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_dataset(pickle_file):
    dataset = []
    with open(pickle_file, 'rb') as file:
        data = pickle.load(file)
        print(pickle_file, " :", data.shape[0])
        dataset.append(data.shape[0])
    return dataset


print("Train dataset\n")
full_train_dataset = []
full_test_dataset = []

for pick_file in train_datasets:
    full_train_dataset.append(test_dataset(pick_file))

print("Test dataset\n")

for pick_file in test_datasets:
    full_test_dataset.append(test_dataset(pick_file))

# TODO: set scale for y-axis
plt.xticks(labels_ticks, labels)
plt.xticks(range(10), labels, rotation=45)
plt.plot(labels_ticks, full_test_dataset, '*')
plt.show()

plt.xticks(labels_ticks, labels)

plt.xticks(range(10), labels, rotation=45)
plt.plot(labels_ticks, full_train_dataset, '*')
plt.show()
