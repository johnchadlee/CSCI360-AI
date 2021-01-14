import numpy as np
from lab5_utils import log_loss, sigmoid, ArtificialNeuralNetwork

def d_mse(y, y_hat):
    pass


def d_relu(x):
    pass

# consider how you can use ArtificialNeuralNetwork.forward and ArtificialNeuralNetwork.at_layer to help with BP
def train(
    neural_network,
    training_inputs,
    training_labels,
    n_epochs,
    learning_rate=0.001
):
    losses = []
    return losses


def extra_credit(x_train, y_train, x_test, y_test):
    #populate this dictionary with your extra credit experiments...
    results = {
        "architectures": [],
        "n_epochs": [],
        "learning_rate": [],
        "training_losses": [],
        "evaluation_mean_squared_error": []
    }

    return results