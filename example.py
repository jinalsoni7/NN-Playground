from nnplayground import network, mnist_loader

x_train, y_train = mnist_loader.read_images_labels(
    images_filepath="archive/train-images.idx3-ubyte",
    labels_filepath="archive/train-labels.idx1-ubyte",
)

y_train = mnist_loader.transform_labels_to_binary(mnist_labels=y_train)
x_train = mnist_loader.normalize_pixel_values(mnist_images=x_train)

model_params = network.train(
    x_input=x_train,
    y_output=y_train,
    number_of_iterations=5,
    learning_rate=0.25,
)

x_test, y_test = mnist_loader.read_images_labels(
    images_filepath="archive/t10k-images.idx3-ubyte",
    labels_filepath="archive/t10k-labels.idx1-ubyte",
)

y_test = mnist_loader.transform_labels_to_binary(mnist_labels=y_test)
x_test = mnist_loader.normalize_pixel_values(mnist_images=x_test)

y_prediction_train = network.predict(x_input=x_train, parameters=model_params)
accuracy_train = network.accuracy(
    y_actual=y_train, y_predicted=y_prediction_train
)

y_prediction_test = network.predict(x_input=x_test, parameters=model_params)
accuracy_test = network.accuracy(
    y_actual=y_test, y_predicted=y_prediction_test
)

print(accuracy_train, accuracy_test)
