# MNIST Digit 0 Classifier

This project implements a simple neural network to classify handwritten digits from the MNIST dataset as **"0" or "not 0"**. It uses the sigmoid activation function, quadratic cost, and learns via gradient descent and backpropagation.


## Objective

- Predict whether a given image represents the digit **0**.
  - **Output = 1** if the image is a **0**
  - **Output = 0** if the image is **any other digit (1–9)**


## How It Works

The project consists of **3 main steps**:

### 1. Load Data
Users must provide all of the following file paths:
- `train_image` and `train_labels`
- `test_image` and `test_labels`
There is no automatic train-test split — all data must be prepared in advance by the user.

### 2. Train Model
Call the training function by providing:
- `train_image`, `train_labels`
- Choose your own:
  - **Number of iterations**
  - **Learning rate**

### 3. Test Model
Evaluate the model using `test_image` after training.
A plot will be shown of **iterations vs. cost**, helping visualize learning progress.


## Features

- Binary classification (0 vs not-0)
- **Sigmoid** activation
- **Quadratic cost function**
- **Gradient descent + backpropagation**
- Plot: iterations vs cost


## Requirements

- Python 3.12.11
- Matplotlib
