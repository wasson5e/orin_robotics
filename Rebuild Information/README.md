# Rebuilding Steps

## SSD
1) Burn the SSD using the images from Nvidia using Etcher
2) Reinstall the SSD and boot the Nano using the SDCard with the working image
3) Create a mount folder in the Documents folder
```
sudo mount /dev/nvme0n1p1 <mountFolder>
```

4) Update the boot information
```
vim /boot/extlinux/extlinux.conf
```
Change root to `APPEND ${cbootargs} root=/dev/nvme0n1p1`
5) Shutdown the Nano, and remove the SDCard
6) Boot nano and finish installation

## Fix Browser Issue - if there is one
```
sudo snap download snapd --revision=24724
sudo snap ack snapd_24724.assert
sudo snap install snapd_24724.snap
sudo snap refresh --hold snapd
```

## SSH Keys for github
`ssh-keygen`

## Git Commands
Clone the repo using SSH
`git add <file>`
`git commit -m 'MESSAGE'`
`git push`

## Install Jetpack
```
sudo apt update
sudo apt install -y nvidia-jetpack
sudo apt show nvidia-jetpack
```

## Fix NVCC
[Nvidia Developer](https://forums.developer.nvidia.com/t/cuda-nvcc-not-found/118068)
```
vim ~/.bashrc
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64\${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
## Install Common Python3 packages
`sudo apt install python3-pip python3-setuptools python3-venv -y`

## Install Jetson-Stats
[Repo](https://github.com/rbonghi/jetson_stats)
```
sudo pip3 install -U jetson-stats
sudo reboot
```

## ReInstall OpenCV with Cuda
Copy this file to Downloads https://raw.githubusercontent.com/AastaNV/JEP/refs/heads/master/script/install_opencv4.10.0_Jetpack6.1.sh
```
wget https://raw.githubusercontent.com/AastaNV/JEP/refs/heads/master/script/install_opencv4.10.0_Jetpack6.1.sh
chmod +x install_opencv4.10.0_Jetpack6.1.sh
bash ./install_opencv4.10.0_Jetpack6.1.sh
```

## Camera Configuration - Jetson Orin Nano
- Camera in use [IMX477](https://www.arducam.com/arducam-12mp-imx477-motorized-focus-high-quality-camera-for-jetson.html)
- Configuration script - I set it for dual IMX477
`sudo /opt/nvidia/jetson-io/jetson-io.py`
- reboot the system
- check that the camera was found
`ls /dev/video*'
- check video information
```
awasson@orinnano:~$ v4l2-ctl --list-formats-ext
ioctl: VIDIOC_ENUM_FMT
	Type: Video Capture

	[0]: 'RG10' (10-bit Bayer RGRG/GBGB)
		Size: Discrete 4032x3040
			Interval: Discrete 0.048s (21.000 fps)
		Size: Discrete 3840x2160
			Interval: Discrete 0.033s (30.000 fps)
		Size: Discrete 1920x1080
			Interval: Discrete 0.017s (60.000 fps)
```

## v4l2-ctl Command Not Found
```
sudo apt install v4l-utils
```

## Install the following in a python environment (safety first)
1) Create the python environment
`mkdir ~/Documents/cvision && cd ~/Documents/cvision && python -m venv . && source bin/activate`

### Install cuSPARSElt (Step 1)
https://developer.nvidia.com/cusparselt-downloads?target_os=Linux&target_arch=aarch64-jetson&Compilation=Native&Distribution=Ubuntu&target_version=22.04&target_type=deb_network
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/arm64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cusparselt
```

### Install PyTorch (Step 2)
[PyTorch Compatibility](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform-release-notes/pytorch-jetson-rel.html)
[Steps](https://ninjalabo.ai/blogs/jetson_pytorch.html)

```
pip3 install --no-cache https://developer.download.nvidia.com/compute/redist/jp/v61/pytorch/torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libopenblas-dev libavcodec-dev libavformat-dev libswscale-dev
git clone --branch release/0.23 https://github.com/pytorch/vision torchvision
cd torchvision && export BUILD_VERSION=0.23.0
python3 setup.py install --user # remove --user if installing in virtualenv

#might want to try this first - seems like it worked
pip install torch==2.9.0+cu126 torchvision==0.23.0 torchaudio==2.9.0 --index-url https://download.pytorch.org/whl/cu126
```

## Git information
1) recreated SSH keys on nano
2) reinstall sublime and sublime merge

## Build safety
When the system is working, change the "Subscribed to" updates to "Security and recommended updates" or "Security Only" since the last packages broke everything.

## JTop / Jetson-Stats - Jetpack Not Detected
- Get the Jetpack verson and L4T version
`cat /etc/nv_tegra_release`
`sudo apt show nvidia-jetpack`
- Install Jetson_Stats and update the code per [HERE](https://rnext.it/jetson_stats/contributing.html)

## Repair keyboard through CLI
```
bluetoothctl
scan on - look for ED:C0:A9:84:CC:64 ProtoArc
devices
scan off
trust ED:C0:A9:84:CC:64
pair ED:C0:A9:84:CC:64
connect ED:C0:A9:84:CC:64
exit
```


## Ultralytics on Jetson Orin Nano
[Link](https://docs.ultralytics.com/guides/nvidia-jetson/#jetpack-support-based-on-jetson-device)

- Make the directory
`mkdir ~/Documents/Ultralytics && python -m venv --system-site-packages . && source bin/activate`

- Install Ultralytics
```
pip install ultralytics
  
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torch-2.5.0a0+872d972e41.nv24.08-cp310-cp310-linux_aarch64.whl
  
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/torchvision-0.20.0a0+afc54f7-cp310-cp310-linux_aarch64.whl
  
pip install https://github.com/ultralytics/assets/releases/download/v0.0.0/onnxruntime_gpu-1.23.0-cp310-cp310-linux_aarch64.whl
  
pip install numpy==1.23.5
```