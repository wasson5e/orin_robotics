# YOLO
- Trying to build out a custom YOLO model that will include people/animals for use at the house

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