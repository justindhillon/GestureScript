# How to make your own AI model

This directory has everything you need to make the AI model.

## Install Dependencies

Run this command to install dependencies

    pip install -r requirements.txt

## Getting Images

Run this script to use your webcam to capture training images.

    python get-images.py

The files are in ```training-images/collected-images```

## Seting Up labelImg

```bash
git submodule update

cd labelImg

# Install pyqt5 on Ubuntu
sudo apt-get install pyqt5-dev-tools

# Install pyqt5 on Fedora
sudo dnf install PyQt5

# Build and runing labelImg.py
make qt5py3
python3 labelImg.py
```

## Using labelImg

1. ```Open Dir``` training-images/collected-images
2. ```Change Save Dir``` training-images/collected-images
3. Set ```Auto Save Mode``` in ```view```
4. Use ```Create RectBox``` on all the training-images

## Move Images

Once the images are labeled with labelImg, we need to allocate some of them for training and others for testing. Each symbol has 15 images. Copy 13 of the images to ```training-images/training```, and the other 2 to ```training-images/testing```.

## Setup Label Map & TFRecords

Run this script to generate ```annotations/label_map.rbtxt```, ```annotations/train.record```, and ```annotations/test.record```

    python create-label-map.py

## Train the model

Run this script to train the model.

    python train.py

You can find the final model in ```GSL-model```.
