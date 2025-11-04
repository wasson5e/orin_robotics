# Orin Nano Build Information

## Build Steps
Nvidia information is shit, so here is what Im finding
[Getting Start Guide](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
- Since the currently available Jetpack 7 version doesnt support the Orin Nano Super, you need to go [HERE](https://developer.nvidia.com/embedded/jetpack-sdk-621) and download version "SD Card Image Method for Jetson Orin Nano Developer Kit" ~12GB
- The image will need to be burned on both an SSD and SDCard
- Connect to the Orin Nano using the TTY connection
- When you see the BIOS message, hit Escape and boot from the SDCard.  
- Log into the system, and then go to the Downloads folder and run ./configure_ssd_boot.sh
```
sudo bash ./configure_ssd_boot.sh 
```
- Power the Orin down, and remove the SDCard, reinstall power and boot from SSD
- Since the SSD is newly flashed, you will have to accept the licensing/finish the setup
- Connect to the Orin using an USB-C cable, and connect directly to the laptop, look for something like
```
/dev/cu.usbmodem14227250685373
```
- Finish doing the configuration

## Jetson-Stats
- Install Jetpack on Orin Nano
```
sudo apt update
sudo apt install -y nvidia-jetpack
sudo apt show nvidia-jetpack
```
## Install Jetson-Stats
[Repo](https://github.com/rbonghi/jetson_stats)
```
sudo apt install python3-pip python3-setuptools -y
sudo pip3 install -U jetson-stats
sudo reboot
```

## NVCC Not Found
[Nvidia Developer](https://forums.developer.nvidia.com/t/cuda-nvcc-not-found/118068)
```
vim ~/.bashrc
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64\
                         ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

## ReInstall OpenCV with Cuda
Copy this file to Downloads https://github.com/AastaNV/JEP/blob/master/script/install_opencv4.10.0_Jetpack6.1.sh
```
chmod +x install_opencv4.10.0_Jetpack6.1.sh
bash ./install_opencv4.10.0_Jetpack6.1.sh
```
## Install PyTorch
[PyTorch Compatibility](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform-release-notes/pytorch-jetson-rel.html)
[Steps](https://ninjalabo.ai/blogs/jetson_pytorch.html)
```
vim cuSPARSELt.sh
chmod +x cuSPARSELt.sh && sudo bash ./cuSPARSELt.sh
pip3 install --no-cache https://developer.download.nvidia.com/compute/redist/jp/v61/pytorch/torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch release/0.23 https://github.com/pytorch/vision torchvision
cd torchvision
export BUILD_VERSION=0.23.0
python3 setup.py install --user # remove --user if installing in virtualenv

#might want to try this first - seems like it worked
pip install torch==2.9.0+cu126 torchvision==0.23.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cu126
```

- Create a new environment off of other venv
```
pip freeze > requirements.txt
```


## Install Python VENV
[VENV](https://docs.python.org/3/library/venv.html)
[Other VENV](https://python.land/virtual-environments/virtualenv)
```
python -m venv ~/Documents/yolo
source ~/Documents/yolo/bin/activate
deactivate



## TTL Connection Informatione
- [TTL](https://www.jetson-ai-lab.com/initial_setup_jon.html)

| Color | Pin |
| ------- | ------- |
| Green | 3 |
| White | 4 |
| Black | 7 |

## Jetpack Version
```
(base) awasson@orinnano:~/Downloads$ sudo apt show nvidia-jetpack
Package: nvidia-jetpack
Version: 6.2.1+b38
Priority: standard
Section: metapackages
Source: nvidia-jetpack (6.2.1)
Maintainer: NVIDIA Corporation
Installed-Size: 199 kB
Depends: nvidia-jetpack-runtime (= 6.2.1+b38), nvidia-jetpack-dev (= 6.2.1+b38)
Homepage: http://developer.nvidia.com/jetson
Download-Size: 29.3 kB
APT-Manual-Installed: yes
APT-Sources: https://repo.download.nvidia.com/jetson/common r36.4/main arm64 Packages
Description: NVIDIA Jetpack Meta Package
```

## Cuda Information
```
(base) awasson@orinnano:~/Downloads$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Wed_Aug_14_10:14:07_PDT_2024
Cuda compilation tools, release 12.6, V12.6.68
Build cuda_12.6.r12.6/compiler.34714021_0
```