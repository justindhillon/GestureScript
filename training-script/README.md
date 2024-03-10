# How to make your own AI model
This directory has everything you need to make the AI model.

## Install Dependencies
Run this command to install dependencies
```bash
pip3 install pyqt5 lxml
```

## Getting Images
Run this script to use your webcam to capture training images.
```bash
python get-images.py
```
The files are in ```training-images/collected-images```

## Seting Up labelImg

```bash
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
