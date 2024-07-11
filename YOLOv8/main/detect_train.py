'''
目标检测 训练
'''
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('/home/duanzeying/ws_yolo/yolov8/ultralytics/cfg/models/v8/yolov8x.yaml')

    model.load('yolov8x.pt') # loading pretrain weights
    #model.load('/home/duanzeying/ws_yolo/runs/detect/train34/weights/best.pt') #
    model.train(data='/home/duanzeying/ws_yolo/yolov8/ultralytics/cfg/datasets/voc2012.yaml', 
                batch=32,epochs=200,device=0)
    #for k, v in model.named_parameters():
    #    print(k)





