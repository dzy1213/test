# YOLOv8：目标检测及图像分类模型

## 项目简介

YOLOv8（You Only Look Once）是目前最先进的实时目标检测模型，基于其前几代的模型进行改进，从而实现更高效的目标检测性能。YOLOv8 采用深度学习，仅需一次处理即可完成图像分析，使其异常快速，适用于需要实时性能的应用场景。

该模型可用于目标检测及图像分类等场景.关于 YOLOv8 模型更详细的介绍，可以查阅[YOLOv8 官方代码](https://github.com/ultralytics/ultralytics)

## 主要工作

- 基于本项目要求，制作目标检测数据集，并在数据集上使用 YOLOv8x 模型进行训练，最终在 63 个通用目标检测类别上实现 MAP 为 87.9%的检测效果。

- 基于本项目要求，制作图像分类数据集，并在数据集上使用 YOLOv8x-cls 模型进行训练，实现对 256 个常用物体的图像分类，top1_acc 达到 86.6%。

## 项目结构介绍

- datasets ：存放数据集
- deal_datasets ：数据集处理所需的代码
- docker ：包含多个 Dockerfile，为不同环境或平台配置，用户可以根据自己的需要选择合适的环境来部署和运行项目
- docs ：存放文档资料，包括多种语言的翻译
- examples ：存放不同编程语言和平台的 YOLOv8 实现示例
- main ：存放运行项目（训练、预测）的 python 文件
- runs ：存放训练结果
  - result_detect ：本项目目标检测的训练结果
  - result_classify ：本项目图像分类的训练结果
- tests ：包含自动测试脚本，用于确保代码的稳定性和性能
- ultralytics ：YOLOv8 的核心代码目录，包含实现模型功能的所有代码
  - assets ：包含项目的静态资源，如图像、预训练模型文件等。这些资源被用于测试、文档或软件中的示例
  - cfg ：存放配置文件，这些文件定义了模型的结构、训练参数等
  - data : 包含与数据处理相关的脚本和文件，如数据集的配置文件或数据预处理代码
  - engine : 包含实现 YOLOv8 核心功能的代码，例如模型训练、验证和推理的引擎
  - hub ：与 PyTorch Hub 集成的代码，允许用户更容易地下载和使用 YOLOv8 模型
  - models : 包含不同 YOLOv8 模型配置的文件
  - nn : 包含神经网络组件的代码，如自定义层、激活函数等
  - trackers : 存放与对象跟踪相关的配置文件
  - solutions : 提供特定解决方案的代码，如线计数和圆形热图功能
  - utils : 包含各种实用程序和辅助函数，如图像处理、性能度量计算等

## 训练方法

### 运行环境

```
python==3.8.0  torch==2.2.1  ultralytics=8.1.27
```

安装环境运行以下脚本：

```
pip install ultralytics
pip install -r requirement.txt
```

### 训练脚本

- 目标检测

训练：

```
yolo detect train data=ultralytics/cfg/datasets/coco128.yaml model=ultralytics/cfg/models/v8/yolov8x.yaml pretrained=yolov8x.pt epochs=100 batch=16 lr0=0.01 resume=true device=\'0,1,2,3\'
```

预测：

```
yolo predict model=runs/detect/train8/weights/best.pt source=ultralytics/assets save_txt=True save_conf=True
```

验证：

```
yolo detect val data=ultralytics/cfg/datasets/social.yaml model=runs/detect/train8/weights/best.pt split='test'
```

- 图像分类

训练：

```
yolo classify train data=/home/duanzeying/ws_yolo/yolov8/datasets/classify model=ultralytics/cfg/models/v8/yolov8x-cls.yaml pretrained=yolov8x-cls.pt epochs=100
```

验证：

```
yolo predict model=runs/classify/train4/weights/best.pt source=ultralytics/assets
```

### 训练文件

main 文件夹中存放训练目标检测、图像分类模型的 python 文件：

- detect_train.py : 目标检测训练文件
- detect_predict.py : 目标检测预测文件
- classify_train.py : 图像分类训练文件
- classify_predict.py : 图像分类预测文件

## 权重文件下载

### YOLOv8 官方权重

- 目标检测：
  | Model | size<br><sup>(pixels) | mAP<sup>val<br>50-95 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) |
  | ------------------------------------------------------------------------------------ | --------------------- | -------------------- | ------------------------------ | ----------------------------------- | ------------------ | ----------------- |
  | [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt) | 640 | 37.3 | 80.4 | 0.99 | 3.2 | 8.7 |
  | [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s.pt) | 640 | 44.9 | 128.4 | 1.20 | 11.2 | 28.6 |
  | [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m.pt) | 640 | 50.2 | 234.7 | 1.83 | 25.9 | 78.9 |
  | [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l.pt) | 640 | 52.9 | 375.2 | 2.39 | 43.7 | 165.2 |
  | [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x.pt) | 640 | 53.9 | 479.1 | 3.53 | 68.2 | 257.8 |

