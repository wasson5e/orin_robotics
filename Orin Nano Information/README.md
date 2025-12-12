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


## TTL Connection Information
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

## OpenCV 4.12.0 Documentation
https://docs.opencv.org/4.12.0/
