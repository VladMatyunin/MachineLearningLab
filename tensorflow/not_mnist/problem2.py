from data_loader import train_datasets, test_datasets
import matplotlib.pyplot as plt
from six.moves import cPickle as pickle

file = open(train_datasets[0], 'rb')
data = pickle.load(file)
for i in range(5):
    plt.imshow(data[i], interpolation='nearest')
    plt.show()
file.close()
