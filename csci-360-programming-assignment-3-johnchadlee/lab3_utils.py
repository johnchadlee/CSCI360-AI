import numpy as np

data_filename = "data.npy"

feature_names = [
    'age_group',
    'menopause',
    'tumor_size',
    'inv_nodes',
    'node_caps',
    'deg_malig',
    'side',
    'quadrant',
    'irradiated'
]


def edit_distance(u, v, l):
    if l == -1:
        return np.sum((np.array(u) == np.array(v)).astype(int))
    elif l == 0:
        raise Exception("l cannot equal 0")
    elif l == np.inf:
        return np.max(np.abs(np.array(u) - np.array(v)))

    return np.power(
        np.sum(
            np.power(np.abs(np.array(u) - np.array(v)), l)
        ), np.divide(1, l))


def accuracy_score(true_labels, predicted_labels):
    return np.average((np.array(true_labels) == np.array(predicted_labels)).astype(int))


def load_data():
    training_inputs, testing_inputs, training_labels, testing_labels = np.load(data_filename, allow_pickle=True)
    return training_inputs, testing_inputs, training_labels, testing_labels