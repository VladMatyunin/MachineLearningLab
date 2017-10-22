import os
from merge_dataset import train_dataset, test_dataset, valid_dataset
from merge_dataset import train_labels, test_labels, valid_labels
from six.moves import cPickle as pickle
from sklearn.linear_model import LogisticRegression
from download import data_root

pickle_file = os.path.join(data_root, 'notMNIST.pickle')

try:
    f = open(pickle_file, 'wb')
    save = {
        'train_dataset': train_dataset,
        'train_labels': train_labels,
        'valid_dataset': valid_dataset,
        'valid_labels': valid_labels,
        'test_dataset': test_dataset,
        'test_labels': test_labels,
    }
    pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
    f.close()
except Exception as e:
    print('Unable to save data to', pickle_file, ':', e)
    raise

statinfo = os.stat(pickle_file)
print('Compressed pickle size:', statinfo.st_size)

number_of_training_images_to_use = 50000 # max = 200000

with open(pickle_file, 'rb') as f:
  save = pickle.load(f)
  train_dataset = save['train_dataset']
  train_labels = save['train_labels']
  valid_dataset = save['valid_dataset']
  valid_labels = save['valid_labels']
  test_dataset = save['test_dataset']
  test_labels = save['test_labels']
  del save  # hint to help gc free up memory
# print('Training set', train_dataset.shape, train_labels.shape)
# print('Validation set', valid_dataset.shape, valid_labels.shape)
# print('Test set', test_dataset.shape, test_labels.shape)


def flattify(some_ndarray):
    """This method converts each of the pictures to a 1D array of the pixels"""
    return some_ndarray.reshape(some_ndarray.shape[0], -1)


classifier = LogisticRegression(verbose=1,
                                n_jobs=-1,
                                solver='sag',
                                max_iter=200)

print("Starting fitting...")
classifier.fit(flattify(train_dataset[:number_of_training_images_to_use]),
                        train_labels[:number_of_training_images_to_use])

print("Fitting finished and score on test dataset is {}".format(
    classifier.score(flattify(test_dataset), test_labels)
    )
)