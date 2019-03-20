# -*- coding: utf-8 -*-

import hashlib
import os
import time
import shutil
# 文件备份


def md5check(file):
    """
        检查文件一致性，通过文件md5进行一致性检查。备份有差异的文件。
        file：文件绝对路径
    """
    m = hashlib.md5()
    with open(file) as fobj:
        while True:
            data = fobj.read(4096)
            if (not data):
                break
            m.update(data)
    return m.hexdigest()


def copy(path):
    """
        对文件进行备份，如果文件内容相同但文件名不一样则替换文件名。
        path：文件绝对路径
    """
    new_path = path
    new_path = new_path.replace(old_source, new_source)  # 自动成成新文件的路径。

    # 由于win系统默认不区分大小写因此将所有文件的路径全部转为大写[小写可以]。
    if(os.path.isfile(new_path.upper())):
        old_md5 = md5check(path)
        new_md5 = md5check(new_path)
        if old_md5 != new_md5:  # 文件修改过
            shutil.copy(path, new_path)
            print("文件\""+path+"\",备份完成。")
        else:
            ddirs = path.split(r"/")
            dd = ''
            for ddir in ddirs:
                if ddir == ddirs[1]:
                    dd = ddir
                elif ddir == ddirs[-2]:
                    dd = dd + "/" + ddir
            for root, dirs, files in os.walk(dd):
                for file in files:
                    if new_path.split(r"/")[-1] == file:
                        pass
                    else:
                        os.remove(new_path)
                        time.sleep(1)
                        shutil.copy(path, new_path)
                        print("文件\""+path+"\",重命名完成。")
            pass
    else:  # 文件不存在
        dirname = os.path.dirname(new_path)
        if (os.path.exists(dirname)):
            shutil.copy(path, new_path)
        else:
            try:
                os.makedirs(dirname)
                print(("创建文件夹\""+dirname+"\",完成"))
                shutil.copy(path, new_path)
                print(("文件\""+path+"\",备份完成。"))
            except WindowsError:
                print(("目标目录\"" + dirname + "\"创建失败,请手动创建该目录"))


def lsdir(forder):
    '''
        判断路径是否为文件夹
        forder： 绝对路径但不一定是文件。
    '''
    path = os.listdir(forder)

    for line in path:
        line = forder + "/" + line
        if(r"/." in line):
            continue
        if (os.path.isdir(line)):
            lsdir(line)
        else:
            copy(line)


if __name__ == '__main__':
    global old_source
    global new_source
    print("开始进行文件备份，请勿关闭当前窗口。\n完成备份时会有相应提示。")
    old_source = input("请输入要备份的目录，示例[D:/xxx/xxx]：")
    new_source = input("请输入存放备份文件的目录，示例[D:/xxx/xxx]：")
    if old_source:
        old_source
    else:
        old_source = "D:/code/server_new"
    if new_source:
        new_source
    else:
        new_source = "D:/code/backup1"

    lsdir(old_source)

    concent = "备份已完成，输入任意键结束程序"
    print(concent)

    input()
