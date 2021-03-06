# README
# This file was originally a Jupyter file written in Pycharm. 
# Each #%% corresponds to a new cell within Jupyter

#%%

import tensorflow as tf  # deep learning library. Tensors are just multi-dimensional arrays
import numpy as np
mnist = tf.keras.datasets.mnist  # mnist is a dataset of 28x28 images of handwritten digits and their labels
(x_train, y_train),(x_test, y_test) = mnist.load_data()  # unpacks images to x_train/x_test and labels to y_train/y_test

x_train = tf.keras.utils.normalize(x_train, axis=1)  # scales data between 0 and 1
x_test = tf.keras.utils.normalize(x_test, axis=1)  # scales data between 0 and 1

#Much more accurate when normalized to values between 0 and 1, think sigmoid function

model = tf.keras.models.Sequential()  # a basic feed-forward model
model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784 vector
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))  # our output layer. 10 units for 10 classes. Softmax for probability distribution

model.compile(optimizer='adam',  # Good default optimizer to start with, one I learned was stochastic gradient descent
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track

model.fit(x_train, y_train, epochs=4)  # train the model

#%%

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss) # too much loss will result in memorization of the set (overfitting) or no accuracy
print(val_acc)

#%%

model.save('num_reader.model')

#%%

import tensorflow as tf
new_model = tf.keras.models.load_model('num_reader.model')

#%%

predictions = new_model.predict(np.array([x_test]))
# arg max returns element with highest value (probability)

#%%

print(predictions)

#%%

import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import random
import time

from IPython.display import clear_output


def button_create():
    btn = widgets.Button(description='Random Number')
    display(btn)
    def btn_eventhandler(obj):
        rand()
    btn.on_click(btn_eventhandler)

button_create()

def rand():
    clear_output()
    button_create()
    time.sleep(.1)
    
    x = random.randint(0,10000) #since 10000 test data
    print(np.argmax(predictions[x]))
    
    plt.imshow(x_test[x],cmap=plt.cm.binary)
    plt.show()

#%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2

DATADIR = "C:/Users/2bran/PycharmProjects/NN2/test.png" #png will prevent the strange dithering

#img_array = mpimg.imread(DATADIR)
img_array = cv2.imread(DATADIR,cv2.IMREAD_GRAYSCALE)
print(img_array.shape) #WORKS HERE

# print(img_array)
#It did print the image as a numpy array

img_array = tf.keras.utils.normalize(img_array, axis=1)

plt.imshow(img_array, cmap = plt.cm.binary)
plt.show()

#plt.cm.binary show BW inverted, yes

#plt.imshow(test, cmap = 'gray')
#print(test)

# NEEDED PIL FOR THIS APPARENTLY

#%%

img_array = np.array(img_array).reshape(-1, 28, 28) # need -1 so total size remains constant
print(np.argmax(new_model.predict(img_array)))

#%%

print(img_array)
#plt.imshow(x_test[1],cmap=plt.cm.binary)
#print(np.argmax(predictions[1]))

#%%

# testing function should be CLEAR SAVE PREDICT
from numpy import complex, array

# from urllib import request
# # access request directly.
# mine = request()
# 
# import urllib.request
# # used as urllib.request
# mine = urllib.request()



import numpy
from tkinter import *
from PIL import Image, ImageEnhance
import tkinter.font
import tkinter as tk

