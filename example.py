from nnplayground import network, mnist_loader

x_train, y_train = mnist_loader.read_images_labels(
    images_filepath="/path/to/images/ubyte", labels_filepath="/path/to/labels/ubyte"
)

model_params = network.train(
    x_input=x_train, y_output=y_train, number_of_iterations=1000, learning_rate=0.25
)

x_test, y_test = mnist_loader.read_images_labels(
    images_filepath="/path/to/images/ubyte", labels_filepath="/path/to/labels/ubyte"
)

y_prediction = network.predict(x_input=x_test, parameters=model_params)

accuracy = network.accuracy(y_actual=y_test, y_predicted=y_prediction)
