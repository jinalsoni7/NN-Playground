import matplotlib.pyplot as plt
import math

from typing import List


def plot(costs: List[float], number_of_iterations: int) -> None:
    fig, ax = plt.subplots()  # figure with single axes
    x_data = [i for i in range(number_of_iterations)]
    y_data = [math.log(i) for i in costs]

    # figure's metadata
    ax.set_title("cost over iterations")
    ax.set_xlabel("number of iterations")
    ax.set_ylabel("cost")

    ax.plot(x_data, y_data, color="red", linestyle="solid")

    plt.show()