def drawnum():
    clear_output()
    button_2()
    time.sleep(.1)
    
    WIDTH = 250
    
    img = Image.new('RGB', (WIDTH, WIDTH)) # originally black bg
    pixels = img.load() # to use pixels [x, y]
    
    #plt.imshow(img, cmap = plt.cm.binary) #transforms to white, works!
    #plt.show()
    
    #img.show() # showing the PNG file
    
    # ---- Define class -----
    class PaintApp:
    
    # ---- Define class variables -----
        drawing_tool = "pencil"
        
        left_but  = "up"
    
        x_pos, y_pos = None, None # null valaue
    
        x1_line_pt, y1_line_pt = None, None
    
    # ---- Catch Mouse Down ----- 
        def left_but_down(self, event = None):
            self.left_but = "down"
        
            self.x1_line_pt = event.x
            self.y1_line_pt = event.y
        
    # ---- Catch Mouse Up -----
        def left_but_up(self, event = None):
            self.left_but = "up"
        
            self.x_pos = None
            self.y_pos = None
        
            if self.drawing_tool == "line":
                self.line_draw(event)
                
    # ---- Catch Mouse Move -----
        def motion(self, event = None):
    
            if self.drawing_tool == "pencil":
                self.pencil_drawing(event)
                
    # ---- Draw Pencil -----
    
        def pencil_drawing(self, event = None):
            
            x = self.x_pos
            y = self.y_pos
            
            if self.left_but == "down":
                if self.x_pos is not None and self.y_pos is not None and 1 <= x <= WIDTH - 3 and 1 <= y <= WIDTH - 3:
                    
                    event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE)
                    # event.widget.create_line(self.x_pos + 1, self.y_pos, event.x, event.y, smooth = TRUE)
                    # event.widget.create_line(self.x_pos - 1, self.y_pos, event.x, event.y, smooth = TRUE)
                    # event.widget.create_line(self.x_pos, self.y_pos + 1, event.x, event.y, smooth = TRUE)
                    # event.widget.create_line(self.x_pos, self.y_pos - 1, event.x, event.y, smooth = TRUE)

              
                    for i in range(10):
                        
                        if x>=WIDTH - 12 or x <= 1 or y <= 1 or y >= WIDTH - 12: #accounting for border
                            break
                        
                        num = 160
                    
                        pixels[x + i, y] = (170 -  num, 170 -  num, 170 - num)
                        pixels[x - i, y] = (170 -  num, 170 - num, 170 - num)
                        pixels[x, y - i] = (170 -  num, 170 - num, 170 - num)
                        pixels[x, y + i] = (170 -num, 170 - num, 170 - num)
                        pixels[x - i, y + i] = (170 - num, 170 - num, 170 - num)
                        pixels[x - i, y + i] = (170 - num, 170 - num, 170 - num)
                        pixels[x + i, y - i] = (170 - num, 170 - num, 170 - num)
                        pixels[x - i, y - i] = (170 - num, 170 - num, 170 - num)
                        pixels[x,y] = (170 - num, 170 - num, 170 - num)
                        
                     
                    
                        # pixels[x + i, y] = 1
                        # pixels[x - i, y] = 1
                        # pixels[x, y - i] = 1
                        # pixels[x, y + i] = 1
                        # pixels[x - i, y + i] = 1
                        # pixels[x - i, y + i] = 1
                        # pixels[x + i, y - i] = 1
                        # pixels[x - i, y - i] = 1
                        # pixels[x,y] = 1
                    
                self.x_pos = event.x
                self.y_pos = event.y
            
    # ---- Initialize -----
    
        def __init__(self, root):
            drawing_area = Canvas(root, width = WIDTH, height = WIDTH) # REMEMBER TO RESHAPE AFTER
        
            drawing_area.pack()
        
            drawing_area.bind("<Motion>", self.motion)
            drawing_area.bind("<ButtonPress-1>", self.left_but_down)
            drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
    
    root = Tk() #main window of application, THIS IS MAKING AN OBJECT OF Tk CLASS
    paint_app = PaintApp(root)
    root.mainloop()
    
    
    #new_img = np.array(img)
    new_img = img.convert('I')
    new_img = tf.keras.utils.normalize(new_img, axis=1)
    new_img = cv2.resize(new_img, (28, 28))

    
    plt.imshow(new_img, cmap = plt.cm.binary) #transforms to white, works!
    plt.show()

    

    data = np.array(new_img).reshape(-1, 28, 28) # need -1 so total size remains constant
    print(np.argmax(new_model.predict(data)))


def button_2():
    btn2 = widgets.Button(description='Draw a number')
    display(btn2)
    def btn2_eventhandler(obj):
        drawnum()
    btn2.on_click(btn2_eventhandler)

button_2()

    


