from nnplayground import network, mnist_loader
import pickle

x_train, y_train = mnist_loader.read_images_labels(
    images_filepath="archive/train-images.idx3-ubyte",
    labels_filepath="archive/train-labels.idx1-ubyte",
)

y_train = mnist_loader.transform_labels_to_binary(mnist_labels=y_train)

model_params = network.train(
    x_input=x_train,
    y_output=y_train,
    number_of_iterations=1000,
    learning_rate=0.25,
)

with open("/Users/jinal/Desktop/NN-Playground/model_params.pickle", "wb") as f:
    pickle.dump(model_params, f, pickle.HIGHEST_PROTOCOL)


x_test, y_test = mnist_loader.read_images_labels(
    images_filepath="archive/t10k-images.idx3-ubyte",
    labels_filepath="archive/t10k-labels.idx1-ubyte",
)

y_test = mnist_loader.transform_labels_to_binary(mnist_labels=y_test)

y_prediction_train = [
    network.predict(x_input=normalized_x, parameters=model_params)
    for normalized_x in x_test
]
accuracy_train = network.accuracy(
    y_actual=y_train, y_predicted=y_prediction_train
)

y_prediction_test = [
    network.predict(x_input=normalized_x, parameters=model_params)
    for normalized_x in x_test
]
accuracy_test = network.accuracy(
    y_actual=y_test, y_predicted=y_prediction_test
)

print(accuracy_train, accuracy_test)
