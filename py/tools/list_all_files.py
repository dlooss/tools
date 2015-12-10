#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
递归列出指定根目录下的所有文件

Created on 2015年12月10日

@author: dlooss
"""
import os
import sys


def list_all(dir_name):
    for file in os.listdir(dir_name):
        path = os.path.join(dir_name, file)
        # print "%s to %s" % (srcPath, desPath)
        if os.path.isdir(path):
            list_all(path)
        else:
            print(path)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python list_all_files.py dir_name")
        exit(1)
    root_dir = sys.argv[1]

    list_all(root_dir)
