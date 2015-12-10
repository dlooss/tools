#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
打开数据库客户端

Created on 2015年12月10日

@author: dlooss
"""
import sys
from commons import get_sql_util

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Usage: python mysql_client [dbname]")
        exit(1)

    if len(sys.argv) == 2:
        get_sql_util(sys.argv[1]).run_mysql_client()
    else:
        get_sql_util().run_mysql_client()
