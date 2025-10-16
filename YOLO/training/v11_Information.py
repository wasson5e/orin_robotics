#model information
#Use on the conda environment yolo
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

for name, param in model.named_parameters():
    print(name)