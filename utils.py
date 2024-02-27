import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
import pytesseract
from keras.layers import Flatten


def ocr_core(image):
    text = pytesseract.image_to_string(image)
    return text


#create the model
def ocrModel():
  model = Sequential()
  model.add(Conv2D(32, (4,4), strides = (1,1), activation = 'relu', input_shape = (128, 128, 1)))
  model.add(MaxPooling2D(pool_size = (4,4), strides = (2,2)))
  model.add(Conv2D(64, (4,4), strides = (1,1), activation = 'relu', input_shape = (128, 128, 1)))
  model.add(MaxPooling2D(pool_size = (4,4),strides = (2,2)))

  model.add(Flatten())

  model.add(Dense(310, activation='relu'))
  model.add(Dense(12, activation = 'softmax'))

  model.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics = ['accuracy'])

  return model