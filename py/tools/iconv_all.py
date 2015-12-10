#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
将文件从gb2312编码转换为utf8编码
源文件的目录为src，转换后的文件目录为dest
Created on 2015年12月10日

@author: dlooss
"""

import os
import commands


def iconv(rootDir, destDir):
    for lists in os.listdir(rootDir):
        srcPath = os.path.join(rootDir, lists)
        desPath = os.path.join(destDir, lists)
        # print "%s to %s" % (srcPath, desPath)
        if os.path.isdir(srcPath):
            os.system("mkdir -p " + desPath)
            iconv(srcPath, desPath)
        else:
            cmd = "iconv -f gb2312 -t utf-8 %s -o %s" % (srcPath, desPath)
            # os.system("iconv -f gb2312 -t utf-8 %s -o %s" % (srcPath, desPath))
            (status, output) = commands.getstatusoutput(cmd)
            # print cmd, status, output
            if (status != 0):
                print cmd, status, output
                cmd = "cp %s %s" % (srcPath, desPath)
                (status, output) = commands.getstatusoutput(cmd)
                print cmd, status, output
            else:
                print "success", cmd


if __name__ == '__main__':
    ROOT_DIR = "./src"
    DEST_DIR = "./dest"
    os.system("mkdir -p " + DEST_DIR)

    iconv(ROOT_DIR, DEST_DIR)
