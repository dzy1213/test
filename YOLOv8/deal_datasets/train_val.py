"""
对数据集进行训练集、验证集的划分
"""
import os
import random
import shutil

def split_and_match_files(folder1_images, folder2_txts, folder3, folder4, folder5, folder6, num_images1, num_images2):
    # 获取文件夹1中所有图片的文件名
    image_files = [f for f in os.listdir(folder1_images) if f.endswith('.jpg')]

    # 获取文件夹2中所有txt文件的文件名
    txt_files = [f for f in os.listdir(folder2_txts) if f.endswith('.txt')]

    # 确保文件夹1中的图片与文件夹2中的txt文件一一对应
    if len(image_files) != len(txt_files):
        print("图片与txt文件数量不一致，请检查！")
        return

    # 随机打乱图片文件的顺序
    random.shuffle(image_files)

    # 创建文件夹3和文件夹4
    os.makedirs(folder3, exist_ok=True)
    os.makedirs(folder4, exist_ok=True)

    # 分配图片到文件夹3和文件夹4中
    for i in range(len(image_files)):
        if i < num_images1:
            shutil.copy(os.path.join(folder1_images, image_files[i]), folder3)
        else:
            shutil.copy(os.path.join(folder1_images, image_files[i]), folder4)

    # 创建文件夹5和文件夹6
    os.makedirs(folder5, exist_ok=True)
    os.makedirs(folder6, exist_ok=True)

    # 匹配txt文件与图片文件名，并复制到文件夹5和文件夹6中
    for txt_file in txt_files:
        image_name = os.path.splitext(txt_file)[0] + '.jpg'
        if os.path.exists(os.path.join(folder3, image_name)):
            shutil.copy(os.path.join(folder2_txts, txt_file), folder5)
        elif os.path.exists(os.path.join(folder4, image_name)):
            shutil.copy(os.path.join(folder2_txts, txt_file), folder6)
        else:
            print(f"未找到与txt文件 {txt_file} 对应的图片")

    print("图片和txt文件分配完成！")

# 设置文件夹路径
folder1_images = 'C:/Users/王航/Desktop/images_9'
folder2_txts = 'C:/Users/王航/Desktop/labels_9'
folder3 = 'C:/Users/王航/Desktop/images_c'#train图片         #合并到源文件夹
folder4 = 'C:/Users/王航/Desktop/images_add'#val图片        #待添加的
folder5 =  'C:/Users/王航/Desktop/labels_c'#train标签
folder6 = 'C:/Users/王航/Desktop/labels_add'#val标签

# 分配图片和txt文件，并匹配
split_and_match_files(folder1_images, folder2_txts, folder3, folder4, folder5, folder6, 1144, 1144)

