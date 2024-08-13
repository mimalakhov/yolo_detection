import torch
from IPython.display import Image  # for displaying images
import os 
import random
import shutil
from sklearn.model_selection import train_test_split
import xml.etree.ElementTree as ET
from xml.dom import minidom
from tqdm import tqdm
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# Read images and annotations
train_images = [os.path.join('Notes_Dataset/images/train', x) for x in os.listdir('Notes_Dataset/images/train')]
train_annotations = [os.path.join('Notes_Dataset/labels/train', x) for x in os.listdir('Notes_Dataset/labels/train') if x[-3:] == "txt"]

val_images = [os.path.join('Notes_Dataset/images/val', x) for x in os.listdir('Notes_Dataset/images/val')]
val_annotations = [os.path.join('Notes_Dataset/labels/val', x) for x in os.listdir('Notes_Dataset/labels/val') if x[-3:] == "txt"]


train_images.sort()
train_annotations.sort()

val_images.sort()
val_annotations.sort()