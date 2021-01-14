import numpy as np

def relu(x):
    return np.maximum(0, x)

def mean_squared_error(y, y_hat):
    assert y.shape[0] == y_hat.shape[0], f"{y.shape[0]} != {y_hat.shape[0]} - " \
                                           f"number of predictions does not match the number of labels"
    return np.mean(np.power((y - y_hat), 2))


class ArtificialNeuralNetwork(object):

    def __init__(self, layers=[], random_seed=360):
        np.random.seed(random_seed)
        self.layers = []
        self.biases = []
        for i in range(1, len(layers)):
            output_size = layers[i]
            input_size = layers[i-1]

            self.layers.append(
                np.random.normal(
                    loc=0.0,
                    scale=np.sqrt(layers[i-1]),
                    size=(output_size, input_size)
                )
            )
            self.biases.append(
                np.random.random((output_size, 1))
            )


    def forward(self, x):
        assert isinstance(x, np.ndarray), "input should be a numpy ndarray"
        assert len(x.shape) == 2, f"x is expected to be two dimensional array"
        assert x.shape[0] == self.layers[0].shape[1], f"input size of x, {x.shape[0]} does not match neural network's" \
                                                      f" input layer size of {self.layers[0].shape[1]}"
        a = x.copy()
        a_memory = []
        z_memory = [None]

        for layer, bias in zip(self.layers, self.biases):
            z = np.dot(layer, a) + bias
            z_memory.append(z)
            a_memory.append(a)

            a = relu(z)

        return a, a_memory, z_memory

    def at_layer(self, x, layer_index):
        assert layer_index <= len(self.layers)
        a = z = x.copy()
        for layer, bias in zip(self.layers[:layer_index], self.biases[:layer_index]):
            z = np.dot(a, layer) + bias
            a = relu(z)

        return a, z