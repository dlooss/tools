#! /usr/bin/python
# -*- coding:utf-8 -*-

"""
Created on 2015年12月10日

@author: dlooss
"""

from sqlutils import SqlCommandUtil
import ConfigParser

CONF_FILE = 'config.ini'


def get_conf(config_file_path=CONF_FILE):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)
    return cf


def get_sql_util(name='default'):
    cf = get_conf()
    section = "db_" + name

    if cf.has_section(section):
        return SqlCommandUtil(host=cf.get(section, "host"),
                              port=cf.getint(section, "port"),
                              dbname=cf.get(section, "dbname"),
                              user=cf.get(section, "user"),
                              password=cf.get(section, "password"),
                              mysql_bin=cf.get("db", "mysql_bin") or "mysql",
                              )
    else:
        raise Exception("unknown database name: " + name)
