#!/usr/bin/env python
# coding: utf-8


import copy
import glob
import os
import shutil
import time

import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
from PIL import Image
from sklearn.model_selection import train_test_split
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms

filepath = "D:/NTUEE/g1s/電資工程設計與實作(車車課)/自選專題 Arduino/Model_Generator/mask_recognition_model2.pth"
model = torch.load(filepath)


class_names = ['with_mask',
               'without_mask'
               ]


def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''

    # TODO: Process a PIL image for use in a PyTorch model
    #pil_image = Image.open(image)
    pil_image = image

    image_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    img = image_transforms(pil_image)
    return img


def classify_face(image):
    device = torch.device("cuda:0")    # "cpu"
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #im_pil = image.fromarray(image)
    #image = np.asarray(im)
    im = Image.fromarray(image)
    image = process_image(im)
    print('image_processed')
    img = image.unsqueeze_(0)
    img = image.float()

    model.eval()
    model.cpu()
    output = model(image)
    print(output, '##############output###########')
    _, predicted = torch.max(output, 1)
    print(predicted.data[0], "predicted")

    classification1 = predicted.data[0]
    index = int(classification1)
    print(class_names[index])
    return class_names[index]


if __name__ == '__main__':
    # map_location=torch.device('cpu')
    image = cv2.imread('praj.jpg')
    label = classify_face(image)
    print("the label is", label)
