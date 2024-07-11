"""
寻找labels文件中含有某个类别的文件,并将相应的图片、标注文件分类放到不同文件夹下.
"""
import os
import shutil

def process_files(folder1, folder2, folder3, folder4, folder5, folder6):
    # 定义需要匹配的数字列表
    match_numbers = ['2','5','11','17']
    i=0
    j=0
    for filename in os.listdir(folder1):  # 遍历文件夹1中的所有txt文件
        if filename.endswith(".txt"):
            file_path = os.path.join(folder1, filename)#每个txt文件的路径
            img_filename = os.path.splitext(filename)[0] + ".jpg"  # 将文件后缀名替换为jpg
            img_path = os.path.join(folder4, img_filename)#每个img文件的路径
            
            with open(file_path, 'r') as file:
                lines = file.readlines()
               # 检查文件中是否存在行的第一个数字是匹配数字列表中的任意一个
                match_found = any(line.strip().split()[0] in match_numbers for line in lines)
                if match_found:
                    shutil.copy(file_path, folder2)
                    shutil.copy(img_path, folder5)
                    #i=i+1
                else:
                    shutil.copy(file_path, folder3)
                    shutil.copy(img_path, folder6)
                    #j=j+1
    #print(i,j,i+j)
    print("分配完成！")

# 用法示例
folder1 = "C:/Users/王航/Desktop/labels"  # 文件夹1路径
folder2 = "C:/Users/王航/Desktop/labels_9"  # 存放存在第一个数字是9的txt文件的文件夹路径
folder3 = "C:/Users/王航/Desktop/labels_no9"  # 存放不存在第一个数字是9的txt文件的文件夹路径
folder4 = "C:/Users/王航/Desktop/images"  # 文件夹4路径
folder5 = "C:/Users/王航/Desktop/images_9"  # 存放与文件夹2中文件名一致的图片的文件夹路径
folder6 = "C:/Users/王航/Desktop/images_no9"  # 存放与文件夹3中文件名一致的图片的文件夹路径

process_files(folder1, folder2, folder3, folder4, folder5, folder6)
