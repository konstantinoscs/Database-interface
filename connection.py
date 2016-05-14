import pymysql
import settings

def connection():
    con = pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema)
    return con
