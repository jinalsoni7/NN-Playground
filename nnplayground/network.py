# This is Neural Network to classify whether the given image is digit 0 or not.

from typing import List
from statistics import mean

from gradient_descent import (
    initialize_weights_bias,
    activation_sigmoid,
    partial_derivatives,
)


def train(
    x_input: List[List],
    y_output: List,
    number_of_iterations: int,
    learning_rate: float,
):
    # initialize weights and bias -- weights will be of size x_input[0] and -
    # bias will be of size 1 since there is only one layer of neurons
    weights, bias = initialize_weights_bias(num_features=len(x_input[0]))

    # repeat number_of_iterations times
    for iteration in range(number_of_iterations):
        # store partial derivatives of c with respect w and b
        dw_list, db_list = [], []

        for example, label in zip(x_input, y_output):
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
        avg_dws = list(*map(mean, zip(*dw_list)))
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


def predict(x_input: List[List], parameters):
    pass


def accuracy(y_actual: List, y_predicted: List):
    pass
