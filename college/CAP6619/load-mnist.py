#!/bin/python3

# Load in the MNIST dataset into keras and create a basic model
# to classify handwritten digits as a number between 0 and 9.
#
# A little starting point for first deep learning
# example.

import time

from keras import models, layers
from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#
# Create an initial model
#
network = models.Sequential()

#
# Add two layers to this model
#
# Dense (fully connected) layers with the size of data inputs (28 x 28)
# designed to distillate the data.
# 
# Last layer can be considered the 10 digit output. These "neurons" give
# a probabalistic value between 0 and 1 to represent what the input
# likely is (a digit between 0 and 9).

network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

#
# Compile the model
#

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

#
# Prepare image data
#
# Reshape test/training sets into 2D array (from 3D), also
# cast values to be float32 and divide each value by 255 to 
# transform greyscale values from 0 - 255 to 0 - 1.

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

#
# Encode Labels
#

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#
# Train model
#
# Run training data through model 5 times (epochs)

tm1 = time.time()
network.fit(train_images, train_labels, epochs=5, batch_size=128)
tm2 = time.time()

print('training took %f' % (tm2 - tm1))

#
# Output model loss/accuracy
#

test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)
