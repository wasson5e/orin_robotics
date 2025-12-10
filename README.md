# Orin Robotics

## Nvidia Links
[PyTorch Orin Nano](https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html)

## Testing Commands
`nvgstcapture-1.0 --orientation 2` - Opens the camera and rotates 180 due to being flipped

## Label-Studio-Converter
```
(label-studio) root@94c756140b69:/orin-robotics# label-studio-converter import coco -h
usage: label-studio-converter import coco [-h] -i INPUT [-o OUTPUT] [--to-name TO_NAME] [--from-name FROM_NAME] [--out-type OUT_TYPE]
                                          [--image-root-url IMAGE_ROOT_URL] [--point-width POINT_WIDTH]

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        directory with COCO where images, labels, notes.json are located
  -o OUTPUT, --output OUTPUT
                        output file with Label Studio JSON tasks
  --to-name TO_NAME     object name from Label Studio labeling config
  --from-name FROM_NAME
                        control tag name from Label Studio labeling config
  --out-type OUT_TYPE   annotation type - "annotations" or "predictions"
  --image-root-url IMAGE_ROOT_URL
                        root URL path where images will be hosted, e.g.: http://example.com/images
  --point-width POINT_WIDTH
                        key point width (size)
```

label-studio-converter import coco -i '/orin-robotics/datasets/coco' -o '/orin-robotics/datasets/coco_output'

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

## GStreamer
[Pipeline](https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c)
