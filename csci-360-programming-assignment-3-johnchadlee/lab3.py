import numpy as np
import sys # Remove when lab is completed
from lab3_utils import edit_distance, feature_names

# Hint: Consider how to utilize np.unique()
def preprocess_data(training_inputs, testing_inputs, training_labels, testing_labels):
    processed_training_inputs, processed_testing_inputs = ([], [])
    processed_training_labels, processed_testing_labels = ([], [])
    # VVVVV YOUR CODE GOES ERE VVVVV $
    np.set_printoptions(threshold=sys.maxsize)
    # Replace "?"
    #Training_inputs
    for ix, x in enumerate(training_inputs):
        for  iy, y in enumerate(x):
            if y == "?":
                unique, counts = np.unique(training_inputs[:,iy], return_counts=True)
                mode = 0
                maxC = max(counts)
                for idx, c in enumerate(counts):
                    if(c == maxC):
                        mode = unique[idx]
                training_inputs[ix,iy] = mode
                
    #Testing_inputs
    for ix, x in enumerate(testing_inputs):
        for  iy, y in enumerate(x):
            if y == "?":
                unique, counts = np.unique(testing_inputs[:,iy], return_counts=True)
                mode = ""
                maxC = max(counts)
                for idx, c in enumerate(counts):
                    if(c == maxC):
                        mode = unique[idx]
                testing_inputs[ix,iy] = mode    
    #Convert categorical features by counting levels in each category
    #Yes or no features, left or right features columms: 4, 6, 8
    for ix, x in enumerate(training_inputs[:,4]):
        if training_inputs[ix,4] == "yes":
            training_inputs[ix,4] = 1
        else:
            training_inputs[ix,4] = 0
    for ix, x in enumerate(training_inputs[:,6]):
        if training_inputs[ix,6] == "yes":
            training_inputs[ix,6] = 1
        else:
            training_inputs[ix,6] = 0
    for ix, x in enumerate(training_inputs[:,8]):
        if training_inputs[ix,8] == "yes":
            training_inputs[ix,8] = 1
        else:
            training_inputs[ix,8] = 0
    #Ordinal features age 0, tumori-size 2, inv-nodes 3, and deg-malig 5.
    # age
    for ix, x in enumerate(training_inputs[:,0]):
        if training_inputs[ix,0] == "0-9":
            training_inputs[ix,0] = 1
        if training_inputs[ix,0] == "10-19":
            training_inputs[ix,0] = 2
        if training_inputs[ix,0] == "20-29":
            training_inputs[ix,0] = 3
        if training_inputs[ix,0] == "30-39":
            training_inputs[ix,0] = 4
        if training_inputs[ix,0] == "40-49":
            training_inputs[ix, 0] = 5
        if training_inputs[ix,0] == "50-59":
            training_inputs[ix, 0] = 6
        if training_inputs[ix,0] == "60-69":
            training_inputs[ix, 0] = 7
        if training_inputs[ix,0] == "70-79":
            training_inputs[ix, 0] = 8
        if training_inputs[ix,0] == "80-89":
            training_inputs[ix, 0] = 9
        if training_inputs[ix,0] == "90-99":
            training_inputs[ix, 0] = 10
    # tumor size
    for ix, x in enumerate(training_inputs[:,2]):
        if training_inputs[ix,2] == "0-4":
            training_inputs[ix,2] = 1
        if training_inputs[ix,2] == "5-9":
            training_inputs[ix,2] = 2
        if training_inputs[ix,2] == "10-14":
            training_inputs[ix,2] = 3
        if training_inputs[ix,2] == "15-19":
            training_inputs[ix,2] = 4
        if training_inputs[ix,2] == "20-24":
            training_inputs[ix,2] = 5
        if training_inputs[ix,2] == "25-29":
            training_inputs[ix,2] = 6
        if training_inputs[ix,2] == "30-34":
            training_inputs[ix,2] = 7
        if training_inputs[ix,2] == "35-39":
            training_inputs[ix,2] = 8
        if training_inputs[ix,2] == "40-44":
            training_inputs[ix,2] = 9
        if training_inputs[ix,2] == "45-49":
            training_inputs[ix,2] = 10
        if training_inputs[ix,2] == "50-54":
            training_inputs[ix,2] = 11
        if training_inputs[ix,2] == "55-59":
            training_inputs[ix,2] = 12
        if training_inputs[ix,2] == "60-64":
            training_inputs[ix,2] = 13
    #inv_node
    for ix, x in enumerate(training_inputs[:,3]):
        if training_inputs[ix,3] == "0-2":
            training_inputs[ix,3] = 1
        if training_inputs[ix,3] == "3-5":
            training_inputs[ix,3] = 2
        if training_inputs[ix,3] == "6-8":
            training_inputs[ix,3] = 3
        if training_inputs[ix,3] == "9-11":
            training_inputs[ix,3] = 4
        if training_inputs[ix,3] == "12-14":
            training_inputs[ix,3] = 5
        if training_inputs[ix,3] == "15-17":
            training_inputs[ix,3] = 6
        if training_inputs[ix,3] == "18-20":
            training_inputs[ix,3] = 7
        if training_inputs[ix,3] == "21-23":
            training_inputs[ix,3] = 8
        if training_inputs[ix,3] == "24-26":
            training_inputs[ix,3] = 9
        if training_inputs[ix,3] == "27-29":
            training_inputs[ix,3] = 10
    #menopause 1
    training_inputs = np.insert(training_inputs, 1, 0, axis=1)
    training_inputs = np.insert(training_inputs, 1, 0, axis=1)
    training_inputs = np.insert(training_inputs, 1, 0, axis=1)
    for ix, x in enumerate(training_inputs[:,4]):
        if training_inputs[ix,4] == "ge40":
            training_inputs[ix,1] = 1
        if training_inputs[ix,4] == "premeno":
            training_inputs[ix, 2] = 1
        if training_inputs[ix,4] == "lt40":
            training_inputs[ix, 3] = 1
    training_inputs = np.delete(training_inputs,4,1)
    # #One Hot encode for quadrant 7
    training_inputs = np.insert(training_inputs, 9, 0, axis=1)
    training_inputs = np.insert(training_inputs, 9, 0, axis=1)
    training_inputs = np.insert(training_inputs, 9, 0, axis=1)
    training_inputs = np.insert(training_inputs, 9, 0, axis=1)
    training_inputs = np.insert(training_inputs, 9, 0, axis=1)
    for ix, x in enumerate(training_inputs[:,7]):
        if training_inputs[ix,14] == "left_up":
            training_inputs[ix,9] = 1
        elif training_inputs[ix,14] == "left_low":
            training_inputs[ix,10] = 1
        elif training_inputs[ix,14] == "right_up":
            training_inputs[ix,11] = 1
        elif training_inputs[ix,14] == "right_low":
            training_inputs[ix,12] = 1
        elif training_inputs[ix,14] == "central":
            training_inputs[ix,13] = 1
    training_inputs = np.delete(training_inputs, 14, 1)
    # TESTING INPUTS
    #Convert categorical features by counting levels in each category
    #Yes or no features, left or right features columms: 4, 6, 8
    for ix, x in enumerate(testing_inputs[:,4]):
        if testing_inputs[ix,4] == "yes":
            testing_inputs[ix,4] = 1
        else:
            testing_inputs[ix,4] = 0
    for ix, x in enumerate(testing_inputs[:,6]):
        if testing_inputs[ix,6] == "yes":
            testing_inputs[ix,6] = 1
        else:
            testing_inputs[ix,6] = 0
    for ix, x in enumerate(testing_inputs[:,8]):
        if testing_inputs[ix,8] == "yes":
            testing_inputs[ix,8] = 1
        else:
            testing_inputs[ix,8] = 0
    #Ordinal features age 0, tumori-size 2, inv-nodes 3, and deg-malig 5.
    # age
    for ix, x in enumerate(testing_inputs[:,0]):
        if testing_inputs[ix,0] == "0-9":
            testing_inputs[ix,0] = 1
        if testing_inputs[ix,0] == "10-19":
            testing_inputs[ix,0] = 2
        if testing_inputs[ix,0] == "20-29":
            testing_inputs[ix,0] = 3
        if testing_inputs[ix,0] == "30-39":
            testing_inputs[ix,0] = 4
        if testing_inputs[ix,0] == "40-49":
            testing_inputs[ix, 0] = 5
        if testing_inputs[ix,0] == "50-59":
            testing_inputs[ix, 0] = 6
        if testing_inputs[ix,0] == "60-69":
            testing_inputs[ix, 0] = 7
        if testing_inputs[ix,0] == "70-79":
            testing_inputs[ix, 0] = 8
        if testing_inputs[ix,0] == "80-89":
            testing_inputs[ix, 0] = 9
        if testing_inputs[ix,0] == "90-99":
            testing_inputs[ix, 0] = 10
    # tumor size
    for ix, x in enumerate(testing_inputs[:,2]):
        if testing_inputs[ix,2] == "0-4":
            testing_inputs[ix,2] = 1
        if testing_inputs[ix,2] == "5-9":
            testing_inputs[ix,2] = 2
        if testing_inputs[ix,2] == "10-14":
            testing_inputs[ix,2] = 3
        if testing_inputs[ix,2] == "15-19":
            testing_inputs[ix,2] = 4
        if testing_inputs[ix,2] == "20-24":
            testing_inputs[ix,2] = 5
        if testing_inputs[ix,2] == "25-29":
            testing_inputs[ix,2] = 6
        if testing_inputs[ix,2] == "30-34":
            testing_inputs[ix,2] = 7
        if testing_inputs[ix,2] == "35-39":
            testing_inputs[ix,2] = 8
        if testing_inputs[ix,2] == "40-44":
            testing_inputs[ix,2] = 9
        if testing_inputs[ix,2] == "45-49":
            testing_inputs[ix,2] = 10
        if testing_inputs[ix,2] == "50-54":
            testing_inputs[ix,2] = 11
        if testing_inputs[ix,2] == "55-59":
            testing_inputs[ix,2] = 12
        if testing_inputs[ix,2] == "60-64":
            testing_inputs[ix,2] = 13
    #inv_node
    for ix, x in enumerate(testing_inputs[:,3]):
        if testing_inputs[ix,3] == "0-2":
            testing_inputs[ix,3] = 1
        if testing_inputs[ix,3] == "3-5":
            testing_inputs[ix,3] = 2
        if testing_inputs[ix,3] == "6-8":
            testing_inputs[ix,3] = 3
        if testing_inputs[ix,3] == "9-11":
            testing_inputs[ix,3] = 4
        if testing_inputs[ix,3] == "12-14":
            testing_inputs[ix,3] = 5
        if testing_inputs[ix,3] == "15-17":
            testing_inputs[ix,3] = 6
        if testing_inputs[ix,3] == "18-20":
            testing_inputs[ix,3] = 7
        if testing_inputs[ix,3] == "21-23":
            testing_inputs[ix,3] = 8
        if testing_inputs[ix,3] == "24-26":
            testing_inputs[ix,3] = 9
        if testing_inputs[ix,3] == "27-29":
            testing_inputs[ix,3] = 10
    #menopause 1
    testing_inputs = np.insert(testing_inputs, 1, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 1, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 1, 0, axis=1)
    for ix, x in enumerate(testing_inputs[:,4]):
        if testing_inputs[ix,4] == "ge40":
            testing_inputs[ix,1] = 1
        if testing_inputs[ix,4] == "premeno":
            testing_inputs[ix, 2] = 1
        if testing_inputs[ix,4] == "lt40":
            testing_inputs[ix, 3] = 1
    testing_inputs = np.delete(testing_inputs,4,1)
    #One Hot encode for quadrant 7
    testing_inputs = np.insert(testing_inputs, 9, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 9, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 9, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 9, 0, axis=1)
    testing_inputs = np.insert(testing_inputs, 9, 0, axis=1)
    for ix, x in enumerate(testing_inputs[:,7]):
        if testing_inputs[ix,14] == "left_up":
            testing_inputs[ix,9] = 1
        elif testing_inputs[ix,14] == "left_low":
            testing_inputs[ix,10] = 1
        elif testing_inputs[ix,14] == "right_up":
            testing_inputs[ix,11] = 1
        elif testing_inputs[ix,14] == "right_low":
            testing_inputs[ix,12] = 1
        elif testing_inputs[ix,14] == "central":
            testing_inputs[ix,13] = 1
    testing_inputs = np.delete(testing_inputs, 14, 1)
    # Return processed data
    processed_training_inputs = training_inputs
    processed_testing_inputs = testing_inputs
    processed_training_labels = training_labels
    processed_testing_labels = testing_labels
    # ^^^^^ YOUR CODE GOES ERE ^^^^^ $
    return processed_training_inputs, processed_testing_inputs, processed_training_labels, processed_testing_labels



