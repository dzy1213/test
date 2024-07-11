'''
图像分类预测
'''
from ultralytics import YOLO

# Load a model
model = YOLO('runs/classify/train11/weights/best.pt')  # load a custom model

# Predict with the model
results = model('ultralytics/assets',save=True,save_txt=True)  # predict on an image