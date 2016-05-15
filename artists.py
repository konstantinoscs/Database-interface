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


def render_artists_table(data):
    st = '<meta charset = "utf-8"/> <table style=" ">'
    st += "<h1>View Artist Results</h1><hr>" \
          "<tr><td><strong>National Id</strong></td>" \
          "<td><strong>Name</strong></td>" \
          "<td><strong>Surname</strong></td>" \
          "<td><strong>Birth Year</strong></td></tr>" \
          "<td><strong>Edit?</strong></td>"

    return st