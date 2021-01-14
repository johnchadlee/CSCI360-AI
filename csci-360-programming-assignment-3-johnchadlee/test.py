from lab3_utils import (
    accuracy_score,
    load_data
)
from lab3 import k_nearest_neighbors, preprocess_data
import numpy as np
import time


if __name__ == "__main__":
    print(f"Loading data from file...")
    start_time = time.time()
    raw_data = load_data()
    load_time = time.time() - start_time
    print(f"Data loaded - time elapsed from start: {load_time:0.9f}")
    print(f"Beginning data preprocessing and cleaning...")
    processed_training_inputs, processed_testing_inputs, processed_training_labels, processed_testing_labels =\
        preprocess_data(*raw_data)
    load_time = time.time() - start_time
    print(f"Data preprocessed - time elapsed from start: {load_time:0.9f}")
    print(f"Example training input: {processed_training_inputs[0]} - label: {processed_training_labels[0]}")
    l_norms = [-1, 1, 2, 3, 4, 5, 6, np.inf]
    k_max = 30
    weighting_options = [True, False]
    accuracies = np.zeros((k_max, len(l_norms), len(weighting_options)))
    for k in range(1, k_max+1):
        for l_i, l_norm in enumerate(l_norms):
            for w, weighting in enumerate(weighting_options):
                print(f"Running kNN with k= {k}, l= {l_norm}, weighting={weighting}")
                predicted_labels = k_nearest_neighbors(
                    predict_on=processed_testing_inputs,
                    reference_points=processed_training_inputs,
                    reference_labels=processed_training_labels,
                    k=k,
                    l=l_norm,
                    weighted=weighting
                )
                load_time = time.time() - start_time
                print(f"kNN completer - time elapsed from start: {load_time:0.9f}")
                accuracies[k-1, l_i, w] = accuracy_score(processed_testing_labels, predicted_labels)

    best_accuracy = np.max(accuracies)
    best_k, best_metric, best_weighting = np.where(accuracies == best_accuracy)
    print(f"Highest accuracy achieved: {best_accuracy:0.4f}")
    for k, l, w in zip(best_k, best_metric, best_weighting):
        print(f"\t k= {k+1} - l= {l_norms[l]} - weighting= {weighting_options[w]}]")

