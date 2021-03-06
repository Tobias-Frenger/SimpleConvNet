# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:04:57 2020

@author: Tobias
"""
#imports
from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.pyplot as plt

import tensorflow.keras as keras
to_categorical = keras.utils.to_categorical
# Load and prepare the MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# Convert to from integers to floating-point numbers
x_train, x_test = x_train / 255.0, x_test / 255.0

# Look at one of the images in the dataset
plt.imshow(x_train[0])

# Check the shape of the image
x_train[0].shape

# Data pre-processing
x_train = x_train.reshape(60000,28,28,1)
x_test = x_test.reshape(10000,28,28,1)

# One-hot encode target column?
y_train = to_categorical (y_train)
y_test = to_categorical (y_test)

y_train[0]
#build a sequential model by stacking layers
model = keras.models.Sequential([
        keras.layers.Conv2D(64, kernel_size=3, strides=1, activation ='relu',input_shape=(28,28,1)),
        keras.layers.MaxPool2D(pool_size=(2, 2), strides=1, padding='valid'),
        keras.layers.Conv2D(32, kernel_size=3, strides=1, activation='relu'),
        keras.layers.MaxPool2D(pool_size=(2, 2), strides=1, padding='valid'),
        keras.layers.Flatten(),
        keras.layers.Dense(16, activation='relu'),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10, activation='softmax')
        ])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train and evaluate the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5)
model.evaluate(x_test, y_test, verbose=2)