- 图像分类：
  | Model | size<br><sup>(pixels) | acc<br><sup>top1 | acc<br><sup>top5 | Speed<br><sup>CPU ONNX<br>(ms) | Speed<br><sup>A100 TensorRT<br>(ms) | params<br><sup>(M) | FLOPs<br><sup>(B) at 640 |
  | -------------------------------------------------------------------------------------------- | --------------------- | ---------------- | ---------------- | ------------------------------ | ----------------------------------- | ------------------ | ------------------------ |
  | [YOLOv8n-cls](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n-cls.pt) | 224 | 69.0 | 88.3 | 12.9 | 0.31 | 2.7 | 4.3 |
  | [YOLOv8s-cls](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s-cls.pt) | 224 | 73.8 | 91.7 | 23.4 | 0.35 | 6.4 | 13.5 |
  | [YOLOv8m-cls](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m-cls.pt) | 224 | 76.8 | 93.5 | 85.4 | 0.62 | 17.0 | 42.7 |
  | [YOLOv8l-cls](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l-cls.pt) | 224 | 76.8 | 93.5 | 163.0 | 0.87 | 37.5 | 99.7 |
  | [YOLOv8x-cls](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x-cls.pt) | 224 | 79.0 | 94.6 | 232.0 | 1.01 | 57.4 | 154.8 |

### 基于本项目自行训练权重

- 目标检测：
- 图像分类：

## 数据集介绍

### 目标检测

[COCO (Common Objects in Context)](https://cocodataset.org/#home—)是一个大规模的图像数据集，广泛用于计算机视觉领域的研究，可用于对象实例分割(Instance Segmentation)、目标检测(Object Detection)、关键点检测(Keypoint Detection)、图像分类(Image Classification)等。COCO2014 数据集是其中一个版本，包含了丰富的图像和注释信息。以下是 COCO2014 数据集的详细介绍：

- 数据集概况

图像数量：训练集：73,460 张图像 ； 验证集：40,504 张图像

类别：
COCO2014 数据集共包含 80 个物体类别，包含人、动物、日常物品、交通工具等多个常用类别。

文件格式和结构：
COCO2014 数据集的注释文件使用 JSON 格式，主要分为以下几部分：
images：包含每张图像的元数据，如图像 ID、文件名、宽度、高度等。
annotations：包含每个对象的详细注释信息，如对象 ID、所属类别、边界框坐标、分割掩码、关键点坐标等。
categories：包含所有类别的信息，如类别 ID、类别名称等。
licenses：包含数据集图像的版权信息。

- 数据集处理

基于本项目要求，删除了 COCO2014 数据集中 16 个类别，剩余 64 个类别。

删除类别：
parking meter，bench，backpack，hangbag，skis，knife，spoon，banana，sandwich，
broccoil，carrot，hot dog，dining table，toaster，hairdrier，toothbrush。

剩余类别：
person,bicycle,car,motorcycle,airplane,bus,train,truck,boat,traffic light,
fire hydrant,stop sign,bird,cat,dog,horse,sheep,cow,elephant,bear,zebra,
giraffe,umbrella,tie,suitcase,frisbee,snowboard,sports ball,kite,baseballbat,
baseball glove,skateboard,surfboard,tennis racket,bottle,wine glass,cup,fork,
bowl,apple,orange,pizza,donut,cake,chair,couch,potted plant,bed,toilet,tv,
laptop,mouse,remote,keyboard,cell phone,microwave,oven,sink,refrigerator,book,
clock,vase,scissors,teddy bear。

- 数据集下载地址 ：[coco2014 数据集下载-阿里云盘](http)

### 图像分类

- 数据集概况

[Caltech-256](http://www.vision.caltech.edu/Image_Datasets/Caltech256/)是一个图像识别数据集，由加州理工学院（Caltech）开发，包含 30,607 个不同大小的真实世界图像，涵盖 256 个类别（256 个对象类别和一个额外的杂波类别）。 每个类别至少有 80 张图像，最多类别包含 827 张图像。图像的分辨率各不相同，一般在 300x300 像素左右。

- 数据集处理

此工作暂未结束

- 数据集下载地址 ：

### 数据集处理相关代码说明

deal_datasets 文件夹中，存放处理数据集的 python 文件:

- count_num.py : 统计文件夹中的文件个数
- delete_num.py : 遍历数据集中的标注文件，删除指定类别的标注信息
- find_num.py : 遍历数据集中的标注文件，找出包含某指定类别的标注信息，并将对应标注信息及图片放到指定文件夹中
- json_to_txt.py : 标注格式转换，由 json 格式转为 txt 格式
- replace_labelnum.py : 遍历数据集中的标注文件，替换某些类别的标注序号
- train_val.py : 训练集与验证集划分
- xml_to_txt.py : 标注格式转换，由 xml 格式转为 txt 格式
