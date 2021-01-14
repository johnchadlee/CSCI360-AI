# Lab 3: K Nearest Neighbors

**CSCI 360: Introduction to Artificial Intelligence**

## Introduction
In this lab you will be implementing the k Nearest Neighbors. The
algorithm uses a distance function and a training set, By using the
distance metrics to look up $$k$$ closest points to an example, we can
average or "vote" on the label that is predicted.

In this lab you will be implementing the algorithm, but first you will
have to clean the data. The data is found in the [`data.npy`](./data.npy).

All the code you write should be in [`lab3.py`](./lab3.py) and you will be
under functions `preprocess_data` and `k_nearest_neighbors`. It is
important you don't change the parameters. You are provided with a
utility file and a test file. The utility file has functions provided
that will compute the `edit_distance`, `accuracy_score`, and `load_data`.

It also contains the names of the features in the dataset in the order that they appear in the columns.

You are allowed to use `numpy` which is outlined by [`requirements.txt`](./requirements.txt)

## Utility file:
### `edit_distance(u, v, l)`

Edit distance can take 2 arrays and a parameter `l`.

`l` can be -1, any real positive number or `numpy.inf`

```
>>> from lab3_utils import edit_distance
>>> edit_distance([1, 2, 3], [1, 2, 3], 1) == 0
True
```



## Test File:
The test file can be run it will try to use the `preprocess_data` and `k_nearest_neighbors` as they are outline in the lab3 PDF.

The test file uses `load_data` this pulls a tuple from the data
