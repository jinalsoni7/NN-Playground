# This is to load MNIST dataset
# Input: file path of MNIST dataset
# Output: training_data and testing_data with images and labels


import struct
from array import array
from typing import Tuple, List


def etl_data(prev_labels: List) -> List:
    """
    Current lables data supports multiple classification of digits 0 to 9.
    This function is written to change labels data to match single classification problem of recognizing single digit 0.
    """

    labels = [1 if digit == 0 else 0 for digit in prev_labels]

    return labels


# MNIST Data Loader Function
def read_images_labels(images_filepath: str, labels_filepath: str) -> Tuple[List, List]:
    labels = []

    with open(labels_filepath, "rb") as file:
        magic, size = struct.unpack(">II", file.read(8))
        if magic != 2049:
            raise ValueError(
                "Magic number mismatch, expected 2049, got {}".format(magic)
            )
        multi_labels = array("B", file.read())

    with open(images_filepath, "rb") as file:
        magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
        if magic != 2051:
            raise ValueError(
                "Magic number mismatch, expected 2051, got {}".format(magic)
            )
        image_data = array("B", file.read())

    images = []

    for i in range(size):
        images.append([0] * rows * cols)

    for i in range(size):
        img = image_data[i * rows * cols : (i + 1) * rows * cols]
        images[i][:] = img

    labels = etl_data(prev_labels=list(multi_labels))

    return images, labels
