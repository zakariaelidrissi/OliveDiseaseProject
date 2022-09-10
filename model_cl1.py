# import library important
from random import random

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import os
import glob

# -------------------------------------------------
def get_files(directory):
  if not os.path.exists(directory):
    return 0
  count = 0
  # crawls inside folders
  for current_path, dirs, files in os.walk(directory):
    for dr in dirs:
      count += len(glob.glob(os.path.join(current_path, dr+"/*")))
  return count

# dataset direction
train_dir = r"D:\cours\Master IAAD\S2\Projet 1\Projet\dataset_olive\train"
test_dir  = r"D:\cours\Master IAAD\S2\Projet 1\Projet\dataset_olive\test"

# -----------------------------------------
# train file image count
train_samples = get_files(train_dir)
# to get tags
num_classes = len(glob.glob(train_dir+"/*"))
# test file image count
test_samples = get_files(test_dir)
print(num_classes, "Classes")
print(train_samples, "Train images")
print(test_samples, "Test images")

# ------------------------------------
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
test_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

# ---------------------------------------
input_shape = (224, 224, 3)
train_generator = train_datagen.flow_from_directory(train_dir, target_size=(224, 224), batch_size=32)
test_generator = test_datagen.flow_from_directory(test_dir, shuffle=True, target_size=(224, 224), batch_size=32)


# load model vgg19
model_vgg19 = load_model(r'D:\cours\Master IAAD\S2\Projet 1\Projet\oliveProjet\model_cl1_vgg19.h5')


classes_vgg19 = list(train_generator.class_indices.keys())
# Pre-Processing test data same as train data.
def prepare(img_path):
  img = image.load_img(img_path, target_size=(224, 224))
  x = image.img_to_array(img)
  x = x/255
  return np.expand_dims(x, axis=0)


def predictionCl1(img_url):
    result_vgg19 = model_vgg19.predict([prepare(img_url)])
    classresult_vgg19 = np.argmax(result_vgg19, axis=1)

    proba = np.max(result_vgg19)
    print(proba)

    return classes_vgg19[classresult_vgg19[0]], proba
