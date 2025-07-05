"""
Gradient Descent for a perceptron

1) we have an input x and output y
2) we initialize weight(w) and bias(b)
3) calculate z = wx + b
4) calculate a = sigmoid(z)
5) cost function C = (1/2n)(a - y)^2
6) Gradient descent = partial derivation of C with w and
                        partial derivation of C with b

    ∂C/∂w = a(1-a)(a-y)x
    ∂C/∂b = a(1-a)(a-y)

-----------------------------------------------------------------------
PROOF

∂c/∂w = ∂c/∂a * ∂a/∂z * ∂z/∂w
    = (1-y) * sigmoid`(z) * x
    = (1-y)a(1-a)x

sigmoid(z) = 1 / (1+e^-z)
∂(sigmoid(z)) = (1+e^-z)^-2 e^-z
                = e^-z / (1 + e^-z)^2
                = (1 / (1 + e^-z)) (e^-z / ((1 + e^-z)))
                = sigmoid(z) (1 - sigmoid(z))
                = a (1 - a)

1 - sigmoid(z) = 1 - (1 / (1+e^-z))
                = 1 + e^-z -1 / (1 + e^-z)
                =  (e^-z / ((1 + e^-z)))
-----------------------------------------------------------------------

7) w' = w - µ . ∂C/∂w
    b' = b - µ . ∂C/∂b

"""

from typing import List, Tuple
import random
import math


def initialize_weights_bias(num_features: int) -> Tuple[List[float], float]:
    weights = [random.gauss(mu=0.0, sigma=1.0) for i in range(num_features)]
    bias = random.gauss(mu=0.0, sigma=1.0)

    return weights, bias


def activation_sigmoid(
    weights: List[float], bias: float, input_x: List[float]
) -> float:
    wx = 0
    for i in range(len(input_x)):
        wx += weights[i] * input_x[i]
    z = wx + bias

    activation_value = 1 / (1 + math.exp(-z))

    return activation_value


def partial_derivatives(
    activation_value: float, output_y: float, input_x: List[float]
) -> Tuple[List[float], float]:
    # ∂C/∂b = a(1-a)(a-y)
    partial_derivation_with_bias = (
        activation_value
        * (1 - activation_value)
        * (activation_value - output_y)
    )

    # ∂C/∂w = a(1-a)(a-y)x
    partial_derivation_with_weights = [
        partial_derivation_with_bias * i for i in input_x
    ]

    return partial_derivation_with_weights, partial_derivation_with_bias


def quadratic_cost(activation: float, output_y: float) -> float:
    cost = 0.5 * ((activation - output_y) ** 2)

    return cost
