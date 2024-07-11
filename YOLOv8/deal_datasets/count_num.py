'''
统计文件夹下的文件个数
'''
import os

def count_files_in_folder(folder_path):
    count = 0
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 对于每个文件，增加计数器
        count += len(files)
    return count

folder_path = "/home/duanzeying/ws_yolo/yolov8/datasets/coco_2014_delete13/images/train2017/val"  # 修改为你的文件夹路径
file_count = count_files_in_folder(folder_path)
print("image文件夹中的文件个数:", file_count)
