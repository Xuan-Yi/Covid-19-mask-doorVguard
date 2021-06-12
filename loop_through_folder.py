import os

import cv2

from mask import create_mask

# 原圖片的資料夾路徑
folder_path = "D:/NTUEE/g1s/電資工程設計與實作(車車課)/自選專題 Arduino/Data_Generator/data/without_mask_k"
images = [os.path.join(folder_path, f) for f in os.listdir(
    folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for i in range(len(images)):
    print("the path of the image is", images[i])
    create_mask(images[i])
