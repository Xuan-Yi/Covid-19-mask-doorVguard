# Covid 19-mask-doorVguard

## Installation (For Windows 10)
Before the following installation, you are expected to have your **python** and **pip** intalled.
### Required for mask-dooorVguard
#### numpy
```pip install numpy```

#### Pillow (PIL)
```pip install Pillow```

#### face_recognition
```pip install face-recognition```

#### OpenCV-python (cv2)
You can check [Official Tutorial](https://pypi.org/project/opencv-python/) or follow the steps given below(simplified from the official tutorial).

1. If you have previous/other manually installed (= not installed via pip) version of OpenCV installed (e.g. cv2 module in the root of Python's site-packages), remove it before installation to avoid conflicts.
2. Make sure that your ```pip``` version is up-to-date (19.3 is the minimum supported version): ```pip install --upgrade pip```. Check version with ```pip -V```.
3. Install opencv package via ```pip install opencv-python```.

If you still run into  problems, please check [Official Tutorial](https://pypi.org/project/opencv-python/)

[OpenCV Documentation](https://docs.opencv.org/master/)

#### PyTorch and Torchvision (torch, torchvision)
In [https://pytorch.org/](https://pytorch.org/), you will get the pip command to install Pytorch and Torchvision. In **PyTorch Build**, please choose **Stable**. In **Package**, choose **Pip**. **Language**, of course **Python**. In **Compute Platform**, if you have a GPU that support CUDA, choose **CUDA 11.1**(the latest cuda version) and install the corresponding CUDA (refer to [this tutorial](https://www.programmersought.com/article/44961416825/)), or just choose **CPU**. Then copy the command in **Run this Command:** to your command prompt and run press enter!

#### Matplotlib (matplotlib)
```pip install matplotlib```

#### pygame 
```pip install pygame```

### Not Required for mask-dooorVguard (for other tests)
#### dlib (not required)
You can follow the steps given  in [this website](https://ibe.tw/install-dlib-for-python3-on-windows/), this method is the easiest method I've found now. Mind that new version of dlib for python cannot be installed directly via ```pip```.

#### imutils
```pip install imutils```

### For recognition of facial landmarks
For facial landmarks recognition, we need a model. Actually, dlib has its build-in models. Here is another readily-trained model ```shape_predictor_68_face_landmarks.dat```, but is not allowed for commercial usage. Here is the license: 
``` 
C. Sagonas, E. Antonakos, G, Tzimiropoulos, S. Zafeiriou, M. Pantic. 
300 faces In-the-wild challenge: Database and results. 
Image and Vision Computing (IMAVIS), Special Issue on Facial Landmark Localisation "In-The-Wild". 2016.
```
You can find *shape_predictor_68_face_landmarks.dat.bz2* [here](https://github.com/davisking/dlib-models/blob/daf943f7819a3dda8aec4276754ef918dc26491f/shape_predictor_68_face_landmarks.dat.bz2), please unzip it in the folder where your .py file is.



    
  
