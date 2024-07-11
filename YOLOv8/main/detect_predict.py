'''
目标检测 预测
'''
from ultralytics import YOLO

# Load a model
model = YOLO('ws_yolo/runs/detect/train30/weights/best.pt')  # load an official model
#model = YOLO('yolov8x.pt')  # load an official model

results = model.predict('ws_yolo/yolov8/ultralytics/assets', save=True)  # predict on an image


