from gradient_descent import define_weights_bias, gradient_descent
from typing import List
import matplotlib.pyplot as plt


# input_x and output_y
input_x = [0.0, 0.75, 0.50, 1.0]
output_y = 1.0

weights, bias = define_weights_bias(input_x=input_x)m

for iteration in range(10000):
    updated_weights, updated_bias = gradient_descent(
        input_x=input_x, output_y=output_y, weights=weights, bias=bias)

    weights = updated_weights
    bias = updated_bias

def plot(cost: List, iterations:int) -> None:
    pass