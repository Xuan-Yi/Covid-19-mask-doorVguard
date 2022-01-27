import os
import cv2
from mask import create_mask

# path of original face images(without_mask)
face_folder_path = os.path.join(
    os.getcwd(), "Data Generator/data/without_mask")
face_images = [os.path.join(face_folder_path, f) for f in os.listdir(
    face_folder_path) if os.path.isfile(os.path.join(face_folder_path, f))]
# paath of mask images
mask_folder_path = os.path.join(os.getcwd(), "Data Generator/images")
mask_images = [os.path.join(mask_folder_path, f) for f in os.listdir(
    mask_folder_path)if os.path.isfile(os.path.join(mask_folder_path, f))]

for i in range(len(face_images)):
    print("path of original: ", face_images[i])
    for j in range(len(mask_images)):
        create_mask(face_images[i], mask_images[j])
