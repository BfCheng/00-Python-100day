#！/user/bin/python3
# -*- coding : utf-8 -*-
# @Author: cheng.bingfeng
# @Date: 2021/1/12
# @Last Modified by: cheng.bingfeng
# @Last Modified time: 21:05
# @File Name: pictureGroup.py
import os, shutil

rootDir = r'C:\Users\dongxuezhen\Desktop\Source'     #需要处理的文件源路径，仅替换''单引号之间的内容即可
desPath = r'C:\Users\dongxuezhen\Desktop\Destination'        #需要处理的文件的目的地路径，仅替换''单引号之间的内容即可
keyWord = '后面'      #需要处理的文件标签，例如'正面', '侧面'， '仪表板视图'
#######=======================================#######
#######*********以下内容不需要进行修改**********######

# ===================================================
def pictureGroup(rootDir, desPath, keyWord):

    print('*********************')
    # print('Processing***********')
    desPath = os.path.join(desPath, keyWord)        #返回文件真实源文件路径
    list = os.listdir(rootDir)      #返回文件夹中有多少个子文件夹数量

    for i in range(len(list)):
        store = []
        path = os.path.join(rootDir, list[i])
        if os.path.isdir(path):
            for item in os.listdir(path):
                store.append(item)
            # print(store)
            for n in range(0, len(store)):
                if store[n].split('_')[0] == keyWord:
                # print(store[n].split('_')[0])
                    dirname = os.path.join(rootDir, list[i])
                    fullPath = os.path.join(dirname, store[n])
                    itemNew = os.path.join(os.path.abspath(desPath), list[i]+'_'+store[n])
                    shutil.copy(fullPath, itemNew)
                    print(itemNew)

pictureGroup(rootDir, desPath, keyWord)
print('**********DONE**********')

