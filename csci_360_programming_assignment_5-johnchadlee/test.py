from lab5_utils import ArtificialNeuralNetwork, mean_squared_error
from lab5 import train, extra_credit
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    np.random.seed(360)
    print("Starting sanity check:")

    print("\tGenerating random data points..,")
    x_train = np.vstack((np.random.uniform(0.5, 1.5, (10, 2)), np.random.uniform(-1.5, -0.5, (10, 2)))).T
    x_test = np.vstack((np.random.uniform(1.0, 2.0, (10, 2)), np.random.uniform(-1.0, 0.0, (10, 2)))).T
    y_train = np.array([1]*10 + [0]*10).reshape(1, -1)
    #######################################################################################################333

    print("\tConstructing Single Layer ANN...")
    ann_simple = ArtificialNeuralNetwork(layers=[2, 1])
    y_pred_pre, _, _ = ann_simple.forward(x_test)
    error_pre = mean_squared_error(y_train, y_pred_pre.astype(int))

    print("\tTraining Single Layer ANN...")
    losses = train(
        neural_network=ann_simple,
        training_inputs=x_train,
        training_labels=y_train,
        n_epochs=10000,
        learning_rate=0.001
    )

    print("\t plotting losses...")
    plt.plot(losses)
    plt.title("Sanity Check Training Loss - Single Layer")
    plt.savefig("sanity-check-training-loss-single-layer.png")

    y_pred_post, _, _ = ann_simple.forward(x_test)
    error_post = mean_squared_error(y_train, y_pred_post.astype(int))

    fig, axs = plt.subplots(1, 2)
    axs[0].scatter(x_test[0, :], x_test[1, :], c=y_pred_pre > 0.5)
    axs[0].set_title(f"Before Training\nMSE: {error_pre:0.2f}")

    axs[1].scatter(x_test[0, :], x_test[1, :], c=y_pred_post > 0.5)
    axs[1].set_title(f"After Training\nMSE: {error_post:0.2f}")
    plt.savefig("sanity-check-predictions-single-layer.png")

    #########################################################################

    print("Constructing Multi Layer ANN...")
    ann_simple = ArtificialNeuralNetwork(layers=[2, 4, 2, 1])
    y_pred_pre, _, _ = ann_simple.forward(x_test)
    error_pre = mean_squared_error(y_train, y_pred_pre.astype(int))

    print("\tTraining ANN...")
    losses = train(
        neural_network=ann_simple,
        training_inputs=x_train,
        training_labels=y_train,
        n_epochs=200,
        learning_rate=0.0001
    )
    print("\tplotting losses...")
    plt.clf()
    plt.plot(losses)
    plt.title("Sanity Check Training Loss - Multi-Layer")
    plt.savefig("sanity-check-training-loss-multi-layer.png")

    y_pred_post, _, _ = ann_simple.forward(x_test)
    error_post = mean_squared_error(y_train, y_pred_post.astype(int))

    fig, axs = plt.subplots(1, 2)
    axs[0].scatter(x_test[0, :], x_test[1, :], c=y_pred_pre > 0.5)
    axs[0].set_title(f"ANN Predictions Before Training\n{error_pre:0.2f}")

    axs[1].scatter(x_test[0, :], x_test[1, :], c=y_pred_post > 0.5)
    axs[1].set_title(f"ANN Predictions After Training\n{error_post:0.2f}")
    plt.savefig("sanity-check-predictions-multi-layer.png")

    ###########################################################################
    print("Loading data from file... ")
    x_train = np.load("training_inputs.npy")
    x_test = np.load("testing_inputs.npy")
    x_plotting = np.load("plotting_inputs.npy")
    input_size = x_train.shape[0]

    y_train = np.load("training_labels.npy").reshape(1, -1)
    y_test = np.load("testing_labels.npy").reshape(1, -1)

    print("Constructing new ANN...")
    multi_layered_ann = ArtificialNeuralNetwork(
        [
            input_size,
            2,
            1
        ]
    )

    y_pred_pre, _, _ = multi_layered_ann.forward(x_test)
    error_pre = mean_squared_error(y_test, y_pred_pre)
    print("Starting ")
    losses = train(
        multi_layered_ann,
        training_inputs=x_train,
        training_labels=y_train,
        n_epochs=5000,
        learning_rate=0.0001
    )
    plt.clf()
    plt.plot(losses)
    plt.title("S Curve Training Loss")
    plt.savefig("s-curve-training-loss.png")
    # plt.show()

    y_pred_post, _, _ = multi_layered_ann.forward(x_test)
    error_post = mean_squared_error(y_test, y_pred_post)

    fig, axs = plt.subplots(1, 3)
    axs[0].scatter(x_plotting[:, 0], x_plotting[:, 1], c=y_test.flatten())
    axs[0].set_title("Ground Truth")

    axs[1].scatter(x_plotting[:, 0], x_plotting[:, 1], c=y_pred_pre.flatten())
    axs[1].set_title(f"Predicted Output prior to training\nMSE: {error_pre:0.4f}")

    axs[2].scatter(x_plotting[:, 0], x_plotting[:, 1], c=y_pred_post.flatten())
    axs[2].set_title(f"Prediction Output after training\nMSE: {error_post:0.4f}")
    plt.savefig("s-curve-regression-results.png")

    ec_results = extra_credit(x_train, y_train, x_test, y_test)
