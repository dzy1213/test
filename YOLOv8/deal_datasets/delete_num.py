'''
删除类别
'''
import os

def delete_lines_with_numbers(directory, numbers_to_delete):
    # 遍历目录中的所有文件
    i=1
    j=1
    for filename in os.listdir(directory):
        # 只处理txt文件
        i=i+1
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            
            # 读取文件内容
            with open(filepath, 'r') as file:
                lines = file.readlines()
            
            # 过滤出第一个数字不在numbers_to_delete中的行
            new_lines = []
            for line in lines:
                # 分割行，检查第一个空格前的部分是否在numbers_to_delete中
                first_word = line.split()[0] if line.split() else ''
                if first_word not in numbers_to_delete:
                    new_lines.append(line)
            
            # 写回文件
            with open(filepath, 'w') as file:
                file.writelines(new_lines)
        if i==1000:
            j=j+1
            print("1000ghhh  ",j,"\n")
            i=1

# 使用示例
directory = '/home/duanzeying/ws_yolo/yolov8/datasets/coco_2014_appleboat/labels/train2017/train'# 替换为你的txt文件所在目录
#numbers_to_delete = [  '8'      '12'              '13',    '24',      '26',     '30',     '43',    '44',    '46',    '47',    '48',       '49',   '50',      '51',     '52',       '60',        '70',   '73'    '78',       '79']  # 替换为你想要删除的数字列表
                    #  boat  parking meter         bench   backpack   hangbag    skis     knife    spoon    banana    apple   sandwich    orange  broccoil   carrot     hotdog    diningtable   toaster  book  hairdrier   toothbrush
#添加boat、apple、orange类别，删掉第九类交通灯 他训练出来置信度最低
numbers_to_delete = [            '12',              '13',    '24',      '26',      '30',    '43',    '44',    '46',            '48',                '50',   '51',  '52',    '60',      '70',     '78',     '79']  # 替换为你想要删除的数字列表

delete_lines_with_numbers(directory, numbers_to_delete)