# Hint: consider how to utilize np.argsort()
def k_nearest_neighbors(predict_on, reference_points, reference_labels, k, l, weighted):
    assert len(predict_on) > 0, f"parameter predict_on needs to be of length 0 or greater"
    assert len(reference_points) > 0, f"parameter reference_points needs to be of length 0 or greater"
    assert len(reference_labels) > 0, f"parameter reference_labels needs to be of length 0 or greater"
    assert len(reference_labels) == len(reference_points), f"reference_points and reference_labels need to be the" \
                                                           f" same length"
    predictions = []
    # VVVVV YOUR CODE GOES ERE VVVVV $
    dist = 0
    
    # compare one patient to all patients in testing
    for i, x in enumerate(predict_on):
        reference = []
        for j, y in enumerate(reference_points):
            dist = (edit_distance(predict_on[i], reference_points[j], l) )
            reference.append(dist)
        sort = np.argsort(reference, axis=0)
        sort = sort[:k]
        no_count = 0
        yes_count = 0
        for i, x in enumerate(sort):
            # print(sort[i])
            if(reference_labels[sort[i]] == "no-recurrence-events"):
                no_count+=1
            else:
                yes_count+=1
        if no_count == yes_count:
            predictions.append("no-recurrence-events")
        elif no_count < yes_count:
            predictions.append("recurrence-events")
        else: 
            predictions.append("no-recurrence-events")   
    # ^^^^^ YOUR CODE GOES ERE ^^^^^ $
    return predictions
