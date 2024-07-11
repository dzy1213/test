'''
图像分类训练
'''
from ultralytics import YOLO

# Load a model
model = YOLO('ultralytics/cfg/models/v8/yolov8x-cls.yaml')  # build a new model from YAML
model.load('yolo_cls.pt')  # build from YAML and transfer weights

# Train the model
results = model.train(data='datasets/classify', epochs=100)
