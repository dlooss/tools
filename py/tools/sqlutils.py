#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Created on 2015年9月12日

@author: dlooss
"""

import os


class SqlCommandUtil(object):
    """
    Mysql 命令行工具类
    """

    def __init__(self, host="127.0.0.1", port=3306, dbname="", user="", password="", mysql_bin="mysql"):
        """
        初始化
        """
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.mysql_bin = mysql_bin

    def export_data_from_db(self, sql, filepath):
        """
                根据sql从数据库中导出数据到文件file中
        """
        command = '%s -h%s -P%d -D%s -u%s -p%s --skip-column-names -N -e "%s" > %s' % \
                  (self.mysql_bin, self.host, self.port, self.dbname,
                   self.user, self.password, sql, filepath)
        print 'command: ' + command

        return os.system(command)

    def run_mysql_client(self):
        """
        打开mysql客户端
        """
        command = '%s -h%s -P%d -D%s -u%s -p%s' % \
                  (self.mysql_bin, self.host, self.port,
                   self.dbname, self.user, self.password)
        print 'command: ' + command

        return os.system(command)
