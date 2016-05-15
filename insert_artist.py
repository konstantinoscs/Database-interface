# -*- coding: utf-8 -*-
import pymysql
from connection import *


def insert_artist(id, name, surname, byear):

    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "insert into `kalitexnis` (`ar_taut`, `onoma`, `epitheto`, `etos_gen`) " \
                  "values (%s, %s, %s, %s)"
            cursor.execute(sql, (id, name, surname, byear))
            con.commit()

    finally:
        con.close()