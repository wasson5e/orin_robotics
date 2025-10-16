#Use on the conda environment yolo
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model.train(data="/Users/awasson/Documents/GitLab/orin-robotics/YOLO/dataset/sophia_dataset.yaml", epochs=30, imgsz=640, device='mps', freeze=23, batch=16)
