# This is to load MNIST dataset
# Input: file path of MNIST dataset
# Output: training_data and testing_data with images and labels


import struct
from array import array
from typing import Tuple, List


def transform_labels_to_binary(mnist_labels: List[int]) -> List[int]:
    """
    MNIST labels are for multiple classification of digits 0 to 9.
    This function is written to change labels to match binary classification -
    problem of recognizing single digit 0.
    """

    labels = [1 if digit == 0 else 0 for digit in mnist_labels]

    return labels


def normalize_pixel_values(image: List[int]) -> List[float]:
    """
    Image pixel values range from 0 to 255.
    This was resulting large z value,
    which causes OverflowError in calculating activation.
    We will apply min-max feature scaling.
    """
    return [pixel_value / 255 for pixel_value in image]


# MNIST Data Loader Function
def read_images_labels(
    images_filepath: str, labels_filepath: str
) -> Tuple[List, List]:
    labels = []

    with open(labels_filepath, "rb") as file:
        magic, size = struct.unpack(">II", file.read(8))
        if magic != 2049:
            raise ValueError(
                "Magic number mismatch, expected 2049, got {}".format(magic)
            )
        labels = array("B", file.read())

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
        img = image_data[i * rows * cols : (i + 1) * rows * cols]  # noqa E203
        images[i][:] = img

    return images, list(labels)
