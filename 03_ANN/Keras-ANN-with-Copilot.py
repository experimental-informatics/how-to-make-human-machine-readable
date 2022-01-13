# solving mnist with tensorflow keras and a dense layer

# import all the required libraries
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# load the data
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# output the shape of the data (also was is drinnen in den datensätzen)
print(train_images.shape)
print(test_images.shape)

# output the dimension of the data
print(train_images.ndim)
print(test_images.ndim)

# output the size of the data
print(train_images.size)
print(test_images.size)


# output the dimension of the labels
print(train_labels.ndim)
print(test_labels.ndim)

# output the dimension of the images
print(train_images.ndim)
print(test_images.ndim)



# normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape the data
train_images = train_images.reshape(60000, 28, 28, 1)
test_images = test_images.reshape(10000, 28, 28, 1)

# do a one hot encoding of the labels
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

# create a sequential model with a dense hidden layer with 512 neurons
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu)
])

# create a dense layer with 10 neurons and softmax activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

# make a summary of the model
model.summary()

# compile the model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'])

# train the model and keep track of the loss and accuracy
history = model.fit(
    train_images, train_labels, 
    epochs=5, 
    validation_data=(test_images, test_labels))

# render the loss and validation loss
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.legend()
plt.show()

# render the accuracy and validation accuracy
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.legend()
plt.show()

# evaluate the model using the test data and print the accuracy
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(test_acc)

# show the first image in the test data
plt.imshow(test_images[0].reshape(28, 28), cmap='Greys')
plt.show()

# plott the first image in the test data with the predicted label
predictions = model.predict(test_images)
print(predictions[0])






