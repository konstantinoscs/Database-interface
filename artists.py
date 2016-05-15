# -*- coding: utf-8 -*-

from connection import connection

def find_artists(name, surname, byear_from, byear_to, type):
    con = connection()

    try:
        with con.cursor() as cursor:
            sql = "select `ar_taut`, `onoma`, `epitheto`, `etos_gen` from `kalitexnis`" \
                  "where `onoma` = %s and `epitheto` = %s and " \
                  "`etos_gen` > %s and `etos_gen` < %s"
            cursor.execute(sql, (name, surname, byear_from, byear_to))
            data = cursor.fetchall()
    finally:
        con.close()