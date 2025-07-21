# This is Neural Network to classify whether the given image is digit 0 or not.

import numpy as np
from typing import List, Tuple
from statistics import mean
from .mnist_loader import normalize_pixel_values
from .gradient_descent import (
    initialize_weights_bias,
    activation_sigmoid,
    partial_derivatives,
)


def train(
    x_input: List[List[int]],
    y_output: List,
    number_of_iterations: int,
    learning_rate: float,
) -> Tuple[List[float], float]:
    # initialize weights and bias -- weights will be of size x_input[0] and -
    # bias will be of size 1 since there is only one layer of neurons
    weights, bias = initialize_weights_bias(num_features=len(x_input[0]))
    normalized_x_input = [normalize_pixel_values(image=x) for x in x_input]

    # repeat number_of_iterations times
    for iteration in range(number_of_iterations):
        # store partial derivatives of c with respect w and b
        dw_list, db_list = [], []

        for example, label in zip(normalized_x_input, y_output):
            # calculate z = ∑wx + b and thus calculate a = sigmoid(z)
            activation_value = activation_sigmoid(
                weights=weights, bias=bias, input_x=example
            )

            # calculate ∂C/∂w and ∂C/∂b -- store it to later average it
            dw, db = partial_derivatives(
                activation_value=activation_value,
                output_y=label,
                input_x=example,
            )

            dw_list.append(dw)
            db_list.append(db)

        # average dw and db
        avg_dws = np.mean(dw_list, axis=0).tolist()
        avg_db = mean(db_list)

        # Update weights
        updated_weights = []
        for init_w, avg_dw in zip(weights, avg_dws):
            updated_w = init_w - (learning_rate * avg_dw)
            updated_weights.append(updated_w)

        # Update bias
        updated_bias = bias - (learning_rate * avg_db)

        # use this for next iteration
        weights = updated_weights
        bias = updated_bias

    return weights, bias


def predict(x_input: List[int], parameters: Tuple) -> int:
    weights, bias = parameters
    normalized_x_input = normalize_pixel_values(image=x_input)

    # calculate z = ∑wx + b and thus calculate a = sigmoid(z)
    activation_value = activation_sigmoid(
        weights=weights, bias=bias, input_x=normalized_x_input
    )

    return 1 if activation_value >= 0.5 else 0


def accuracy(y_actual: List, y_predicted: List):
    correct_classifications = 0
    total_classifications = len(y_actual)

    for actual, predicted in zip(y_actual, y_predicted):
        if actual == predicted:
            correct_classifications += 1

    accuracy = correct_classifications / total_classifications

    return accuracy
