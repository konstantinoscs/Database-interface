# -*- coding: utf-8 -*-
import pymysql
import settings

def connection():
    con = pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset="utf8",
        use_unicode=True)
    con.set_charset('utf8')
    con.cursor().execute('SET NAMES utf8;')
    con.cursor().execute('SET CHARACTER SET utf8;')
    con.cursor().execute('SET character_set_connection=utf8;')

    return con
