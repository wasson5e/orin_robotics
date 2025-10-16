# YOLO
- Trying to build out a custom YOLO model that will include people/animals for use at the house

## Yolov11 Infrastructure
| Variant | Backbone Modules | Backbone Layers | Neck Modules | Neck Layers | Head Modules | Head Layers | Total Layers |
| -------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| n (nano)| 11| 36| 12| 28| 1| 139| 20|


## Conda ENV
- yolo
```
conda activate yolo
```

## Label Studio
```
label-studio
```

# Reference information
- ejtech.io/learn/train-yolo-models
- github.com/ultralytics
- labelstud.io/guide
- github.com/HumanSignal/label-studio
- docs.ultralytics.com/guies/data-collection-and-annotation
- [Yolo Webcam](https://github.com/nudro/yolo-webcam/blob/main/webcam_detection.py)

## Background information
- [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

## Training with an established model
```
# Example: Train YOLOv5s on the COCO128 dataset for 3 epochs
python train.py --img 640 --batch 16 --epochs 3 --data coco128.yaml --weights yolov5s.pt
```

## retrain the system while freezing the base information
- So you dont lose what was already there.
- [Frozen Layers](https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/)
```
python train.py --weights yolov5s.pt --data /Users/awasson/Documents/GitLab/yolo/data.yaml --freeze 10 --batch 16
```

## Links
- [YOLOv11](https://docs.ultralytics.com/models/yolo11)
- [YOLO OBB](https://docs.ultralytics.com/tasks/obb/)
- [YOLO Modes](https://docs.ultralytics.com/modes)
- [Ultralytics Main Repo](https://github.com/ultralytics/ultralytics)
- [Yolo Performance Metrics](https://docs.ultralytics.com/guides/yolo-performance-metrics)
- [YOLOv11 Backbone information](https://github.com/orgs/ultralytics/discussions/20876)


## Test out the model
```
```