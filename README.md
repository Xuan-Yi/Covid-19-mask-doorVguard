# Covid 19-mask-doorVguard

## Installation (For Windows 10)
It's recommended to use [**Anaconda Python**](https://www.anaconda.com/products/individual), or you will suffer from installing piles of modules.

#### [Anaconda Python](https://www.anaconda.com/products/individual)
It's recommended to always run `pip` and `conda` in **anaconda prompt** to ensure that every modules are installed in anaconda environment but not other pythons, expecially `pip`.

#### [face_recognition](https://anaconda.org/conda-forge/face_recognition)
```conda install -c conda-forge face_recognition```

#### [opencv](https://pypi.org/project/opencv-python/)
```pip install opencv-python```

#### [Pandas](https://anaconda.org/anaconda/pandas)
```conda install -c anaconda pandas```

#### [Pytorch]((https://pytorch.org/))
* Go to [pytorch](https://pytorch.org/), you will get the command to install Pytorch and other required modules. In **PyTorch Build**, please choose **Stable**. In **Package**, choose **Conda**. In **Language**, chooses **Python**. In **Compute Platform**, if you have a GPU that support CUDA, choose the latest CUDA version that your CPU support, or just choose **CPU** if you have no GPU. Then copy the command in **Run this Command:** to your Anaconda prompt and run!
* As seen in the conda command, CUDA has been installed; therefore, you needn't go to CUDA website to downloaad and install CUDA again.
* cuDNN is also a awesome tool, but I'm still finding method to access it in Pytorch.

### [keras](https://pypi.org/project/keras/)
```pip install keras```

### [tensorflow](https://pypi.org/project/tensorflow/)
```pip install tensorflow```

### [pygame](https://pypi.org/project/pygame/)
```pip install pygame```

# Frame
I've seperated this code into 3 processes:
1. Generate data (**Data Generator**)
2. Generator model (**Model Generator**)
3. Realize face mask recognition

I'will introduce these parts step by step below.

## Generate data
* That is, the folder **Data Generator**
* This folder should look like the following:
    ```
    Data Generator
        |- data
            |- without_mask
            |- with_black_mask  (auto generated)
            |- with_blue_mask   (auto generated)
            |- with_white_mask  (auto generated)
        |- images
        |- loop_through_folder.py
        |- mask.py
    ```
* Run **loop_through_folder.py**, then data will be generated,i.e. , folder *data* will be complete.
* You can also get files from [Files](#Files)

## Generate model
* That is, the folder **Model  Generator**
* This folder should look like the following:
    ```
    Model Generator
        |- experimernts (auto generated)
            |- data
                |- with_mask
                |- without_mask
            |- dest_folder
                |- test
                |- train
                |- test.csv 
                |- train.csv
        |- training.ipynb
    ```
* Run **training.ipynb**, then the model *mask_recognition_model.pth* will be generated automatically (See next part).

## Realize face mask recognition
* This is at the top layer, so it looks like:
    ```
    Covid-19-mask-doorVguard
        |- Data Generator
        |- Model Generator
        |- alarm.wav
        |- mask_recognition_model.pth   (auto generated)
        |- label_detect.py
        |- webcam_detect.py
    ```
* Run *webcam_detect.py*, then the computer will start detecting.

### Files
1. [images.zip](https://drive.google.com/file/d/1kDngXx2uwEYMJvxP5jqWJRq_K8HZ1FET/view?usp=sharing)
    * These are images of face mask.
    * This folder should be under `Covid-19-mask-doorVguard/Data Generator`
3. [without_mask.zip](https://drive.google.com/file/d/18W7alkle8MhNarnxcdZveMt2eEXOwmwV/view?usp=sharing)
    * This are images of faces.
    * This folder should be under `Covid-19-mask-doorVguard/Data Generator/data`
    * Image source are [here](https://github.com/prajnasb/observations.git) and Google.
4. [experiements.zip](https://drive.google.com/file/d/1hIF20_zFoS-TAJ3BmJ3HSJ0dTFR9CPvi/view?usp=sharing)
    * This folder can also be generated automatically, so you actually needn't download this file.
5. [mask_recognition_model.zip](https://drive.google.com/file/d/1iRQ3-7Vn1hATtzjIhWjpQH5LKY8YE0SK/view?usp=sharing)
    * This is the final model for face mask recognition, and can also be generated automatically, so you needn't download this file, either.

# Announcement
* Most code are from [here](https://github.com/prajnasb/observations.git)
* This is one of my final project, I'm tidying it up recently, so it may be imcomplete now.
    
  
