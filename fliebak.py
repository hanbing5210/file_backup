# -*- coding: utf-8 -*-
import os,hashlib
# 获取源目录中单个文件
def get_source_file(source_path):
    if os.path.isdir(source_path):
        if os.listdir(source_path):
            with open(source_path, mode='rb') as f:
                file = f.read()
                return file
    else:
        with open(source_path, mode='rb') as f:
                file = f.read()
                return file
                
def get_target_file(target_path):
    if os.path.isdir(target_path):
        if os.listdir(target_path):
            with open(target_path, mode='rb') as f:
                file = f.read()
                return file
    else:
        with open(source_path, mode='rb') as f:
                file = f.read()
                return file
def set_target_file(target_path,file_bytes):
    with open(target_path,mode="wb") as f:
        f.write(file_bytes)

def get_source_filenames(path):
    files_name=os.listdir(path)
    print(files_name)
    paths = []
    for file_name in files_name:
        file_path = os.path.join( path,file_name)
        a= (file_name,file_path)
        paths.append(a)
    return paths

if __name__ == '__main__':
    source_path = input("请输入源路径:")# 如果是固定备份位置的话可以将这个变量写死
    target_path = input("请输入备份路径:")# 如果是固定备份位置的话可以将这个变量写死
    if os.path.exists(target_path):
        pass
    else:
        os.makedirs(target_path)
    # 获取源目录文件列表及文件名
    source_files = get_source_filenames(source_path)
    # files_name=[]
    # for source_file in source_files:
    #     if os.path.isdir(source_file[1]):
    #         print(source_file[0]+"是文件夹")
    #     elif os.path.isfile(source_file[1]):
    #         print(source_file[0]+"是文件")
    #     else:
    #         pass

    #     files_name.append(source_file[0])
    # 获取备份目录文件列表
    target_files = get_source_filenames(target_path)
    print(target_files)
    # 检查源目录中的文件是否被备份
    for source_file in source_files:
        # 检查源目录中的文件是否被备份
        target_path1 = os.path.join(target_path,source_file[0])

        if not (source_file[1] in target_files):
            source_file_bitys = get_source_file(source_file[1])
            set_target_file(target_path1,source_file_bitys)
            print(source_file[1])
            print(target_path)
            print("文件备份完成")
        else:
            for target_file in target_files:
                if target_file[0]==source_file[0]:
                    source_md5 = hashlib.md5(get_source_file(source_file)).hexdigest()
                    target_md5 = hashlib.md5(get_target_file(target_file)).hexdigest()
                    if source_md5==target_md5:
                        print("文件已存在,无需备份")
                    else:
                        set_target_file(target_path, get_source_file(source_file[1]))
                        print("文件更新完成")
    print("文件已备份完成 :)")
