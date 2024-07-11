"""
将label中的txt文件的类别数全部改为80
"""

import os
# 指定标签文件夹路径
folder_path = 'val/'

# 循环遍历文件夹中的每一个文件
for filename in os.listdir(folder_path):
    # 仅处理txt文件
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        # 打开文件并逐行读取内容
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # 修改每一行的第一个数字为80
        modified_lines = ['80' + line[1:] for line in lines]
        # 写入修改后的内容到同一文件
        with open(file_path, 'w') as file:
            file.writelines(modified_lines)

print("修改完成！")